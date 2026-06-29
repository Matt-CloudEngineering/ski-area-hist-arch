from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Collection, HistoricalAsset, HistoricalSnapshot, Institution, Resort
from .schemas import CollectionOut, HistoricalAssetOut, HistoricalSnapshotOut, InstitutionOut, ResortOut

app = FastAPI(
    title="Fantasy Shred Ski Area Historical Archive API",
    version="2.0.0",
    description="Evidence-centered API for ski-area history, archival collections, historical snapshots, maps, aerials, and GIS-ready metadata.",
)


@app.on_event("startup")
def startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "version": "2.0.0"}


@app.get("/resorts", response_model=list[ResortOut])
def list_resorts(db: Session = Depends(get_db)):
    return db.scalars(select(Resort).order_by(Resort.name)).all()


@app.get("/resorts/{resort_id}", response_model=ResortOut)
def get_resort(resort_id: str, db: Session = Depends(get_db)):
    resort = db.get(Resort, resort_id)
    if resort is None:
        raise HTTPException(status_code=404, detail="Resort not found")
    return resort


@app.get("/resorts/{resort_id}/snapshots", response_model=list[HistoricalSnapshotOut])
def list_resort_snapshots(resort_id: str, db: Session = Depends(get_db)):
    return db.scalars(
        select(HistoricalSnapshot)
        .where(HistoricalSnapshot.resort_id == resort_id)
        .order_by(HistoricalSnapshot.year)
    ).all()


@app.get("/resorts/{resort_id}/assets", response_model=list[HistoricalAssetOut])
def list_resort_assets(resort_id: str, db: Session = Depends(get_db)):
    return db.scalars(
        select(HistoricalAsset)
        .where(HistoricalAsset.resort_id == resort_id)
        .order_by(HistoricalAsset.date_start, HistoricalAsset.title)
    ).all()


@app.get("/institutions", response_model=list[InstitutionOut])
def list_institutions(db: Session = Depends(get_db)):
    return db.scalars(select(Institution).order_by(Institution.name)).all()


@app.get("/collections", response_model=list[CollectionOut])
def list_collections(db: Session = Depends(get_db)):
    return db.scalars(select(Collection).order_by(Collection.title)).all()


@app.get("/assets", response_model=list[HistoricalAssetOut])
def list_assets(asset_type: str | None = None, db: Session = Depends(get_db)):
    stmt = select(HistoricalAsset).order_by(HistoricalAsset.date_start, HistoricalAsset.title)
    if asset_type:
        stmt = stmt.where(HistoricalAsset.asset_type == asset_type)
    return db.scalars(stmt).all()

from sqlalchemy import Boolean, Date, Float, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Institution(Base):
    __tablename__ = "institutions"

    id: Mapped[str] = mapped_column(String(120), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    type: Mapped[str | None] = mapped_column(String(80))
    geographic_coverage: Mapped[dict | None] = mapped_column(JSON)
    digital_access: Mapped[str | None] = mapped_column(String(120))
    contact_status: Mapped[str | None] = mapped_column(String(120))
    partnership_status: Mapped[str | None] = mapped_column(String(120))

    collections: Mapped[list["Collection"]] = relationship(back_populates="institution")


class Collection(Base):
    __tablename__ = "collections"

    id: Mapped[str] = mapped_column(String(120), primary_key=True)
    institution_id: Mapped[str | None] = mapped_column(ForeignKey("institutions.id"))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    date_range: Mapped[str | None] = mapped_column(String(120))
    subject_coverage: Mapped[dict | None] = mapped_column(JSON)
    access_restrictions: Mapped[str | None] = mapped_column(Text)
    estimated_item_count: Mapped[int | None] = mapped_column(Integer)
    digitization_status: Mapped[str | None] = mapped_column(String(120))

    institution: Mapped[Institution | None] = relationship(back_populates="collections")
    assets: Mapped[list["HistoricalAsset"]] = relationship(back_populates="collection")


class Resort(Base):
    __tablename__ = "resorts"

    id: Mapped[str] = mapped_column(String(120), primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    state: Mapped[str | None] = mapped_column(String(80))
    country: Mapped[str | None] = mapped_column(String(80))
    status: Mapped[str | None] = mapped_column(String(80))
    summary: Mapped[str | None] = mapped_column(Text)
    official_site: Mapped[dict | None] = mapped_column(JSON)
    coordinates: Mapped[dict | None] = mapped_column(JSON)
    coverage: Mapped[dict | None] = mapped_column(JSON)

    assets: Mapped[list["HistoricalAsset"]] = relationship(back_populates="resort")
    snapshots: Mapped[list["HistoricalSnapshot"]] = relationship(back_populates="resort")
    lifecycle_events: Mapped[list["LifecycleEvent"]] = relationship(back_populates="resort")


class HistoricalAsset(Base):
    __tablename__ = "historical_assets"

    id: Mapped[str] = mapped_column(String(160), primary_key=True)
    asset_type: Mapped[str] = mapped_column(String(80), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    resort_id: Mapped[str | None] = mapped_column(ForeignKey("resorts.id"))
    collection_id: Mapped[str | None] = mapped_column(ForeignKey("collections.id"))
    date_start: Mapped[str | None] = mapped_column(String(40))
    date_end: Mapped[str | None] = mapped_column(String(40))
    source_url: Mapped[str | None] = mapped_column(Text)
    rights_status: Mapped[str | None] = mapped_column(String(120))
    provenance: Mapped[dict | None] = mapped_column(JSON)
    confidence_score: Mapped[int | None] = mapped_column(Integer)

    resort: Mapped[Resort | None] = relationship(back_populates="assets")
    collection: Mapped[Collection | None] = relationship(back_populates="assets")


class HistoricalSnapshot(Base):
    __tablename__ = "historical_snapshots"

    id: Mapped[str] = mapped_column(String(160), primary_key=True)
    resort_id: Mapped[str] = mapped_column(ForeignKey("resorts.id"), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    label: Mapped[str | None] = mapped_column(String(255))
    summary: Mapped[str | None] = mapped_column(Text)
    metrics: Mapped[dict | None] = mapped_column(JSON)
    asset_ids: Mapped[dict | None] = mapped_column(JSON)
    confidence_score: Mapped[int | None] = mapped_column(Integer)

    resort: Mapped[Resort] = relationship(back_populates="snapshots")


class LifecycleEvent(Base):
    __tablename__ = "lifecycle_events"

    id: Mapped[str] = mapped_column(String(160), primary_key=True)
    resort_id: Mapped[str] = mapped_column(ForeignKey("resorts.id"), nullable=False)
    event_type: Mapped[str] = mapped_column(String(80), nullable=False)
    event_date: Mapped[str | None] = mapped_column(String(40))
    description: Mapped[str] = mapped_column(Text, nullable=False)
    source_ids: Mapped[dict | None] = mapped_column(JSON)
    confidence_score: Mapped[int | None] = mapped_column(Integer)

    resort: Mapped[Resort] = relationship(back_populates="lifecycle_events")


class GeographicLayer(Base):
    __tablename__ = "geographic_layers"

    id: Mapped[str] = mapped_column(String(160), primary_key=True)
    resort_id: Mapped[str | None] = mapped_column(ForeignKey("resorts.id"))
    layer_type: Mapped[str] = mapped_column(String(80), nullable=False)
    effective_date: Mapped[str | None] = mapped_column(String(40))
    geometry_format: Mapped[str | None] = mapped_column(String(80))
    geometry_source: Mapped[str | None] = mapped_column(Text)
    source_asset_id: Mapped[str | None] = mapped_column(ForeignKey("historical_assets.id"))
    confidence_score: Mapped[int | None] = mapped_column(Integer)


class OralHistory(Base):
    __tablename__ = "oral_histories"

    id: Mapped[str] = mapped_column(String(160), primary_key=True)
    interviewee: Mapped[str | None] = mapped_column(String(255))
    role: Mapped[str | None] = mapped_column(String(255))
    resort_ids: Mapped[dict | None] = mapped_column(JSON)
    interview_date: Mapped[Date | None] = mapped_column(Date)
    recording_url: Mapped[str | None] = mapped_column(Text)
    transcript_url: Mapped[str | None] = mapped_column(Text)
    rights_status: Mapped[str | None] = mapped_column(String(120))
    related_asset_ids: Mapped[dict | None] = mapped_column(JSON)

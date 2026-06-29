import json
from pathlib import Path

import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from apps.api.database import Base, SessionLocal, engine  # noqa: E402
from apps.api.models import HistoricalAsset, HistoricalSnapshot, Resort  # noqa: E402

AREAS_DIR = ROOT / "archive" / "areas"


def stable_id(*parts: str) -> str:
    return "-".join(str(part).lower().replace(" ", "-").replace("/", "-") for part in parts if part)


def seed() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        for path in sorted(AREAS_DIR.glob("*.json")):
            data = json.loads(path.read_text())
            resort = Resort(
                id=data["id"],
                name=data["name"],
                state=data.get("state"),
                country=data.get("country"),
                status=data.get("status"),
                summary=data.get("summary"),
                official_site=data.get("official_site"),
                coordinates=data.get("coordinates"),
                coverage=data.get("coverage") or {
                    "trail_maps": "partial" if data.get("map_references") else "missing",
                    "aerial_imagery": "missing",
                    "lift_history": "missing",
                    "ownership_history": "missing",
                    "oral_histories": "missing",
                    "gis_ready": False,
                },
            )
            db.merge(resort)

            for idx, map_ref in enumerate(data.get("map_references", []), start=1):
                asset = HistoricalAsset(
                    id=stable_id(data["id"], "map", str(idx)),
                    asset_type="trail_map",
                    title=map_ref.get("title") or f"{data['name']} trail map reference",
                    resort_id=data["id"],
                    date_start=map_ref.get("year_range"),
                    date_end=map_ref.get("year_range"),
                    source_url=map_ref.get("url"),
                    rights_status=map_ref.get("rights_status"),
                    provenance={"original_creator": None, "current_holder": None, "digitized_by": None},
                    confidence_score=80,
                )
                db.merge(asset)

            for item in data.get("historical_snapshots", []):
                snapshot = HistoricalSnapshot(
                    id=item.get("id") or stable_id(data["id"], str(item.get("year"))),
                    resort_id=data["id"],
                    year=int(item["year"]),
                    label=item.get("label"),
                    summary=item.get("summary"),
                    metrics=item.get("metrics"),
                    asset_ids=item.get("asset_ids"),
                    confidence_score=item.get("confidence_score"),
                )
                db.merge(snapshot)

        db.commit()
        print("Seed complete")
    finally:
        db.close()


if __name__ == "__main__":
    seed()

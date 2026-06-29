from typing import Any
from pydantic import BaseModel, ConfigDict


class InstitutionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    type: str | None = None
    geographic_coverage: dict[str, Any] | None = None
    digital_access: str | None = None
    contact_status: str | None = None
    partnership_status: str | None = None


class CollectionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    institution_id: str | None = None
    title: str
    date_range: str | None = None
    subject_coverage: dict[str, Any] | None = None
    access_restrictions: str | None = None
    estimated_item_count: int | None = None
    digitization_status: str | None = None


class ResortOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    state: str | None = None
    country: str | None = None
    status: str | None = None
    summary: str | None = None
    official_site: dict[str, Any] | None = None
    coordinates: dict[str, Any] | None = None
    coverage: dict[str, Any] | None = None


class HistoricalAssetOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    asset_type: str
    title: str
    resort_id: str | None = None
    collection_id: str | None = None
    date_start: str | None = None
    date_end: str | None = None
    source_url: str | None = None
    rights_status: str | None = None
    provenance: dict[str, Any] | None = None
    confidence_score: int | None = None


class HistoricalSnapshotOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    resort_id: str
    year: int
    label: str | None = None
    summary: str | None = None
    metrics: dict[str, Any] | None = None
    asset_ids: dict[str, Any] | None = None
    confidence_score: int | None = None

# Archive Schema v2

This schema expands the archive from resort-centered records to evidence-centered historical documentation.

## Core Entities

```text
Institution
Collection
HistoricalAsset
HistoricalSnapshot
Resort
Lift
OwnershipEvent
LifecycleEvent
OralHistory
GeographicLayer
Contributor
```

## Institution

```json
{
  "id": "new-england-ski-museum",
  "name": "New England Ski Museum",
  "type": "museum",
  "geographic_coverage": ["Northeastern United States"],
  "digital_access": "partial",
  "collections": [],
  "contact_status": "not contacted",
  "partnership_status": "research only"
}
```

## Collection

```json
{
  "id": "vermont-trail-map-collection",
  "institution_id": "vermont-ski-and-snowboard-museum",
  "title": "Vermont Trail Map Collection",
  "date_range": "1930-present",
  "subject_coverage": ["trail maps", "resort brochures", "photographs"],
  "access_restrictions": "varies by item",
  "estimated_item_count": null,
  "digitization_status": "partial"
}
```

## Historical Asset

```json
{
  "id": "whiteface-1978-trail-map",
  "asset_type": "trail_map",
  "title": "Whiteface Mountain Trail Map",
  "resort_id": "whiteface-mountain",
  "collection_id": null,
  "date_start": "1978",
  "date_end": "1978",
  "source_url": null,
  "rights_status": "link-only pending review",
  "provenance": {
    "original_creator": "resort or publisher pending confirmation",
    "current_holder": null,
    "digitized_by": null
  },
  "confidence_score": 90
}
```

## Historical Snapshot

Historical snapshots are the primary bridge between evidence and resort history.

```json
{
  "id": "whiteface-1978",
  "resort_id": "whiteface-mountain",
  "year": 1978,
  "label": "Whiteface - 1978",
  "assets": [],
  "trail_count": null,
  "lift_count": null,
  "vertical_feet": null,
  "skiable_acres": null,
  "ownership": null,
  "operator": null,
  "notes": [],
  "confidence_score": 70
}
```

## Lifecycle Event

```json
{
  "id": "example-lift-installation",
  "resort_id": "whiteface-mountain",
  "event_type": "lift_installation",
  "date": "1978",
  "description": "Lift installation event pending source confirmation.",
  "source_ids": [],
  "confidence_score": 60
}
```

Supported event types:

```text
opening
closure
reopening
expansion
lift_installation
lift_removal
ownership_change
operator_change
snowmaking_expansion
base_area_change
redevelopment
demolition
```

## Oral History

```json
{
  "id": "example-oral-history",
  "interviewee": null,
  "role": null,
  "resort_ids": [],
  "interview_date": null,
  "recording_url": null,
  "transcript_url": null,
  "rights_status": "pending review",
  "related_asset_ids": []
}
```

## Geographic Layer

```json
{
  "id": "whiteface-boundary-1978",
  "resort_id": "whiteface-mountain",
  "layer_type": "historical_boundary",
  "effective_date": "1978",
  "geometry_format": "geojson",
  "geometry_source": null,
  "source_asset_id": null,
  "confidence_score": 60
}
```

Supported layer types:

```text
historical_boundary
lift_alignment
trail_geometry
base_area
parking_area
expansion_area
lost_terrain
```

## Coverage Status Fields

Each resort record may include:

```json
{
  "coverage": {
    "trail_maps": "partial",
    "aerial_imagery": "missing",
    "lift_history": "missing",
    "ownership_history": "partial",
    "oral_histories": "missing",
    "gis_ready": false
  }
}
```

## Confidence Scoring

```text
95-100 Official primary source with clear date and provenance
85-94  Official map, brochure, or institutional archive item
70-84  Newspaper, secondary archive, or well-supported historical reference
55-69  Community contribution or unsourced collector scan requiring review
0-54   Placeholder or research lead only
```

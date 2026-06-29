# Fantasy Shred Archive 2.0 Implementation Plan

## Objective

Move the ski-area historical archive from static JSON-backed pages toward a durable historical GIS and archive platform.

The v2 architecture supports:

- public resort archive
- museum and collection registry
- historical trail map archive
- aerial imagery archive
- historical snapshot timelines
- lift and ownership history
- oral histories
- GIS-ready resort evolution layers
- future personal ski and snowboard history integration

## System Shape

```text
PostgreSQL + PostGIS
        ↓
FastAPI Archive API
        ↓
Public Gallery + Map Explorer
        ↓
Admin Research Portal
        ↓
AI Metadata / OCR / GIS Extraction
```

## Phase 1: Data Foundation

Status: started.

Deliverables:

- PostGIS schema
- SQLAlchemy models
- API endpoints
- seed script from existing archive JSON
- source registry
- schema documentation

Primary entities:

```text
Institution
Collection
Resort
HistoricalAsset
HistoricalSnapshot
LifecycleEvent
GeographicLayer
OralHistory
```

## Phase 2: API-Backed Public Archive

Deliverables:

- expose `/api/resorts`
- expose `/api/assets`
- expose `/api/snapshots`
- convert gallery cards to API-backed data
- preserve static fallback while API deployment is tested

## Phase 3: Historical Snapshot Viewer

Deliverables:

- year-based resort pages
- map/aerial/photo groupings by year
- confidence score display
- evidence provenance display
- side-by-side historical comparison foundation

## Phase 4: Admin Research Portal

Deliverables:

- source intake queue
- asset review workflow
- rights/provenance fields
- confidence scoring
- research gap tracker
- institution/contact tracking

## Phase 5: GIS Layer

Deliverables:

- PostGIS geometry storage
- resort historical boundaries
- lift alignments
- trail geometries
- lost terrain polygons
- base area and parking expansion layers
- Leaflet or MapLibre viewer

## Phase 6: AI-Assisted Enrichment

Deliverables:

- trail map OCR
- lift/trail name extraction
- map date detection
- source classification
- candidate GIS feature extraction
- human review before publication

## Phase 7: Personal History Integration

Deliverables:

- user ski/board day logbook
- resort visit history
- pass import support
- weather enrichment
- lifetime stats
- personal map overlays

## Current Priority Order

1. Stabilize PostGIS schema.
2. Seed existing archive records into v2.
3. Build API-backed public resort list.
4. Build historical snapshot page.
5. Build collection and institution browsing.
6. Add admin intake queue.
7. Add GIS viewer.

## Non-Negotiable Design Principles

- Preserve source provenance.
- Never overwrite uncertain history with false precision.
- Track confidence scores for historical claims.
- Separate original sources from interpreted facts.
- Keep static publication possible as a fallback.
- Treat maps and aerials as evidence, not decoration.

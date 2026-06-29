# Ski Area Historical Archive

A long-term historical archive and research platform focused on ski areas over the past 100+ years.

## Version 2.0 Status

Version 2.0 has begun.

The repository now contains an additive application scaffold for:

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

The existing static gallery remains in place while the v2 API and database are introduced safely.

## Current Focus

The archive is now organized around historical evidence rather than simple resort profiles.

The core model is evolving toward:

```text
Institution
    ↓
Collection
    ↓
Historical Asset
    ↓
Historical Snapshot
    ↓
Resort
```

This supports museums, university archives, private collections, trail maps, aerial imagery, lift history, oral histories, and year-specific resort snapshots.

## Local v2 Run

```bash
docker compose up
```

Then seed existing JSON records:

```bash
docker compose exec api python scripts/seed_v2_from_json.py
```

API documentation will be available at:

```text
http://localhost:8000/docs
```

See:

- `docs/v2-runbook.md`
- `docs/v2-implementation-plan.md`
- `docs/archive-schema-v2.md`
- `db/schema_v2.sql`

## Goals

- Collect historical ski area information
- Preserve trail maps, lift history, mountain statistics, photos, brochures, oral histories, and aerial imagery
- Track ski-area evolution over time
- Build searchable historical timelines and historical snapshot views
- Generate browser-based galleries and map comparisons
- Support AI-assisted metadata enrichment, OCR extraction, and future GIS feature extraction

## Architecture

```text
Collectors / Agents
    ↓
Normalized JSON + Archive Database
    ↓
Institutions / Collections / Assets
    ↓
Historical Snapshots
    ↓
Metadata Enrichment
    ↓
FastAPI + Gallery Generator / Public Frontend
    ↓
Forge / GitHub Pages / Cloudflare Pages / Static Output
```

## Planned Data Categories

- Ski area metadata
- Institutions and archival collections
- Trail maps by year
- Historical aerial imagery
- Lift installation and removal timelines
- Ownership and operator history
- Vertical drop evolution
- Skiable acreage evolution
- Historical boundary and expansion areas
- Historical ticket pricing
- Snowmaking expansion
- Photo archives
- Oral histories and transcripts
- Defunct/lost ski areas
- Historical brochures/postcards
- Source provenance and rights status

## Source Tiers

### Tier 1: Primary ski-area evidence

- Trail maps
- Historical aerial imagery
- Official resort brochures
- Official resort timelines
- Lift installation records

### Tier 2: Archival institutions and collections

- Ski museums
- University archives
- Local historical societies
- State digital archives
- County and tourism archives
- Digital Public Library collections

### Tier 3: Community and secondary research

- NELSAP and other lost-area research
- Collector submissions
- Newspaper references
- Ski-history articles
- Former employee and local historian interviews

## Seed Sources

- Skimap.org
- NewEnglandSkiHistory.com
- NELSAP
- OpenSkiMap
- New England Ski Museum
- Vermont Ski and Snowboard Museum
- Maine Ski and Snowboard Museum
- University of Utah Ski Archives
- Historical newspapers
- State tourism archives
- Local historical societies
- Digital Public Library of America
- Internet Archive

## Active Refinements Added

- Institution and collection support
- Historical snapshot schema
- Source provenance fields
- Oral history support
- Lifecycle events for openings, closures, lift changes, expansions, and ownership changes
- Gallery navigation for collections, museums, trail maps, lost areas, and timelines
- Coverage tracking for trail maps, aerial imagery, lift history, ownership, oral histories, and GIS readiness
- FastAPI v2 archive endpoints
- PostGIS-ready schema
- JSON-to-database seed script
- Docker Compose development stack

## Roadmap

### Phase 1

- Repository structure
- JSON schema
- Seed ski areas
- Static gallery prototype
- Weekly refinement workflow

### Phase 2

- Institution and collection registry
- Historical snapshot model
- Source provenance metadata
- Museum and archive partner tracking
- API-backed public archive

### Phase 3

- OCR trail map extraction
- GIS overlays
- Temporal comparisons
- Lift alignment and trail geometry extraction
- AI-assisted tagging

### Phase 4

- Semantic search
- Vector similarity for maps/images
- Public contribution workflows
- Expanded geospatial visualizations
- Historical map and aerial comparison viewer

### Phase 5

- Personal ski and snowboard history integration
- Pass import workflows
- Weather enrichment
- Lifetime skier/rider analytics

# Ski Area Historical Archive

A long-term historical archive and research platform focused on ski areas over the past 100+ years.

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

## Goals

- Collect historical ski area information
- Preserve trail maps, lift history, mountain statistics, photos, brochures, oral histories, and aerial imagery
- Track ski-area evolution over time
- Build searchable historical timelines and historical snapshot views
- Generate browser-based galleries and map comparisons
- Support AI-assisted metadata enrichment, OCR extraction, and future GIS feature extraction

## Initial Architecture

```text
Collectors / Agents
    ↓
Normalized JSON + SQLite
    ↓
Institutions / Collections / Assets
    ↓
Historical Snapshots
    ↓
Metadata Enrichment
    ↓
Static Gallery Generator
    ↓
GitHub Pages / Cloudflare Pages / Forge-hosted static output
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

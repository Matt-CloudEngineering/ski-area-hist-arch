# Ski Area Historical Archive

A long-term historical archive and research platform focused on ski areas over the past 100+ years.

## Goals

- Collect historical ski area information
- Preserve trail maps, lift history, mountain statistics, and photos
- Track ski-area evolution over time
- Build searchable historical timelines
- Generate browser-based galleries and map comparisons
- Support AI-assisted metadata enrichment and OCR extraction

## Initial Architecture

```text
Collectors / Agents
    ↓
Normalized JSON + SQLite
    ↓
Metadata Enrichment
    ↓
Static Gallery Generator
    ↓
GitHub Pages / Cloudflare Pages
```

## Planned Data Categories

- Ski area metadata
- Trail maps by year
- Lift installation timelines
- Ownership history
- Vertical drop evolution
- Skiable acreage evolution
- Historical ticket pricing
- Snowmaking expansion
- Photo archives
- Defunct/lost ski areas
- Historical brochures/postcards

## Initial Seed Sources

- Skimap.org
- NewEnglandSkiHistory.com
- NELSAP
- OpenSkiMap
- Historical newspapers
- State tourism archives
- University archives

## Roadmap

### Phase 1
- Repository structure
- JSON schema
- Seed ski areas
- Static gallery prototype
- Weekly refinement workflow

### Phase 2
- OCR trail map extraction
- GIS overlays
- Temporal comparisons
- AI-assisted tagging

### Phase 3
- Semantic search
- Vector similarity for maps/images
- Public contribution workflows
- Expanded geospatial visualizations

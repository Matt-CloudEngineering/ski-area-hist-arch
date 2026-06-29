# Version 2.0 Runbook

## Local Development

Start PostGIS and the API:

```bash
docker compose up
```

The API will be available at:

```text
http://localhost:8000
```

Interactive API documentation:

```text
http://localhost:8000/docs
```

Health check:

```bash
curl http://localhost:8000/health
```

## Seed Existing Archive JSON

After the containers are running:

```bash
docker compose exec api python scripts/seed_v2_from_json.py
```

This imports existing files from:

```text
archive/areas/*.json
```

into the v2 database tables.

## Current API Endpoints

```text
GET /health
GET /resorts
GET /resorts/{resort_id}
GET /resorts/{resort_id}/snapshots
GET /resorts/{resort_id}/assets
GET /institutions
GET /collections
GET /assets
GET /assets?asset_type=trail_map
```

## Deployment Notes

The current repository still contains the static gallery generator. The v2 API is additive and does not replace the existing gallery until the deployment path is confirmed.

Recommended production sequence:

1. Deploy PostGIS.
2. Deploy the FastAPI app behind `/api`.
3. Seed existing archive JSON.
4. Convert the static gallery to consume API output.
5. Add an admin research dashboard.
6. Add GIS viewer and historical map comparison tools.

## Safety Rule

Do not remove the existing static gallery until the v2 API, seed process, and public routing are confirmed in production.

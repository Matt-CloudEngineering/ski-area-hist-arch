CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS institutions (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  type TEXT,
  geographic_coverage JSONB,
  digital_access TEXT,
  contact_status TEXT,
  partnership_status TEXT
);

CREATE TABLE IF NOT EXISTS collections (
  id TEXT PRIMARY KEY,
  institution_id TEXT REFERENCES institutions(id),
  title TEXT NOT NULL,
  date_range TEXT,
  subject_coverage JSONB,
  access_restrictions TEXT,
  estimated_item_count INTEGER,
  digitization_status TEXT
);

CREATE TABLE IF NOT EXISTS resorts (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  state TEXT,
  country TEXT,
  status TEXT,
  summary TEXT,
  official_site JSONB,
  coordinates JSONB,
  coverage JSONB
);

CREATE TABLE IF NOT EXISTS historical_assets (
  id TEXT PRIMARY KEY,
  asset_type TEXT NOT NULL,
  title TEXT NOT NULL,
  resort_id TEXT REFERENCES resorts(id),
  collection_id TEXT REFERENCES collections(id),
  date_start TEXT,
  date_end TEXT,
  source_url TEXT,
  rights_status TEXT,
  provenance JSONB,
  confidence_score INTEGER CHECK (confidence_score BETWEEN 0 AND 100)
);

CREATE TABLE IF NOT EXISTS historical_snapshots (
  id TEXT PRIMARY KEY,
  resort_id TEXT NOT NULL REFERENCES resorts(id),
  year INTEGER NOT NULL,
  label TEXT,
  summary TEXT,
  metrics JSONB,
  asset_ids JSONB,
  confidence_score INTEGER CHECK (confidence_score BETWEEN 0 AND 100)
);

CREATE TABLE IF NOT EXISTS lifecycle_events (
  id TEXT PRIMARY KEY,
  resort_id TEXT NOT NULL REFERENCES resorts(id),
  event_type TEXT NOT NULL,
  event_date TEXT,
  description TEXT NOT NULL,
  source_ids JSONB,
  confidence_score INTEGER CHECK (confidence_score BETWEEN 0 AND 100)
);

CREATE TABLE IF NOT EXISTS geographic_layers (
  id TEXT PRIMARY KEY,
  resort_id TEXT REFERENCES resorts(id),
  layer_type TEXT NOT NULL,
  effective_date TEXT,
  geometry_format TEXT,
  geometry_source TEXT,
  source_asset_id TEXT REFERENCES historical_assets(id),
  confidence_score INTEGER CHECK (confidence_score BETWEEN 0 AND 100),
  geom GEOMETRY
);

CREATE TABLE IF NOT EXISTS oral_histories (
  id TEXT PRIMARY KEY,
  interviewee TEXT,
  role TEXT,
  resort_ids JSONB,
  interview_date DATE,
  recording_url TEXT,
  transcript_url TEXT,
  rights_status TEXT,
  related_asset_ids JSONB
);

CREATE INDEX IF NOT EXISTS idx_assets_resort_id ON historical_assets(resort_id);
CREATE INDEX IF NOT EXISTS idx_assets_type ON historical_assets(asset_type);
CREATE INDEX IF NOT EXISTS idx_snapshots_resort_year ON historical_snapshots(resort_id, year);
CREATE INDEX IF NOT EXISTS idx_lifecycle_resort_type ON lifecycle_events(resort_id, event_type);
CREATE INDEX IF NOT EXISTS idx_geographic_layers_resort_type ON geographic_layers(resort_id, layer_type);
CREATE INDEX IF NOT EXISTS idx_geographic_layers_geom ON geographic_layers USING GIST (geom);

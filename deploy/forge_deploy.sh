#!/usr/bin/env bash
set -euo pipefail

echo "Deploying Fantasy Shred"

cd /home/forge/fantasyshred.com

git pull origin main

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

python -m gallery_site.build_site
python -m landing.build_landing

rm -rf public/*
mkdir -p public/area-archives

cp -R landing/output/* public/
cp -R gallery_site/output/* public/area-archives/

echo "Deployment complete."

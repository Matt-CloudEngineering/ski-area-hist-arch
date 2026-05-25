#!/usr/bin/env bash
set -euo pipefail

echo "Deploying Ski Area Historical Archive"

cd /home/forge/fantasyshred.com

git pull origin main

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

python -m gallery_site.build_site

rm -rf public/*
cp -R gallery_site/output/* public/

echo "Deployment complete. Static site published to public/."

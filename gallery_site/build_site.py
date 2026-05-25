from pathlib import Path
import json
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parents[1]
AREAS = ROOT / 'archive' / 'areas'
OUTPUT = ROOT / 'gallery_site' / 'output'
TEMPLATES = ROOT / 'gallery_site' / 'templates'

OUTPUT.mkdir(parents=True, exist_ok=True)

areas = []
for path in AREAS.glob('*.json'):
    areas.append(json.loads(path.read_text()))

env = Environment(loader=FileSystemLoader(TEMPLATES))

template = env.get_template('index.html')
rendered = template.render(areas=areas)

(OUTPUT / 'index.html').write_text(rendered)

print('Generated gallery site')

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

areas = sorted(areas, key=lambda a: a.get('name', ''))

env = Environment(loader=FileSystemLoader(TEMPLATES))

index_template = env.get_template('index.html')
area_template = env.get_template('area.html')

index_rendered = index_template.render(areas=areas)
(OUTPUT / 'index.html').write_text(index_rendered)

for area in areas:
    rendered = area_template.render(area=area)
    (OUTPUT / f"{area['id']}.html").write_text(rendered)

print(f'Generated {len(areas)} archive pages')

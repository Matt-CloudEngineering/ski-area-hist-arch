from pathlib import Path
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'landing' / 'output'
TEMPLATES = ROOT / 'landing' / 'templates'

OUTPUT.mkdir(parents=True, exist_ok=True)

env = Environment(loader=FileSystemLoader(TEMPLATES))
template = env.get_template('index.html')

(OUTPUT / 'index.html').write_text(template.render())

print('Generated Fantasy Shred landing page')

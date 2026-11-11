"""Builds the Downloads page images from the Play Store screenshots (outside git, ../store-assets).
Run (needs Pillow): python3 tools/prepare_downloads.py
Writes assets/downloads/<app>/<lang>/<nn>-{300,480}.webp and content/downloads_captions.json (caption text = the Play screenshot's
title + subtitle, used as alt text). Sources stay untouched; rerun only when the Play screenshots change."""
import os, re, json
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, '..', 'store-assets')
APPS = {'server': 'dognas-server', 'client': 'dognas-client', 'lite': 'dognas-client-lite'}
LANGS = {'pt': 'pt-BR', 'en': 'en-US', 'es': 'es-ES'}
caps = {}
for app, repo in APPS.items():
    caps[app] = {}
    for L, loc in LANGS.items():
        d = os.path.join(STORE, repo, 'play-console', 'screenshots-2026-11-10', loc)
        items = []
        for i, f in enumerate(sorted(x for x in os.listdir(d) if x.endswith('.png')), 1):
            name = f[:-4]
            h = open(os.path.join(d, 'src', name + '.html'), encoding='utf-8').read()
            m = re.search(r'<h1>(.*?)</h1><p>(.*?)</p>', h)
            title = re.sub(r'<br>', ' ', re.sub(r'</?em>', '', m.group(1)))
            items.append({'n': f'{i:02d}', 'alt': f'{title}. {m.group(2)}'})
            out = os.path.join(ROOT, 'assets', 'downloads', app, L)
            os.makedirs(out, exist_ok=True)
            im = Image.open(os.path.join(d, f)).convert('RGB')
            for w in (300, 480):
                im.resize((w, round(w * im.height / im.width)), Image.LANCZOS).save(os.path.join(out, f'{i:02d}-{w}.webp'), 'WEBP', quality=80, method=6)
        caps[app][L] = items
json.dump(caps, open(os.path.join(ROOT, 'content', 'downloads_captions.json'), 'w'), ensure_ascii=False, indent=1)
print({a: len(v['pt']) for a, v in caps.items()})

# Two-device diagram (Downloads page): real captures, status bar and empty lower part cropped.
# client = Client explorer on the everyday phone (G100 raw); server = DogNAS server status screen (Play set).
RAW = {'pt': 'pt', 'en': 'en', 'es': 'es'}
for L, loc in LANGS.items():
    out = os.path.join(ROOT, 'assets', 'downloads', 'diagram', L)
    os.makedirs(out, exist_ok=True)
    c = Image.open(os.path.join(STORE, 'dognas-client', 'play-console', 'screenshots-2026-11-10', 'raw-g100', RAW[L], '03-photos.png')).convert('RGB')
    c = c.crop((0, 130, c.width, 1690))
    sv = Image.open(os.path.join(STORE, 'dognas-server', 'play-console', 'screenshots-2026-11-10', loc, 'src', 'status.png')).convert('RGB')
    sv = sv.crop((0, 110, sv.width, 1670))
    for name, im in (('client', c), ('server', sv)):
        for w in (300, 600):
            im.resize((w, round(w * im.height / im.width)), Image.LANCZOS).save(os.path.join(out, f'{name}-{w}.webp'), 'WEBP', quality=82, method=6)
print('diagram ok')


"""Responsive variants for PageSpeed: small icons and width variants of screenshots, photos and blog covers.
Run after adding/changing images: python3 tools/optimize_images.py (needs Pillow). Sources stay untouched; variants are
committed (the site is static). Names: icon-80/128/240.webp, icon-lite-128.webp, icon-96.png (favicon),
shots/<lang>/<name>-300|460.webp, photos/<name>-450.webp, blog/<group>/cover-<lang>-600|900.webp."""
import os, glob
from PIL import Image
A = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets')

def save(im, path, w, **kw):
    im = im.convert('RGBA' if im.mode in ('RGBA', 'LA', 'P') else 'RGB')
    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    im.save(path, **kw)

icon = Image.open(f'{A}/icon.png'); lite = Image.open(f'{A}/icon-lite.png')
for w in (80, 128, 240): save(icon, f'{A}/icon-{w}.webp', w, quality=85, method=6)
save(lite, f'{A}/icon-lite-128.webp', 128, quality=85, method=6)
save(icon, f'{A}/icon-96.png', 96, optimize=True)
n = 0
for f in glob.glob(f'{A}/shots/*/*.webp') + glob.glob(f'{A}/photos/*.webp') + glob.glob(f'{A}/blog/*/cover-*.webp'):
    stem = f[:-5]
    if stem.rsplit('-', 1)[-1].isdigit(): continue  # already a variant
    im = Image.open(f)
    widths = (300, 460) if '/shots/' in f else (450,) if '/photos/' in f else (600, 900)
    for w in widths:
        if w < im.width: save(im, f'{stem}-{w}.webp', w, quality=80, method=6); n += 1
print('ok', n, 'variants')

"""Cover for the 'google-storage-full' blog group from a real photo (phone server + USB hub + two-drive dock).

Source: ../store-assets/real-images (not in git). The crop stops left of the framed family photo, so no people appear;
the output has no EXIF. Needs Pillow. Run `python3 tools/optimize_images.py` afterwards for the -600/-900 variants.
"""
import os
from PIL import Image, ImageEnhance, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, '..', 'store-assets', 'real-images', '065464F3-2FB1-4412-95F2-7960355F180A.JPG')
OUT = os.path.join(ROOT, 'assets', 'blog', 'google-storage-full')

im = ImageOps.exif_transpose(Image.open(SRC)).convert('RGB')
w, h = im.size
x1 = int(w * .85)  # stops left of the framed photo
im = im.crop((0, int(h * .5), x1, int(h * .5) + round(x1 * 630 / 1200))).resize((1200, 630), Image.LANCZOS)
im = ImageEnhance.Color(ImageEnhance.Brightness(ImageOps.autocontrast(im, cutoff=.5)).enhance(1.08)).enhance(1.05)
os.makedirs(OUT, exist_ok=True)
for lang in ('pt', 'en', 'es'):
    im.save(os.path.join(OUT, f'cover-{lang}.webp'), quality=82)
    im.save(os.path.join(OUT, f'social-{lang}.jpg'), quality=86)

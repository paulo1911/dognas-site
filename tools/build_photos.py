"""Real-world photos for the landing page: crop, hide private details, light grade, WebP.

Sources are the originals in ../store-assets/real-images (not in git). Boxes are fractions
of the upright image so they survive re-exports at another resolution. The framed family
photo on the desk is blurred or cropped out: this is a public site. Output carries no EXIF.
Needs Pillow: python3 -m pip install pillow
"""
import os
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, '..', 'store-assets', 'real-images')
OUT = os.path.join(ROOT, 'assets', 'photos')
WIDTH = 900  # ~2x the widest slot on the page

# name: (source, crop box, [private boxes to blur], all as fractions of the upright image)
PHOTOS = {
    'always-on': ('6BFBDF00-1DD3-4C60-AE69-936D9861F94F.JPG', (0, .29, .726, .802), []),
    'usb-drive': ('AB2E3A51-6796-43B2-A2FA-A85828F3A349.JPG', (0, .075, 1, .917), [(.86, .24, 1.1, .51)]),
}

def frac(box, w, h): return tuple(int(v * (w if i % 2 == 0 else h)) for i, v in enumerate(box))

os.makedirs(OUT, exist_ok=True)
for name, (src, crop, private) in PHOTOS.items():
    im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, src))).convert('RGB')
    w, h = im.size
    if private:
        # Heavy blur plus darkening behind a feathered mask: reads as background, with no
        # hard edge, and no face stays recognizable.
        mask = Image.new('L', im.size, 0)
        for box in private:
            mask.paste(255, frac(box, w, h))
        mask = mask.filter(ImageFilter.GaussianBlur(w / 30))
        hidden = ImageEnhance.Brightness(im.filter(ImageFilter.GaussianBlur(w / 25))).enhance(.5)
        im = Image.composite(hidden, im, mask)
    im = im.crop(frac(crop, w, h))
    im = ImageOps.autocontrast(im, cutoff=.5)
    im = ImageEnhance.Brightness(im).enhance(1.08)
    im = ImageEnhance.Color(im).enhance(1.05)
    im = im.resize((WIDTH, round(im.height * WIDTH / im.width)), Image.LANCZOS)
    im.save(os.path.join(OUT, f'{name}.webp'), 'WEBP', quality=78, method=6)
    print(name, im.size, os.path.getsize(os.path.join(OUT, f'{name}.webp')) // 1024, 'KB')

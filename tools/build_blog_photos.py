"""EXPERIMENT (branch exp/blog-real-photos): real photos of the DogNAS setups for the blog, ready to validate.

Only the user's OWN photos from ../store-assets/real-images are used (never the three catalogue pictures of third-party
TV boxes there: Vivensis, Trendoca/Aquario, XSmart). Each photo is upright, cropped, lightly graded, stripped of EXIF
and written as WebP at 900 px (and 450 px). The framed family picture on the desk (it shows people) is blurred out in
the photos that include it. Output: assets/photos/blog/<name>(-450).webp and assets/photos/blog/preview.html to
review every image with its alt text in a browser before wiring any of them into an article.
Needs Pillow: python3 -m pip install pillow     Run: python3 tools/build_blog_photos.py
"""
import os
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, '..', 'store-assets', 'real-images')
OUT = os.path.join(ROOT, 'assets', 'photos', 'blog')
WIDTH = 900

# name: (source prefix, crop box, [private boxes to blur], alt text); boxes are fractions of the UPRIGHT image
PHOTOS = {
    's20fe-dark':   ('3A7B99D0', (.0, .20, 1, .86), [], 'A Samsung Galaxy S20 FE running DogNAS, standing on a desk with a blue backlight.'),
    's20fe-closeup': ('9A13259E', (.0, .0, 1, .90), [], 'Close-up of the DogNAS server dashboard on a Galaxy S20 FE: Wi-Fi, disk writing, CPU and memory cards.'),
    's20fe-side':   ('693C60F1', (.0, .20, 1, .86), [], 'The same Galaxy S20 FE seen from a lower angle, showing the Wi-Fi, disk, CPU and memory cards.'),
    'tv-box-g100':  ('4BA63DC1', (.0, .0, 1, 1), [], 'An Android TV box on a desk with a Moto G100 in front, connected to it with DogNAS Client Lite.'),
    'tv-launcher':  ('C72B8822', (.0, .08, 1, .92), [], 'The Android TV home screen with DogNAS among the favourite apps, on a TV box connected to a TV.'),
    'old-tablet':   ('87EB4681', (.0, .08, 1, .86), [], 'An old white 7-inch Android tablet used as a DogNAS server, next to a Wi-Fi router.'),
}
ALT_PT = {}


def frac(box, w, h):
    return tuple(int(v * (w if i % 2 == 0 else h)) for i, v in enumerate(box))


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for name, (prefix, crop, private, alt) in PHOTOS.items():
        f = next((x for x in sorted(os.listdir(SRC)) if x.startswith(prefix)), None)
        if not f:
            print('missing', prefix); continue
        im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, f))).convert('RGB')   # upright; the copy below has no EXIF
        w, h = im.size
        if private:
            mask = Image.new('L', im.size, 0)
            for box in private: mask.paste(255, frac(box, w, h))
            mask = mask.filter(ImageFilter.GaussianBlur(w / 30))
            hidden = ImageEnhance.Brightness(im.filter(ImageFilter.GaussianBlur(w / 25))).enhance(.5)
            im = Image.composite(hidden, im, mask)
        im = im.crop(frac(crop, w, h))
        im = ImageOps.autocontrast(im, cutoff=.5)
        im = ImageEnhance.Brightness(im).enhance(1.06)
        im = im.resize((WIDTH, round(im.height * WIDTH / im.width)), Image.LANCZOS)
        im.save(os.path.join(OUT, f'{name}.webp'), 'WEBP', quality=80, method=6)          # no exif= argument: nothing is written
        im.resize((450, round(im.height * 450 / im.width)), Image.LANCZOS).save(os.path.join(OUT, f'{name}-450.webp'), 'WEBP', quality=78, method=6)
        print(name, im.size, os.path.getsize(os.path.join(OUT, f'{name}.webp')) // 1024, 'KB')
        rows.append(f'<figure><img src="{name}-450.webp" srcset="{name}-450.webp 450w, {name}.webp 900w" sizes="300px" alt="{alt}" loading="lazy"><figcaption>{name}: {alt}</figcaption></figure>')
    open(os.path.join(OUT, 'preview.html'), 'w').write(
        '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Blog photos (validate)</title>'
        '<style>body{margin:0;background:#0a0a0a;color:#ddd;font:14px system-ui}.g{display:flex;flex-wrap:wrap;gap:16px;padding:16px}'
        'figure{margin:0;width:300px}img{width:100%;height:auto;border-radius:10px;display:block}figcaption{color:#9a9a9a;margin-top:6px}</style>'
        '<h2 style="margin:16px">Fotos reais para o blog (validar)</h2><div class="g">' + ''.join(rows) + '</div>')


if __name__ == '__main__':
    main()

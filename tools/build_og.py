"""Share images (og-<lang>.jpg, 1024x500): keeps the logo + phone art of the existing files and redraws the headline
block (left, below the logo). Idempotent: the text area is cleared before drawing. Needs Pillow.
Run: python3 tools/build_og.py. NOTE: written for the 1024x500 art; the committed files are now 1200x630 (LinkedIn/Facebook ratio, padded) — redraw from the 1024x500 originals in git history if you rerun it."""
import os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = ['/System/Library/Fonts/Supplemental/Arial Bold.ttf', '/Library/Fonts/Arial Bold.ttf', '/System/Library/Fonts/Helvetica.ttc']
REG = ['/System/Library/Fonts/Supplemental/Arial.ttf', '/Library/Fonts/Arial.ttf', '/System/Library/Fonts/Helvetica.ttc']
def font(paths, size):
    for p in paths:
        if os.path.exists(p): return ImageFont.truetype(p, size)
    raise SystemExit('no font found')
TEXT = {
 'pt': (['Seu celular antigo.', 'Seu armazenamento particular.'], 'Sem nuvem e sem mensalidade, pelo seu Wi-Fi.'),
 'en': (['Your old phone.', 'Your private storage.'], 'No cloud, no monthly fee, over your Wi-Fi.'),
 'es': (['Tu móvil viejo.', 'Tu almacenamiento privado.'], 'Sin nube y sin cuotas, por tu Wi-Fi.'),
}
for lang, (lines, sub) in TEXT.items():
    p = os.path.join(ROOT, f'assets/og-{lang}.jpg'); im = Image.open(p).convert('RGB'); d = ImageDraw.Draw(im)
    # clear the old text with a per-row horizontal gradient so the glow on the right is kept
    for y in range(235, 441):
        c0, c1 = im.getpixel((6, y)), im.getpixel((668, y))
        for x in range(0, 669):
            t = x / 668; im.putpixel((x, y), tuple(int(c0[k] + (c1[k] - c0[k]) * t) for k in range(3)))
    d = ImageDraw.Draw(im)
    f1, f2 = font(FONTS, 42), font(REG, 24)
    y = 250
    for l in lines: d.text((56, y), l, font=f1, fill=(245, 245, 245)); y += 52
    d.text((56, y + 12), sub, font=f2, fill=(170, 170, 175))
    d.rectangle([56, y + 62, 236, y + 66], fill=(255, 59, 48))
    im.save(p, quality=88)
print('ok')

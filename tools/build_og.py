"""Share images (og-<lang>.jpg, 1200x630 — the LinkedIn/Facebook ratio): keeps the logo + phone art of the committed files and
redraws the headline block (left, below the logo). The text area is cleared with a horizontal gradient before drawing; if a NEW headline is longer than the one already in the file, restore the file from git first (leftover pixels beyond the sample column would smear).
Needs Pillow. Run: python3 tools/build_og.py"""
import os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOLD = ['/System/Library/Fonts/Supplemental/Arial Bold.ttf', '/Library/Fonts/Arial Bold.ttf', '/System/Library/Fonts/Helvetica.ttc']
REG = ['/System/Library/Fonts/Supplemental/Arial.ttf', '/Library/Fonts/Arial.ttf', '/System/Library/Fonts/Helvetica.ttc']
def font(paths, size):
    for p in paths:
        if os.path.exists(p): return ImageFont.truetype(p, size)
    raise SystemExit('no font found')
TEXT = {
 'pt': (['Seu Android!', 'Seu armazenamento particular.'], 'Sem nuvem e sem mensalidade, pelo seu Wi-Fi.'),
 'en': (['Your Android!', 'Your private storage.'], 'No cloud, no monthly fee, over your Wi-Fi.'),
 'es': (['¡Tu Android!', 'Tu almacenamiento privado.'], 'Sin nube y sin cuotas, por tu Wi-Fi.'),
}
Y0, Y1, XR = 290, 560, 790   # text block area on the 1200x630 art (the phone starts at x≈820)
for lang, (lines, sub) in TEXT.items():
    p = os.path.join(ROOT, f'assets/og-{lang}.jpg'); im = Image.open(p).convert('RGB')
    assert im.size == (1200, 630), im.size
    for y in range(Y0, Y1):
        c0, c1 = im.getpixel((6, y)), im.getpixel((XR + 8, y))
        for x in range(0, XR + 1):
            t = x / XR; im.putpixel((x, y), tuple(int(c0[k] + (c1[k] - c0[k]) * t) for k in range(3)))
    d = ImageDraw.Draw(im); f1, f2 = font(BOLD, 47), font(REG, 28)
    y = 318
    for l in lines: d.text((66, y), l, font=f1, fill=(245, 245, 245)); y += 58
    d.text((66, y + 14), sub, font=f2, fill=(170, 170, 175))
    d.rectangle([66, y + 72, 278, y + 77], fill=(255, 59, 48))
    im.save(p, quality=88)
print('ok')

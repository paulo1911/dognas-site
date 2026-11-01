"""EXPERIMENT: alternative DogNAS-server images in a Galaxy S20 FE frame, in HD, for a carousel.

The screenshots come from the debug captures of the server (1080x2160, `store-assets/dognas-screenshots/g100/<lang>/`,
already stripped of the CPU/Memory cards by the store scripts). They are put in a neutral phone frame of the
S20 FE's proportions (20:9, punch-hole camera) and saved as WebP at 1x/2x so the existing `.carousel` markup of
the blog can show them. No real S20 FE capture is needed (the official server phone stays untouched).

Output: assets/s20fe/<lang>/<name>.webp (+ -540 variant) and assets/s20fe/preview.html (a stand-alone carousel
to review in a browser). Needs Pillow: python3 -m pip install pillow
Run: python3 tools/build_s20_carousel.py
"""
import os
from PIL import Image, ImageDraw, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = os.path.join(ROOT, '..', 'store-assets', 'dognas-screenshots', 'g100')
OUT = os.path.join(ROOT, 'assets', 's20fe')
NAMES = ['welcome', 'status', 'monitor', 'qr']
# 'performance' (debug write-buffer details) and 'upgrade' (captured on an older build, old plan table) are left out on purpose;
# add them back to NAMES after recapturing from the release build.
CAPTION = {
    'en': {'welcome': 'First run: three steps', 'status': 'Status: server online', 'monitor': 'Monitor: transfers in real time',
           'performance': 'Performance: Wi-Fi, disk, CPU', 'qr': 'Pair a phone with a QR Code', 'upgrade': 'DogNAS Pro'},
    'pt': {'welcome': 'Primeiro uso: três passos', 'status': 'Status: servidor online', 'monitor': 'Monitor: transferências em tempo real',
           'performance': 'Performance: Wi-Fi, disco, CPU', 'qr': 'Pareie um celular com QR Code', 'upgrade': 'DogNAS Pro'},
    'es': {'welcome': 'Primer uso: tres pasos', 'status': 'Estado: servidor en línea', 'monitor': 'Monitor: transferencias en tiempo real',
           'performance': 'Rendimiento: Wi-Fi, disco, CPU', 'qr': 'Empareja un móvil con un código QR', 'upgrade': 'DogNAS Pro'},
}
FRAME, BEZEL = (28, 28, 30), 26          # body colour, bezel in px at 1080 px of screen width
SCALE = 1.0


def redact(name: str, shot: Image.Image) -> Image.Image:
    """Public site: no LAN address, no pairing QR. Boxes are fractions of the 1080x2160 capture (see the
    debug captures of the server); the QR is blurred hard so it cannot be decoded, the address is painted over."""
    shot = shot.convert('RGB')
    w, h = shot.size
    if name == 'monitor':
        # "Home · 192.168.x.x" sits in the client row, which moves between languages: find the grey-blue text line
        # that starts at x=250 and is 300-340 px wide with the address after x=298 (second line of the client row),
        # i.e. the group of grey text rows right above the "N / 15 TCP sessions" line, and paint only the address.
        px = shot.load()
        def grey(x, y):
            r, g, b = px[x, y]
            return abs(r - 139) < 26 and abs(g - 156) < 26 and abs(b - 176) < 26
        rows = [y for y in range(1100, 1700) if sum(grey(x, y) for x in range(300, 470)) > 6]
        groups = []
        for y in rows:
            if groups and y - groups[-1][1] <= 3: groups[-1][1] = y
            else: groups.append([y, y])
        # Only the client row: its address line is the grey line whose "Home" label starts at x~196 AND that has a
        # bright-white client name ("OpenSSH") just above it; the subtitle / "TCP sessions" lines have no such name.
        def white(x, y):
            return min(px[x, y]) > 200
        for y0, y1 in groups:
            mid = (y0 + y1) // 2
            has_home = sum(grey(x, mid) for x in range(196, 270)) > 4
            has_name_above = any(sum(white(x, yy) for x in range(196, 340)) > 8 for yy in range(y0 - 60, y0 - 12, 3))
            # the client row has the green status dot at the far left (x 80-110) near its name; the header subtitle does not
            has_dot = any(px[x, yy][1] > 190 and px[x, yy][0] < 90 for x in range(80, 112, 2) for yy in range(y0 - 60, y0, 4))
            if y1 - y0 > 8 and has_home and has_name_above and has_dot:
                bg = px[1000, y0 - 6]
                ImageDraw.Draw(shot).rectangle((292, y0 - 5, 470, y1 + 5), fill=bg)
    if name == 'qr':
        box = (int(.20 * w), int(.60 * h), int(.80 * w), int(.91 * h))  # the white QR card is x .23-.77, y .63-.89
        region = shot.crop(box).filter(ImageFilter.GaussianBlur(34))
        shot.paste(region, box[:2])
    return shot


def framed(shot: Image.Image) -> Image.Image:
    w, h = shot.size
    pad = BEZEL
    body = Image.new('RGBA', (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(body)
    d.rounded_rectangle((0, 0, body.width - 1, body.height - 1), radius=118, fill=FRAME + (255,))
    # soft edge highlight, as on a real phone body
    d.rounded_rectangle((3, 3, body.width - 4, body.height - 4), radius=115, outline=(70, 70, 74, 255), width=3)
    mask = Image.new('L', (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), radius=92, fill=255)
    body.paste(shot.convert('RGB'), (pad, pad), mask)
    d = ImageDraw.Draw(body)
    cx, cy, r = body.width // 2, pad + 38, 17   # punch-hole front camera, top centre like the S20 FE
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(8, 8, 10, 255))
    # side keys (power + volume on the right edge)
    d.rounded_rectangle((body.width - 5, int(body.height * .27), body.width, int(body.height * .27) + 120), radius=3, fill=(60, 60, 64, 255))
    d.rounded_rectangle((body.width - 5, int(body.height * .37), body.width, int(body.height * .37) + 210), radius=3, fill=(60, 60, 64, 255))
    return body


def shadowed(phone: Image.Image) -> Image.Image:
    m = 70
    canvas = Image.new('RGBA', (phone.width + 2 * m, phone.height + 2 * m), (0, 0, 0, 0))
    sh = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((m, m + 30, m + phone.width, m + phone.height + 30), radius=118, fill=(0, 0, 0, 150))
    canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(34)))
    canvas.alpha_composite(phone, (m, m))
    return canvas


def main():
    html = ['<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
            '<title>S20 FE carousel (experiment)</title>',
            '<style>body{margin:0;background:#0a0a0a;color:#eee;font:15px system-ui}h2{margin:18px 16px 0}',
            '.track{display:flex;gap:18px;overflow-x:auto;scroll-snap-type:x mandatory;padding:16px}',
            'figure{margin:0;flex:0 0 auto;scroll-snap-align:center}img{height:520px;width:auto;display:block}',
            'figcaption{text-align:center;color:#aaa;margin-top:6px;font-size:13px;max-width:240px;margin-inline:auto}</style>']
    for lang in ('en', 'pt', 'es'):
        os.makedirs(os.path.join(OUT, lang), exist_ok=True)
        figs = []
        for n in NAMES:
            src = os.path.join(SHOTS, lang, f'{n}.png')
            if not os.path.exists(src):
                print('missing', src); continue
            ph = shadowed(framed(redact(n, Image.open(src))))
            hd = ph.copy()
            hd.save(os.path.join(OUT, lang, f'{n}.webp'), 'WEBP', quality=88, method=6)
            sm = ph.resize((540, round(ph.height * 540 / ph.width)), Image.LANCZOS)
            sm.save(os.path.join(OUT, lang, f'{n}-540.webp'), 'WEBP', quality=85, method=6)
            print(lang, n, hd.size, os.path.getsize(os.path.join(OUT, lang, f'{n}.webp')) // 1024, 'KB')
            figs.append(f'<figure><img src="{lang}/{n}-540.webp" srcset="{lang}/{n}-540.webp 540w, {lang}/{n}.webp {hd.width}w" '
                        f'sizes="260px" alt="{CAPTION[lang][n]}" loading="lazy"><figcaption>{CAPTION[lang][n]}</figcaption></figure>')
        html.append(f'<h2>{lang.upper()}</h2><div class="track">{"".join(figs)}</div>')
    open(os.path.join(OUT, 'preview.html'), 'w').write('\n'.join(html))


if __name__ == '__main__':
    main()

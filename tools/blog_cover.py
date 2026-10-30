"""Text-free blog covers v2: python3 tools/blog_cover.py [group ...] (default: all). Needs Pillow.
Each pillar has its own colour; each article a pictogram (drawn here, no embedded text) plus an app screenshot, so no two
covers look alike at card size. Writes assets/blog/<group>/cover-<lang>.webp (page, 1200x630) and social-<lang>.jpg (Open Graph).
After running, `python3 tools/optimize_images.py` makes the -600/-900 variants."""
import os, sys, re
from PIL import Image, ImageDraw, ImageFilter, ImageChops
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import blog_pillars as bp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PILLAR_COLOR = {'reuse': (229, 72, 59), 'storage': (31, 185, 138), 'sftp': (79, 140, 255), 'compare': (245, 165, 36)}
# group -> (pictogram, app screenshot)
COVERS = {'old-android-server': ('phone-wifi', 'server-status'), 'old-tablet': ('tablet', 'server-monitor'), 'old-laptop-hdd': ('disk', 'server-monitor'),
          'old-phone-ideas': ('phone-spark', 'lite-home'), 'free-phone-space': ('phone-out', 'lite-files'), 'cloud-subscription-savings': ('cloud-coin', 'server-status'),
          'pc-phone-transfer': ('pc-phone', 'lite-transfers'), 'sftp-explained': ('lock', 'server-qr'), 'sftp-clients': ('terminal', 'lite-files'),
          'nas-vs-android': ('versus', 'server-status'), 'home-nas': ('house', 'lite-files'), 'sell-or-reuse': ('recycle', 'lite-home')}
ICON_ALT = {  # cover_alt = pictogram + screen (the covers carry no text)
 'phone-wifi': dict(en='a phone with Wi-Fi', pt='um celular com Wi-Fi', es='un celular con Wi-Fi'), 'tablet': dict(en='a tablet with Wi-Fi', pt='um tablet com Wi-Fi', es='una tablet con Wi-Fi'),
 'disk': dict(en='a hard drive', pt='um HD', es='un disco duro'), 'phone-spark': dict(en='a phone with sparks of ideas', pt='um celular com faíscas de ideias', es='un celular con destellos de ideas'),
 'phone-out': dict(en='a phone with an arrow moving files out', pt='um celular com uma seta tirando arquivos', es='un celular con una flecha sacando archivos'),
 'cloud-coin': dict(en='a cloud with a coin', pt='uma nuvem com uma moeda', es='una nube con una moneda'), 'pc-phone': dict(en='a computer and a phone exchanging files', pt='um computador e um celular trocando arquivos', es='una computadora y un celular intercambiando archivos'),
 'lock': dict(en='a padlock', pt='um cadeado', es='un candado'), 'terminal': dict(en='a terminal window', pt='uma janela de terminal', es='una ventana de terminal'),
 'versus': dict(en='a NAS box facing a phone', pt='uma caixa de NAS diante de um celular', es='una caja de NAS frente a un celular'), 'house': dict(en='a house with a storage box', pt='uma casa com uma caixa de armazenamento', es='una casa con una caja de almacenamiento'),
 'recycle': dict(en='a phone with recycling arrows', pt='um celular com setas de reciclagem', es='un celular con flechas de reciclaje')}
SCREEN = {'server': dict(en='the DogNAS server screen', pt='a tela do servidor DogNAS', es='la pantalla del servidor DogNAS'), 'lite': dict(en='the DogNAS Client Lite screen', pt='a tela do DogNAS Client Lite', es='la pantalla del DogNAS Client Lite')}
JOIN = dict(en='Illustration of {i} next to {s}', pt='Ilustração de {i} ao lado d{s}', es='Ilustración de {i} junto a {s}')


def alt(group, lang):
    kind, shot = COVERS[group]; sc = SCREEN[shot.split('-')[0]][lang]
    return JOIN[lang].format(i=ICON_ALT[kind][lang], s=sc)


K = 4  # supersampling for the pictogram


def draw_icon(kind, color, size=300):
    S = size * K
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    w = 16 * K
    c = lambda v: int(v * K)
    def rr(x0, y0, x1, y1, r, fill=None, width=w): d.rounded_rectangle((c(x0), c(y0), c(x1), c(y1)), c(r), outline=color, width=width, fill=fill)
    def ln(pts, width=w): d.line([(c(x), c(y)) for x, y in pts], fill=color, width=width, joint='curve'); [d.ellipse((c(x) - width // 2, c(y) - width // 2, c(x) + width // 2, c(y) + width // 2), fill=color) for x, y in (pts[0], pts[-1])]
    def arc(cx, cy, r, a0, a1, width=w): d.arc((c(cx - r), c(cy - r), c(cx + r), c(cy + r)), a0, a1, fill=color, width=width)
    def dot(x, y, r): d.ellipse((c(x - r), c(y - r), c(x + r), c(y + r)), fill=color)
    def phone(x0=95, y0=30, x1=205, y1=270): rr(x0, y0, x1, y1, 24); ln([(135, 246), (165, 246)], 10 * K)
    def wifi(cx, cy):
        dot(cx, cy, 8)
        for r in (26, 50, 74): arc(cx, cy, r, 225, 315, 12 * K)
    if kind == 'phone-wifi': phone(); wifi(150, 175)
    elif kind == 'tablet': rr(25, 60, 275, 240, 22); dot(150, 215, 7); wifi(150, 165)
    elif kind == 'disk':
        rr(25, 70, 275, 230, 28); d.ellipse((c(70), c(100), c(170), c(200)), outline=color, width=w); dot(120, 150, 14); ln([(205, 130), (245, 130)], 12 * K); dot(238, 200, 9)
    elif kind == 'phone-spark':
        phone(70, 30, 180, 270)
        for x, y, r in ((228, 70, 30), (245, 170, 20), (215, 235, 14)): ln([(x - r, y), (x + r, y)], 12 * K); ln([(x, y - r), (x, y + r)], 12 * K)
    elif kind == 'phone-out': phone(); ln([(150, 190), (150, 80)]); ln([(112, 116), (150, 78), (188, 116)])
    elif kind == 'cloud-coin':
        m = Image.new('L', (S, S), 0); md = ImageDraw.Draw(m)  # cloud = union of circles + base, outlined by eroding the mask
        for cx, cy, r in ((95, 165, 50), (150, 120, 62), (215, 160, 55)): md.ellipse((c(cx - r), c(cy - r), c(cx + r), c(cy + r)), fill=255)
        md.rounded_rectangle((c(95), c(150), c(215), c(215)), c(30), fill=255); md.rectangle((c(95), c(165), c(215), c(215)), fill=255)
        inner = m.filter(ImageFilter.MinFilter(2 * (w // 2) + 1))
        ring = ImageChops.subtract(m, inner); im.paste(Image.new('RGBA', (S, S), color), (0, 0), ring)
        d.ellipse((c(185), c(185), c(280), c(280)), fill=(18, 18, 22, 255), outline=color, width=w); ln([(210, 232), (254, 232)], 12 * K)
    elif kind == 'pc-phone':
        rr(15, 50, 195, 185, 14); ln([(105, 185), (105, 225)]); ln([(65, 228), (145, 228)]); rr(205, 120, 280, 260, 16, width=12 * K); ln([(235, 105), (265, 105)], 1)
        ln([(215, 40), (270, 40)], 12 * K); ln([(250, 22), (272, 40), (250, 58)], 12 * K)
    elif kind == 'lock':
        rr(50, 125, 250, 270, 28); arc(150, 110, 62, 180, 360); ln([(88, 110), (88, 128)]); ln([(212, 110), (212, 128)]); dot(150, 190, 16); ln([(150, 195), (150, 232)], 12 * K)
    elif kind == 'terminal':
        rr(20, 40, 280, 260, 24); ln([(20, 95), (280, 95)], 12 * K); ln([(62, 140), (104, 172), (62, 204)]); ln([(130, 214), (200, 214)])
    elif kind == 'versus':
        rr(15, 70, 125, 240, 18); ln([(40, 110), (100, 110)], 10 * K); ln([(40, 150), (100, 150)], 10 * K); dot(70, 205, 9)
        rr(175, 70, 285, 240, 24); ln([(213, 215), (247, 215)], 10 * K); ln([(130, 155), (170, 155)], 12 * K)
    elif kind == 'house':
        ln([(25, 135), (150, 30), (275, 135)]); ln([(55, 120), (55, 265), (245, 265), (245, 120)])
        rr(105, 160, 195, 235, 14, width=12 * K); ln([(125, 188), (175, 188)], 9 * K); dot(125, 214, 6)
    elif kind == 'recycle':
        phone(105, 85, 195, 215); arc(150, 150, 120, 200, 320); ln([(250, 100), (262, 62), (222, 60)]) ; arc(150, 150, 120, 20, 140); ln([(50, 200), (38, 238), (78, 240)])
    return im.resize((size, size), Image.LANCZOS)


def cover(group, lang):
    pillar = bp.ASSIGN[group]; col = PILLAR_COLOR[pillar]; kind, shot = COVERS[group]
    W, H = 1200, 630
    bg = Image.new('RGB', (W, H), (10, 10, 12))
    glow = Image.new('RGB', (W, H), (0, 0, 0)); ImageDraw.Draw(glow).ellipse((-150, 220, 650, 900), fill=tuple(int(x * .42) for x in col))
    bg = ImageChops.add(bg, glow.filter(ImageFilter.GaussianBlur(110)))
    d = ImageDraw.Draw(bg)
    d.rounded_rectangle((120, 135, 520, 535), 64, fill=(18, 18, 22), outline=tuple(int(x * .75) for x in col), width=3)
    bg.paste(draw_icon(kind, col + (255,), 300), (170, 185), draw_icon(kind, col + (255,), 300))
    d.rounded_rectangle((0, 0, W, 10), 0, fill=col)  # pillar colour band
    s = Image.open(os.path.join(ROOT, 'assets', 'shots', lang, shot + '.webp')).convert('RGB')
    w = 380; s = s.resize((w, int(s.height * w / s.width)), Image.LANCZOS)
    m2 = Image.new('L', s.size, 0); ImageDraw.Draw(m2).rounded_rectangle((0, 0, s.width, s.height), 36, fill=255)
    bg.paste(s, (700, 60), m2)  # phone bleeds off the bottom edge on purpose
    return bg


if __name__ == '__main__':
    for group in sys.argv[1:] or COVERS:
        out = os.path.join(ROOT, 'assets', 'blog', group); os.makedirs(out, exist_ok=True)
        for lang in ('pt', 'en', 'es'):
            im = cover(group, lang)
            im.save(os.path.join(out, f'cover-{lang}.webp'), quality=82); im.save(os.path.join(out, f'social-{lang}.jpg'), quality=88)
    for group in sys.argv[1:] or COVERS:  # keep cover_alt truthful in the front matter
        for lang in ('pt', 'en', 'es'):
            f = os.path.join(ROOT, 'content', 'blog', group, lang + '.md'); t = open(f).read()
            open(f, 'w').write(re.sub(r'^cover_alt: .*$', 'cover_alt: ' + alt(group, lang), t, count=1, flags=re.M))
    print('ok')

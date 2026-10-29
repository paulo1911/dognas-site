"""Text-free blog cover from the app screenshots: python3 tools/blog_cover.py <group> <shot> (e.g. old-android-server server-status).
Writes assets/blog/<group>/cover-<lang>.webp (page, 1200x630) and social-<lang>.jpg (Open Graph). Needs Pillow."""
import os, sys
from PIL import Image, ImageDraw
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
group, shot = sys.argv[1], sys.argv[2]
out = os.path.join(ROOT, 'assets', 'blog', group); os.makedirs(out, exist_ok=True)
for lang in ('pt', 'en', 'es'):
    bg = Image.new('RGB', (1200, 630), (10, 10, 10))
    d = ImageDraw.Draw(bg)
    for i in range(630): d.line([(0, i), (1200, i)], fill=(10 + i // 30, 10, 10))  # faint red glow towards the bottom
    icon = Image.open(os.path.join(ROOT, 'assets', 'icon.png')).convert('RGBA').resize((300, 300))
    mask = Image.new('L', icon.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, 300, 300), 60, fill=255)
    bg.paste(icon, (170, 165), mask)
    s = Image.open(os.path.join(ROOT, 'assets', 'shots', lang, shot + '.webp')).convert('RGB')
    w = 380; s = s.resize((w, int(s.height * w / s.width)))
    m2 = Image.new('L', s.size, 0); ImageDraw.Draw(m2).rounded_rectangle((0, 0, s.width, s.height), 36, fill=255)
    bg.paste(s, (700, 60), m2)  # phone bleeds off the bottom edge on purpose
    bg.save(os.path.join(out, f'cover-{lang}.webp'), quality=82)
    bg.save(os.path.join(out, f'social-{lang}.jpg'), quality=88)
print('ok')

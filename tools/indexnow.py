"""Notify IndexNow search engines (Bing, Yandex, Seznam, Naver…; Google does not use it) that URLs changed.
Outward-facing: run only after a deploy is live, e.g. `python3 tools/indexnow.py` (all sitemap URLs). The key file
`<key>.txt` at the site root proves ownership (see build_seo.py)."""
import re, sys, json, os, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = 'dognas.app'
key = next(f[:-4] for f in os.listdir(ROOT) if re.fullmatch(r'[0-9a-f]{32}\.txt', f))
urls = re.findall(r'<loc>([^<]+)</loc>', open(os.path.join(ROOT, 'sitemap.xml')).read())
body = json.dumps({'host': HOST, 'key': key, 'keyLocation': f'https://{HOST}/{key}.txt', 'urlList': urls}).encode()
req = urllib.request.Request('https://api.indexnow.org/indexnow', body, {'Content-Type': 'application/json; charset=utf-8'})
print(urls, urllib.request.urlopen(req, timeout=30).status if '--send' in sys.argv else 'dry run (add --send)')

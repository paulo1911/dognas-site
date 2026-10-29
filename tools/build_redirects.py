"""Stub pages for URLs that moved when English became the default language (GitHub Pages has no 301s):
meta refresh + canonical to the new URL. Run LAST: python3 tools/build_redirects.py
Moves: /en/... -> /... (English is now the root) and the Portuguese blog articles /blog/<slug>/ -> /pt/blog/<slug>/.
Not redirectable: the old Portuguese /, /client/ and /blog/ (those URLs now serve English; hreflang points to /pt/...)."""
import os, shutil, html
import blog_content as bc
from build_home import ROOT
SITE = 'https://dognas.app/'
moves = {'en/': '', 'en/client/': 'client/', 'en/blog/': 'blog/'}
arts, _ = bc.load()
for a in arts:
    if a['lang'] == 'en': moves[f'en/blog/{a["slug"]}/'] = bc.article_path(a)
    if a['lang'] == 'pt': moves[f'blog/{a["slug"]}/'] = bc.article_path(a)
shutil.rmtree(os.path.join(ROOT, 'en'), ignore_errors=True)  # old English tree: every page is regenerated at the root or replaced by a stub
for old, new in moves.items():
    url = html.escape(SITE + new)
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>DogNAS</title>
<link rel="canonical" href="{url}"><meta http-equiv="refresh" content="0; url={url}">
<meta name="viewport" content="width=device-width, initial-scale=1"></head>
<body><p>This page moved to <a href="{url}">{url}</a>.</p></body></html>
'''
    out = os.path.join(ROOT, old, 'index.html'); os.makedirs(os.path.dirname(out), exist_ok=True); open(out, 'w').write(page)
print(f'ok: {len(moves)} redirect stubs')

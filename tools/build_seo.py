"""Crawler/agent files at the site root: robots.txt, sitemap.xml, llms.txt, llms-full.txt, agents.txt,
.well-known/security.txt, 404.html and the IndexNow key. Run: python3 tools/build_seo.py
Facts here must match the product and DECISIONS.md: no prices, no tested-device list, no unverified claims."""
import os, subprocess, datetime, hashlib
from build_home import ROOT, LANGS, EMAIL, GA_TAG, CSS_V, CSS_INLINE
SITE = 'https://dognas.app/'
def w(path, text):
    full = os.path.join(ROOT, path); os.makedirs(os.path.dirname(full), exist_ok=True); open(full, 'w').write(text)

# ---- robots.txt: everyone welcome, AI search/answer/training crawlers named explicitly -------------------------------
AI_BOTS = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'anthropic-ai',
           'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Applebot', 'Applebot-Extended', 'Bingbot', 'DuckAssistBot',
           'Meta-ExternalAgent', 'Amazonbot', 'CCBot', 'cohere-ai', 'MistralAI-User', 'YouBot']
robots = '# DogNAS — public marketing site: indexing by search engines and AI assistants is welcome.\n# Machine-readable summaries: /llms.txt, /llms-full.txt, /agents.txt\n\nUser-agent: *\nAllow: /\n\n'
robots += ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in AI_BOTS)
robots += f'Sitemap: {SITE}sitemap.xml\n'
w('robots.txt', robots)

# ---- sitemap.xml with hreflang alternates -------------------------------------------------------------------------
def lastmod(src):
    p = os.path.join('tools', src)
    try:
        dirty = subprocess.run(['git', 'diff', '--quiet', 'HEAD', '--', p], cwd=ROOT).returncode != 0
        d = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', p], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        return datetime.date.today().isoformat() if dirty or not d else d
    except Exception:
        return datetime.date.today().isoformat()
HREF = {'pt': 'pt-BR', 'en': 'en', 'es': 'es'}
groups = [(['', 'pt/', 'es/'], 'build_home.py', '1.0'), (['client/', 'pt/client/', 'es/client/'], 'build_client.py', '0.7')]
urls = []
for paths, src, prio in groups:
    for l, pth in zip(['en', 'pt', 'es'], paths):
        alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{HREF[a]}" href="{SITE}{ap}"/>' for a, ap in zip(['en', 'pt', 'es'], paths))
        alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{paths[0]}"/>'
        urls.append(f'<url><loc>{SITE}{pth}</loc><lastmod>{lastmod(src)}</lastmod><priority>{prio}</priority>{alts}</url>')
import blog_content as bc
barts, _ = bc.load()
def alt_links(items):
    items = dict(items)
    if len(items) < 2: return ''
    out = ''.join(f'<xhtml:link rel="alternate" hreflang="{HREF[l]}" href="{SITE}{p}"/>' for l, p in items.items())
    return out + f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{items.get("en", next(iter(items.values())))}"/>'
blive = [l for l in ['en', 'pt', 'es'] if any(a['lang'] == l for a in barts)]
bdate = max((a.get('updated') or a['created'] for a in barts), default='')
for l in blive:
    urls.append(f'<url><loc>{SITE}{bc.list_path(l)}</loc><lastmod>{max(a.get("updated") or a["created"] for a in barts if a["lang"] == l)}</lastmod><priority>0.6</priority>{alt_links({x: bc.list_path(x) for x in blive})}</url>')
for l in blive:
    urls.append(f'<url><loc>{SITE}{bc.about_path(l)}</loc><lastmod>{max(a.get("updated") or a["created"] for a in barts if a["lang"] == l)}</lastmod><priority>0.4</priority>{alt_links({x: bc.about_path(x) for x in blive})}</url>')
import blog_pillars as bp
for pid in bp.ORDER:
    sib = {l: bc.pillar_path(l, pid) for l in blive if any(a['lang'] == l and a['pillar'] == pid for a in barts)}
    for l, pth in sib.items():
        urls.append(f'<url><loc>{SITE}{pth}</loc><lastmod>{max(a.get("updated") or a["created"] for a in barts if a["lang"] == l and a["pillar"] == pid)}</lastmod><priority>0.5</priority>{alt_links(sib)}</url>')
for a in barts:
    sib = {x['lang']: bc.article_path(x) for x in barts if x['group'] == a['group']}
    urls.append(f'<url><loc>{SITE}{bc.article_path(a)}</loc><lastmod>{a.get("updated") or a["created"]}</lastmod><priority>0.6</priority>{alt_links(sib)}</url>')
urls.append(f'<url><loc>{SITE}privacy/</loc><lastmod>{lastmod("build_privacy.py")}</lastmod><priority>0.3</priority></url>')
w('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + '\n'.join(urls) + '\n</urlset>\n')

# ---- llms.txt (llmstxt.org format) and llms-full.txt --------------------------------------------------------------
NAME = {'pt': 'Português', 'en': 'English', 'es': 'Español'}
blog_llms = ('## Blog\n' + ''.join(f'- [Atom feed, {NAME[l]}]({SITE}{bc.blog_dir(l)}feed.xml)\n' for l in sorted({a['lang'] for a in barts})) + ''.join(f'- [{a["title"]}]({SITE}{bc.article_path(a)}) ({NAME[a["lang"]]}): {a["summary"]}\n' for a in sorted(barts, key=lambda a: (a['lang'], a['slug']))) + '\n') if barts else ''
llms = f'''# DogNAS

> DogNAS turns a compatible Android phone or tablet into a private file server (a small NAS) on your home Wi-Fi: keep and reach photos, videos and documents without the cloud and without a monthly fee. Other phones pair with a QR Code and a PIN; PCs and Macs connect over SFTP. Available in Portuguese (default), English and Spanish.

Key facts: the server app runs on Android 7.0 or newer; files stay in the storage you choose on the server device (internal memory, SD card or USB drive); access is encrypted (SFTP over SSH-2); the apps collect no personal data. DogNAS is not a backup: keep an independent copy of important files.

## Apps
- [DogNAS (server) on Google Play](https://play.google.com/store/apps/details?id=com.dognas.server): installs on the Android that will keep the files; free plan, optional one-time Pro purchase.
- [DogNAS Client Lite on Google Play](https://play.google.com/store/apps/details?id=com.dognas.client.lite): free, lightweight Android app to browse, upload and download files from a DogNAS.
- [DogNAS Client (Android and iPhone)]({SITE}client/): the full client app, coming soon.

## Site
- [Home (English)]({SITE}): what DogNAS is, how it works, plans, requirements.
- [Home (Português)]({SITE}pt/): same content in Portuguese.
- [Home (Español)]({SITE}es/): same content in Spanish.
- [Privacy policy]({SITE}privacy/): what the apps and this website collect (apps: nothing; website: analytics only after consent).

{blog_llms}## Optional
- [Full text for LLMs]({SITE}llms-full.txt): longer plain-text description of the product.
- [Sitemap]({SITE}sitemap.xml)
- [Agent access notes]({SITE}agents.txt)
'''
w('llms.txt', llms)
full = f'''# DogNAS — full description for language models

Canonical site: {SITE} · Contact: {EMAIL} · Languages: en (default), pt-BR, es.

## What it is
DogNAS is a file server for Android. It turns a compatible Android phone or tablet (for example one that is no longer used every day) into private storage on the home Wi-Fi network. It is not a cloud service: files are kept on the server device, in the storage the user chooses (internal memory, SD card, or a USB drive with a phone that supports USB OTG).

## How it works
1. Install the DogNAS server app on the Android that will keep the files, choose where to store them and tap Start.
2. Create a profile; the app shows a QR Code. Each profile has its own PIN and its own folders.
3. On another phone, scan the QR Code with a DogNAS client app (DogNAS Client Lite today) and type the PIN. Then browse, upload and download files over the home Wi-Fi.
4. PCs, Macs and scripts connect with any SFTP client (FileZilla, WinSCP, Cyberduck, rclone, OpenSSH) using the credentials of a paired device.

## Security and privacy
Connections use SFTP over SSH-2 (AES-GCM or ChaCha20); the server key is pinned when a device is paired and each device has its own revocable credential. The apps do not collect, send or sell personal data and contain no ads or third-party analytics. The website uses Google Analytics only after the visitor accepts the cookie notice. See {SITE}privacy/.

## Plans
- Free: DogNAS manages up to 64 GB, the Home profile plus 2 more, 3 paired devices. In the client app, transfers pause when you leave the client app (this is a client behavior; the server keeps running).
- Pro: one-time purchase, no subscription: the whole storage, unlimited profiles and devices, client-app transfers keep going with the app closed, the server can start by itself after a reboot, and maximum optimized performance.
- DogNAS Client Lite is always free. (Prices are shown in the store, not on this site.)

## Requirements and limits
- Android 7.0 or newer on the server and on the client phones, all on the same network.
- The server runs as a foreground service with a persistent notification and stays active with the screen off and the app closed; Android or the phone maker can still stop it to save battery, so check battery and permission settings.
- USB drives need USB OTG; spinning hard drives may need a powered USB hub.
- Each disk or DogNAS is an independent storage: DogNAS does not combine several drives into one volume.
- DogNAS is not a backup. A single disk can fail: keep an independent copy of important files.

## Apps
- DogNAS (server): https://play.google.com/store/apps/details?id=com.dognas.server
- DogNAS Client Lite (free, Android): https://play.google.com/store/apps/details?id=com.dognas.client.lite
- DogNAS Client (Android and iPhone): coming soon — {SITE}client/
'''
w('llms-full.txt', full)

# ---- agents.txt (emerging convention; no formal standard) --------------------------------------------------------------
w('agents.txt', f'''# agents.txt — DogNAS (emerging convention, not a formal standard)
# Public marketing site: AI agents and assistants may read, summarize and cite it.

Site: {SITE}
Contact: {EMAIL}
Languages: pt-BR, en, es
Allow: read, crawl, summarize, quote-with-attribution
Actions: none (no accounts, forms or purchases on this site; apps are installed from Google Play)
Preferred-Citation: DogNAS — {SITE}
Canonical-Sources: {SITE}llms.txt, {SITE}llms-full.txt, {SITE}sitemap.xml, {SITE}privacy/
Robots: {SITE}robots.txt
Notes: do not state prices or device compatibility as fact; point to the Google Play listings. DogNAS is not a backup solution.
''')

# ---- security.txt, 404.html, IndexNow key -------------------------------------------------------------------------------
exp = (datetime.date.today() + datetime.timedelta(days=365)).isoformat() + 'T00:00:00.000Z'
w('.well-known/security.txt', f'Contact: mailto:{EMAIL}\nExpires: {exp}\nPreferred-Languages: en, pt, es\nCanonical: {SITE}.well-known/security.txt\n')
w('404.html', f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
{GA_TAG}<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">
<title>DogNAS — 404</title><link rel="icon" type="image/png" href="/assets/icon-96.png">{CSS_INLINE}</head>
<body><div class="wrap"><header class="top"><a class="brand" href="/"><img src="/assets/icon-80.webp" alt="" width="36" height="36"><span>Dog<b>NAS</b></span></a></header>
<section class="hero"><h1>404</h1><p>Página não encontrada · Page not found · Página no encontrada</p><div class="cta"><a class="btn primary" href="/">DogNAS</a></div></section></div></body></html>
''')
key = hashlib.sha256(b'dognas.app-indexnow').hexdigest()[:32]
w(f'{key}.txt', key + '\n')
print('ok', key)

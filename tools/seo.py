"""Shared SEO helpers: canonical + hreflang + social meta and JSON-LD for the generated pages.
Everything here must stay true to the product (no ratings, prices or testimonials): see ../CLAUDE.md and the
workspace DECISIONS.md (communication strategy)."""
import html, json
SITE = 'https://dognas.app/'
LOCALES = {'pt': 'pt_BR', 'en': 'en_US', 'es': 'es_ES'}
HREFLANG = {'pt': 'pt-BR', 'en': 'en', 'es': 'es'}
PLAY_SERVER = 'https://play.google.com/store/apps/details?id=com.dognas.server'
PLAY_LITE = 'https://play.google.com/store/apps/details?id=com.dognas.client.lite'

def meta(lang, path, title, desc, alternates=None, og_type='website', noindex=False, image=None):
    """`path`: this page's path from the site root ('' = home); `alternates`: {lang: path} of translations."""
    t, d = html.escape(title), html.escape(desc)
    url = SITE + path
    img = SITE + (image or f'assets/og-{lang}.jpg')
    out = [
        f'<meta name="robots" content="{"noindex,follow" if noindex else "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"}">',
        '<meta name="theme-color" content="#0a0a0a">',
        f'<link rel="canonical" href="{url}">',
    ]
    for l, pth in (alternates or {}).items():
        out.append(f'<link rel="alternate" hreflang="{HREFLANG[l]}" href="{SITE + pth}">')
    if alternates:
        out.append(f'<link rel="alternate" hreflang="x-default" href="{SITE + alternates.get("pt", path)}">')
    out += [
        f'<meta property="og:type" content="{og_type}">', '<meta property="og:site_name" content="DogNAS">',
        f'<meta property="og:locale" content="{LOCALES[lang]}">',
    ] + [f'<meta property="og:locale:alternate" content="{LOCALES[l]}">' for l in (alternates or {}) if l != lang] + [
        f'<meta property="og:title" content="{t}">', f'<meta property="og:description" content="{d}">',
        f'<meta property="og:url" content="{url}">', f'<meta property="og:image" content="{img}">',
        '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{t}">',
        '<meta name="twitter:card" content="summary_large_image">', f'<meta name="twitter:title" content="{t}">',
        f'<meta name="twitter:description" content="{d}">', f'<meta name="twitter:image" content="{img}">',
    ]
    return '\n'.join(out) + '\n'

def ld(graph):
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':')) + '</script>\n'

ORG = {'@type': 'Organization', '@id': SITE + '#org', 'name': 'DogNAS', 'url': SITE, 'logo': SITE + 'assets/icon.png'}

def website(lang, home_path):
    return {'@type': 'WebSite', '@id': SITE + '#site', 'url': SITE, 'name': 'DogNAS', 'inLanguage': HREFLANG[lang], 'publisher': {'@id': SITE + '#org'}}

def app(name, desc, store_url, lang, os_='Android 7.0+', app_id=None):
    """SoftwareApplication. Free to install; no price, rating or review data on purpose (nothing verifiable to claim)."""
    a = {'@type': 'SoftwareApplication', 'name': name, 'description': desc, 'applicationCategory': 'UtilitiesApplication',
         'operatingSystem': os_, 'inLanguage': HREFLANG[lang], 'publisher': {'@id': SITE + '#org'},
         'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}}
    if app_id: a['@id'] = SITE + app_id
    if store_url: a['downloadUrl'] = store_url; a['installUrl'] = store_url
    return a

def webpage(lang, path, title, desc, breadcrumbs=None):
    g = {'@type': 'WebPage', '@id': SITE + path + '#page', 'url': SITE + path, 'name': title, 'description': desc,
         'inLanguage': HREFLANG[lang], 'isPartOf': {'@id': SITE + '#site'}}
    out = [g]
    if breadcrumbs:
        out.append({'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': i, 'name': n, 'item': SITE + p} for i, (n, p) in enumerate(breadcrumbs, 1)]})
    return out

def faq(items):
    """FAQPage from (question, answer) pairs; the same text is visible on the page."""
    return {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in items]}

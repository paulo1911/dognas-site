"""Blog pages: list (paginated) and articles at /blog/ (en, default), /pt/blog/, /es/blog/ from content/blog (see blog_content.py).
Run: python3 tools/build_blog.py            (published articles only; fails on any content error)
     python3 tools/build_blog.py --preview  (also drafts/review, written under _preview/, git-ignored)
Reuses the shell of the other generators. A language with no published article gets no blog pages."""
import os, sys, re, html, shutil
import seo, blog_content as bc, blog_about as ab, blog_pillars as bp
from build_home import inline_css, ROOT, GA_TAG, CSS_V, LANGS, NAMES, EMAIL, play, CLIENT_PLAY

BLOG_CSS = inline_css('style.css', 'blog.css')
PREVIEW = '--preview' in sys.argv
OUT = os.path.join(ROOT, '_preview') if PREVIEW else ROOT
UI = {
 'pt': dict(about='Conhecer o DogNAS', blog='Blog', h1='Blog DogNAS', lead='Guias práticos para usar seu Android como armazenamento particular, sem nuvem.', home='Início', toc='Neste artigo',
   related='Leia também', get='Baixar o DogNAS', updated='Atualizado em', min='min de leitura', newer='← Mais recentes', older='Mais antigos →', privacy='Privacidade', cookies='Cookies',
   cta_server=('Quero instalar no meu Android agora', 'Instale o DogNAS no Android que vai guardar seus arquivos. Grátis.'),
   cta_client=('Acessar meus arquivos', 'Instale o DogNAS Client Lite no aparelho que vai acessar o seu DogNAS. Grátis.'), draft='RASCUNHO — não publicado',
   cta_both='Instale o DogNAS no Android que vai guardar seus arquivos e o app de acesso nos aparelhos que vão usá-los. Os dois são grátis.',
   mid=dict(server='Tem um Android parado? Transforme-o no seu armazenamento particular em poucos minutos.', client='Precisa acessar seus arquivos de outro celular? Instale o app de acesso, é grátis.', both='Um Android guarda os arquivos e os outros aparelhos acessam. Comece grátis em poucos minutos.')),
 'en': dict(about='About DogNAS', blog='Blog', h1='DogNAS Blog', lead='Practical guides to use your Android as private storage, with no cloud.', home='Home', toc='In this article',
   related='Keep reading', get='Get DogNAS', updated='Updated', min='min read', newer='← Newer', older='Older →', privacy='Privacy', cookies='Cookies',
   cta_server=('Install on my Android now', 'Install DogNAS on the Android that will keep your files. Free.'),
   cta_client=('Access my files', 'Install DogNAS Client Lite on the device that will reach your DogNAS. Free.'), draft='DRAFT — not published',
   cta_both='Install DogNAS on the Android that will keep your files and the access app on the devices that will reach them. Both are free.',
   mid=dict(server='Have an old Android sitting idle? Turn it into your private storage in a few minutes.', client='Need to reach your files from another phone? Install the access app, it is free.', both='One Android keeps the files and your other devices reach them. Start free in a few minutes.')),
 'es': dict(about='Conocer DogNAS', blog='Blog', h1='Blog DogNAS', lead='Guías prácticas para usar tu Android como almacenamiento privado, sin nube.', home='Inicio', toc='En este artículo',
   related='Sigue leyendo', get='Descargar DogNAS', updated='Actualizado el', min='min de lectura', newer='← Más recientes', older='Más antiguos →', privacy='Privacidad', cookies='Cookies',
   cta_server=('Quiero instalarlo en mi Android ahora', 'Instala DogNAS en el Android que guardará tus archivos. Gratis.'),
   cta_client=('Acceder a mis archivos', 'Instala DogNAS Client Lite en el dispositivo que accederá a tu DogNAS. Gratis.'), draft='BORRADOR — no publicado',
   cta_both='Instala DogNAS en el Android que guardará tus archivos y la app de acceso en los dispositivos que los usarán. Las dos son gratis.',
   mid=dict(server='¿Tienes un Android parado? Conviértelo en tu almacenamiento privado en pocos minutos.', client='¿Necesitas acceder a tus archivos desde otro celular? Instala la app de acceso, es gratis.', both='Un Android guarda los archivos y tus otros dispositivos acceden. Empieza gratis en pocos minutos.')),
}


# Floating CTA: after ~40 % of the page, never over the cookie banner, hidden while an in-page CTA is on screen (no stacking).
STICKY_JS = """(function(){var f=document.querySelector('.float-cta');if(!f||!('IntersectionObserver' in window))return;var past=false,busy=0,tick=false;
function update(){f.hidden=!(past&&!busy&&!document.getElementById('dn-consent'));}
function onScroll(){tick=false;var h=document.documentElement;past=(window.scrollY+window.innerHeight)/h.scrollHeight>.4;update();}
window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(onScroll);}},{passive:true});onScroll();
var io=new IntersectionObserver(function(es){es.forEach(function(x){busy+=x.isIntersecting?1:-1;});busy=Math.max(0,busy);update();});
document.querySelectorAll('.post-cta,.mid-cta').forEach(function(n){io.observe(n);});
new MutationObserver(update).observe(document.body,{childList:true});})();"""


def store_url(app, loc):
    """Play link of the server or of the access app (the Client once CLIENT_PLAY is set, the Lite until then); `loc` = utm_campaign."""
    if app == 'client' and CLIENT_PLAY:
        return CLIENT_PLAY + ('&' if '?' in CLIENT_PLAY else '?') + 'referrer=utm_source%3Ddognas.app%26utm_medium%3Dwebsite%26utm_campaign%3D' + loc
    return play('server' if app == 'server' else 'lite', loc)


def cta_btn(a, app, pos, label, primary=True):
    """One CTA link. Positions: end (the box under the article; loc without suffix, as before), mid, sticky. Play campaign = loc."""
    loc = 'blog_' + a['group'] + ('' if pos == 'end' else '_' + pos)
    cid = loc + ('_' + app if pos == 'end' else '')
    return f'<a class="btn{" primary" if primary else ""}" href="{store_url(app, loc)}" rel="noopener" data-ev="blog_{app}_download_click" data-loc="{cid}">{label}</a>'


def write(path, text):
    full = os.path.join(OUT, path, 'index.html'); os.makedirs(os.path.dirname(full), exist_ok=True); open(full, 'w').write(text)


def shell(L, path, title, desc, main, base, nav, jsonld, alternates=None, og_type='website', noindex=False, image=None):
    t = UI[L]
    home = f'{base}{LANGS[L][1]}'
    return f'''<!doctype html>
<html lang="{LANGS[L][0]}">
<head>
<meta charset="utf-8">
{GA_TAG}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{seo.meta(L, path, title, desc, alternates, og_type, noindex or PREVIEW, image)}{jsonld}<link rel="alternate" type="application/atom+xml" title="{html.escape(t['h1'])}" href="{seo.SITE}{bc.blog_dir(L)}feed.xml"><link rel="icon" type="image/png" href="{base}assets/icon-96.png">
{BLOG_CSS}
</head>
<body><div class="wrap">
<header class="top"><a class="brand" href="{home}"><img src="{base}assets/icon-80.webp" alt="" width="36" height="36"><span>Dog<b>NAS</b></span></a><nav class="lang"><a class="btn primary hdr-cta" data-ev="blog_server_download_click" data-loc="blog_header" href="{play('server', 'blog_header')}" rel="noopener">{t['get']}</a>{nav}</nav></header>
{main}
<footer><span>© 2026 DogNAS</span><span><a href="{base}{bc.blog_dir(L)}">{t['blog']}</a> · <a href="{base}{bc.about_path(L)}">{ab.LABEL[L]['how']}</a> · <a href="{base}{bc.blog_dir(L)}feed.xml">RSS</a> · <a href="{base}privacy/#{L}">{t['privacy']}</a> · <a href="#" data-cookie-prefs>{t['cookies']}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span></footer>
</div></body></html>
'''


def atom(L, items):
    """Atom 1.0 feed of the language's published articles (newest first): title, link, dates, summary and category per entry.
    Summaries only: the feed is for discovery, the article page carries the CTA."""
    t, url = UI[L], seo.SITE + bc.blog_dir(L)
    stamp = lambda d: d + 'T00:00:00Z'
    updated = max((a.get('updated') or a['created'] for a in items))
    entries = ''.join(f'''<entry><title>{html.escape(a["title"])}</title><link href="{seo.SITE}{bc.article_path(a)}" rel="alternate" type="text/html"/><id>{seo.SITE}{bc.article_path(a)}</id><published>{stamp(a.get("published") or a["created"])}</published><updated>{stamp(a.get("updated") or a["created"])}</updated><summary type="text">{html.escape(a["summary"])}</summary><category term="{html.escape(a["category"])}"/></entry>
''' for a in items)
    return f'''<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xml:lang="{LANGS[L][0]}"><title>{html.escape(t["h1"])}</title><subtitle>{html.escape(t["lead"])}</subtitle><link href="{url}feed.xml" rel="self" type="application/atom+xml"/><link href="{url}" rel="alternate" type="text/html"/><id>{url}</id><updated>{stamp(updated)}</updated><author><name>DogNAS</name></author>
{entries}</feed>
'''


CHIPS = {'pt': ('Todos', 'Temas', 'Guias', 'guias'), 'en': ('All', 'Topics', 'Guides', 'guides'), 'es': ('Todos', 'Temas', 'Guías', 'guías')}


def cards_html(items, b, loc):
    """Article cards (list and hub pages); `loc` is the data-loc prefix, unique per page type."""
    return ''.join(f'<a class="post" href="{b}{bc.article_path(a)}" data-ev="blog_list_article_click" data-loc="{loc}_{a["group"]}">'
                   + (f'<img src="{b}{a["cover"]}" alt="{html.escape(a.get("cover_alt", ""))}" width="640" height="360" loading="lazy">' if a.get('cover') else '')
                   + f'<span class="cat">{html.escape(a["category"])}</span><h2>{html.escape(a["title"])}</h2><p>{html.escape(a["summary"])}</p></a>' for a in items)


def chips_html(L, b, current, pillars):
    """Plain links (work without JS, crawlable): All + one per pillar that has articles in this language."""
    t = CHIPS[L]
    one = lambda href, label, on, loc: f'<a href="{b}{href}"{" aria-current=page" if on else ""} data-ev="blog_pillar_click" data-loc="blog_chip_{loc}">{html.escape(label)}</a>'
    return f'<nav class="chips" aria-label="{t[1]}">' + one(bc.list_path(L), t[0], current is None, 'all') + ''.join(one(bc.pillar_path(L, pid), bp.PILLARS[pid][L]['name'], pid == current, pid) for pid in pillars) + '</nav>'


def fmt(date, L):
    import datetime
    d = datetime.date.fromisoformat(date)
    mon = {'pt': 'jan fev mar abr mai jun jul ago set out nov dez', 'en': 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec', 'es': 'ene feb mar abr may jun jul ago sep oct nov dic'}[L].split()
    return f'{d.day} {mon[d.month - 1]} {d.year}'


def main():
    arts, errors = bc.load(include_drafts=PREVIEW)
    if errors:
        print('\n'.join('ERROR ' + e for e in errors)); sys.exit(1)
    if PREVIEW:
        shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT); os.symlink(os.path.join(ROOT, 'assets'), os.path.join(OUT, 'assets'))
    by_lang = {l: sorted([a for a in arts if a['lang'] == l], key=lambda a: a.get('published') or a['created'], reverse=True) for l in LANGS}
    live = [l for l in LANGS if by_lang[l]]
    by_pillar = {(pid, l): [a for a in by_lang[l] if a['pillar'] == pid] for pid in bp.ORDER for l in LANGS}
    by_group = {(a['group'], a['lang']): a for a in arts}
    n = 0
    for L in live:
        if not PREVIEW:
            os.makedirs(os.path.join(OUT, bc.blog_dir(L)), exist_ok=True)
            open(os.path.join(OUT, bc.blog_dir(L), 'feed.xml'), 'w').write(atom(L, by_lang[L]))
        t, base = UI[L], '../' * (bc.blog_dir(L).count('/'))
        pillars = [pid for pid in bp.ORDER if by_pillar[(pid, L)]]
        # list pages
        pages = [by_lang[L][i:i + bc.PER_PAGE] for i in range(0, len(by_lang[L]), bc.PER_PAGE)]
        for p, chunk in enumerate(pages, 1):
            path = bc.list_path(L, p)
            b = '../' * path.count('/')
            nav = ''.join(f'<a href="{b}{bc.list_path(l)}"{" class=on" if l == L else ""}>{NAMES[l]}</a>' if l in live else
                          f'<a href="{b}{LANGS[l][1]}"{" class=on" if l == L else ""}>{NAMES[l]}</a>' for l in LANGS)
            cards = cards_html(chunk, b, 'blog_list')
            pager = ''
            if len(pages) > 1:
                prev = f'<a href="{b}{bc.list_path(L, p - 1)}">{t["newer"]}</a>' if p > 1 else ''
                nxt = f'<a href="{b}{bc.list_path(L, p + 1)}">{t["older"]}</a>' if p < len(pages) else ''
                pager = f'<nav class="pager">{prev}<span></span>{nxt}</nav>'
            title = t['h1'] + (f' — {p}' if p > 1 else '') + ' | DogNAS'
            alts = {l: bc.list_path(l) for l in live} if p == 1 else None
            blog_ld = {'@type': 'Blog', '@id': seo.SITE + bc.list_path(L) + '#blog', 'url': seo.SITE + bc.list_path(L), 'name': t['h1'], 'description': t['lead'], 'inLanguage': seo.HREFLANG[L],
                       'publisher': {'@id': seo.SITE + '#org'}, 'blogPost': [{'@id': seo.SITE + bc.article_path(x) + '#post'} for x in by_lang[L]]}
            ld = seo.ld([seo.ORG, seo.website(L, path)] + seo.webpage(L, path, title, t['lead'], [('DogNAS', LANGS[L][1]), (t['blog'], bc.list_path(L))]) + ([blog_ld] if p == 1 else []))
            main_html = f'<section class="blog-head"><h1>{t["h1"]}</h1><p>{t["lead"]}</p></section>{chips_html(L, b, None, pillars)}<div class="posts">{cards}</div>{pager}'
            write(path, shell(L, path, title, t['lead'], main_html, b, nav, ld, alts, noindex=p > 1))
            n += 1
        # trust page
        A, path = ab.PAGE[L], bc.about_path(L)
        b = '../' * path.count('/')
        body_html, _ = bc.render(A['body'], b, L)
        nav = ''.join(f'<a href="{b}{bc.about_path(l)}"{" class=on" if l == L else ""}>{NAMES[l]}</a>' if l in live else f'<a href="{b}{LANGS[l][1]}">{NAMES[l]}</a>' for l in LANGS)
        crumbs = f'<nav class="crumbs" aria-label="breadcrumb"><a href="{b}{LANGS[L][1]}">{t["home"]}</a> › <a href="{b}{bc.list_path(L)}">{t["blog"]}</a> › {ab.LABEL[L]["how"]}</nav>'
        ld = seo.ld([seo.ORG, seo.website(L, path)] + seo.webpage(L, path, A['title'] + ' | DogNAS', A['desc'], [('DogNAS', LANGS[L][1]), (t['blog'], bc.list_path(L)), (ab.LABEL[L]['how'], path)]))
        write(path, shell(L, path, A['title'] + ' | DogNAS', A['desc'], f'{crumbs}<article class="post-full"><header><h1>{html.escape(A["title"])}</h1></header><div class="prose">{body_html}</div></article>', b, nav, ld, {l: bc.about_path(l) for l in live}))
        n += 1
        # pillar hubs
        for pid in pillars:
            P, path = bp.PILLARS[pid][L], bc.pillar_path(L, pid)
            b = '../' * path.count('/')
            alts = {l: bc.pillar_path(l, pid) for l in live if by_pillar[(pid, l)]}
            nav = ''.join(f'<a href="{b}{alts[l]}"{" class=on" if l == L else ""}>{NAMES[l]}</a>' if l in alts else f'<a href="{b}{bc.list_path(l) if l in live else LANGS[l][1]}">{NAMES[l]}</a>' for l in LANGS)
            crumbs = f'<nav class="crumbs" aria-label="breadcrumb"><a href="{b}{LANGS[L][1]}">{t["home"]}</a> › <a href="{b}{bc.list_path(L)}">{t["blog"]}</a> › {html.escape(P["name"])}</nav>'
            intro = ''.join(f'<p>{html.escape(x)}</p>' for x in P['intro'])
            items = by_pillar[(pid, L)]
            ld = seo.ld([seo.ORG, seo.website(L, path)] + seo.webpage(L, path, P['title'], P['desc'], [('DogNAS', LANGS[L][1]), (t['blog'], bc.list_path(L)), (P['name'], path)])
                        + [{'@type': 'CollectionPage', '@id': seo.SITE + path + '#collection', 'url': seo.SITE + path, 'name': P['name'], 'description': P['desc'], 'inLanguage': seo.HREFLANG[L],
                            'isPartOf': {'@id': seo.SITE + bc.list_path(L) + '#blog'}, 'hasPart': [{'@id': seo.SITE + bc.article_path(x) + '#post'} for x in items]}])
            main_html = f'{crumbs}<section class="blog-head"><h1>{html.escape(P["name"])}</h1><div class="hub-intro">{intro}</div></section>{chips_html(L, b, pid, pillars)}<div class="posts">{cards_html(items, b, "blog_hub_" + pid)}</div>'
            write(path, shell(L, path, P['title'], P['desc'], main_html, b, nav, ld, alts if len(alts) > 1 else None))
            n += 1
        # articles
        for a in by_lang[L]:
            path = bc.article_path(a)
            b = '../' * path.count('/')
            html_body, toc = bc.render(a['body'], b, L)
            alts = {l: bc.article_path(by_group[(a['group'], l)]) for l in live if (a['group'], l) in by_group and by_group[(a['group'], l)].get('status') == 'published'}
            nav = ''.join(f'<a href="{b}{alts[l]}"{" class=on" if l == L else ""}>{NAMES[l]}</a>' if l in alts else
                          f'<a href="{b}{bc.list_path(l) if l in live else LANGS[l][1]}">{NAMES[l]}</a>' for l in LANGS)
            toc_html = (f'<nav class="toc" aria-label="{t["toc"]}"><strong>{t["toc"]}</strong><ul>' + ''.join(f'<li class="l{lv}"><a href="#{sid}">{html.escape(tx)}</a></li>' for lv, sid, tx in toc) + '</ul></nav>') if len(toc) >= 3 else ''
            kind = a['cta']  # server | client | both
            first = 'client' if kind == 'client' else 'server'
            label, sub = t['cta_' + (kind if kind != 'both' else 'server')]
            if kind == 'both': sub = t['cta_both']
            btns = cta_btn(a, first, 'end', label) + (' ' + cta_btn(a, 'client', 'end', t['cta_client'][0], False) if kind == 'both' else '')
            cta = f'<aside class="post-cta"><p>{sub}</p>{btns} <a class="more" href="{b}{LANGS[L][1]}" data-ev="blog_product_cta_click" data-loc="blog_{a["group"]}_product">{t["about"]}</a></aside>'
            # A short band before the middle section (after the reader has seen what the guide delivers), and a floating
            # button after ~40 % of the scroll (script below); each position has its own cta_id and Play campaign.
            heads = [m.start() for m in re.finditer(r'<h2 id=', html_body)]
            if len(heads) >= 4:
                mid = f'<aside class="cta-band mid-cta"><p>{t["mid"][kind]}</p>{cta_btn(a, first, "mid", label)}</aside>'
                html_body = html_body[:heads[len(heads) // 2]] + mid + html_body[heads[len(heads) // 2]:]
            sticky = f'<div class="float-cta" hidden>{cta_btn(a, first, "sticky", label)}</div>'
            rel = [by_group[(r, L)] for r in (a.get('related') or []) if (r, L) in by_group]
            rel_html = (f'<section class="related"><h2>{t["related"]}</h2><ul>' + ''.join(f'<li><a href="{b}{bc.article_path(r)}" data-ev="blog_related_article_click" data-loc="blog_{a["group"]}_related_{r["group"]}">{html.escape(r["title"])}</a></li>' for r in rel) + '</ul></section>') if rel else ''
            crumbs = f'<nav class="crumbs" aria-label="breadcrumb"><a href="{b}{LANGS[L][1]}">{t["home"]}</a> › <a href="{b}{bc.list_path(L)}">{t["blog"]}</a> › <a href="{b}{bc.pillar_path(L, a["pillar"])}">{html.escape(a["category"])}</a></nav>'
            cover = f'<figure class="cover"><img src="{b}{a["cover"]}" srcset="{b}{a["cover"][:-5]}-600.webp 600w, {b}{a["cover"][:-5]}-900.webp 900w, {b}{a["cover"]} 1200w" sizes="(max-width: 912px) calc(100vw - 32px), 880px" alt="{html.escape(a["cover_alt"])}" width="1200" height="630" fetchpriority="high"></figure>' if a.get('cover') else ''
            draft = f'<p class="draft-flag">{t["draft"]} ({a["status"]})</p>' if a['status'] != 'published' else ''
            upd = a.get('updated') or a['created']
            words = len(a['body'].split())
            tested = f'<p class="tested"><strong>{ab.LABEL[L]["tested"]}:</strong> {html.escape(a["tested"])}</p>' if a.get('tested') else ''
            main_html = f'''{crumbs}{draft}<article class="post-full"><header><a class="cat" href="{b}{bc.pillar_path(L, a["pillar"])}" data-ev="blog_pillar_click" data-loc="blog_article_{a["group"]}_pillar">{html.escape(a["category"])}</a><h1>{html.escape(a["title"])}</h1>
<p class="meta">{ab.LABEL[L]["by"]} <a href="{b}{bc.about_path(L)}" data-ev="blog_about_click" data-loc="blog_article_{a["group"]}_byline">{ab.TEAM[L]}</a> · {t["updated"]} {fmt(upd, L)} · {max(1, round(words / 200))} {t["min"]}</p>{tested}</header>{cover}{toc_html}<div class="prose">{html_body}</div>{cta}</article>{rel_html}{sticky}<script>(function(){{document.querySelectorAll('.carousel').forEach(function(c){{var t=c.querySelector('.track');[['prev','\u2039',-1],['next','\u203a',1]].forEach(function(b){{var x=document.createElement('button');x.type='button';x.className='nav '+b[0];x.textContent=b[1];x.setAttribute('aria-label',b[0]);x.onclick=function(){{t.scrollBy({{left:b[2]*t.clientWidth*.8,behavior:'smooth'}});}};c.appendChild(x);}});}});}})();</script><script>{STICKY_JS}</script><script>document.addEventListener('DOMContentLoaded',function(){{if(window.dnEvent)dnEvent('blog_article_view',{{article:'{a["group"]}',category:'{a["pillar"]}',cta:'{a["cta"]}',lang:'{L}'}});}});(function(){{var p=document.querySelector('.prose'),done=false,tick=false;if(!p)return;function chk(){{tick=false;if(done||!window.dnEvent)return;var r=p.getBoundingClientRect();if((innerHeight-r.top)/r.height>=.5){{done=true;dnEvent('blog_read_50',{{article:'{a["group"]}',category:'{a["pillar"]}',lang:'{L}'}});}}}}addEventListener('scroll',function(){{if(!tick){{tick=true;requestAnimationFrame(chk);}}}},{{passive:true}});}})();</script>'''
            image = a.get('social_image') or a.get('cover')
            ld = seo.ld([seo.ORG, seo.website(L, path)] + seo.webpage(L, path, a['meta_title'], a['meta_description'], [('DogNAS', LANGS[L][1]), (t['blog'], bc.list_path(L)), (a['category'], bc.pillar_path(L, a['pillar'])), (a['title'], path)])
                        + [{'@type': 'BlogPosting', '@id': seo.SITE + path + '#post', 'headline': a['title'], 'description': a['meta_description'], 'inLanguage': seo.HREFLANG[L],
                            'datePublished': a.get('published') or a['created'], 'dateModified': upd, 'mainEntityOfPage': seo.SITE + path,
                            'author': {'@type': 'Organization', 'name': ab.TEAM[L], 'url': seo.SITE + bc.about_path(L)}, 'publisher': {'@id': seo.SITE + '#org'}, 'isPartOf': {'@id': seo.SITE + bc.list_path(L) + '#blog'},
                            'wordCount': words, 'articleSection': a['category'], **({'keywords': ', '.join(a['tags'])} if a.get('tags') else {}),
                            **({'image': [seo.SITE + x for x in dict.fromkeys([a.get('cover'), a.get('social_image')]) if x]} if image else {})}])
            write(path, shell(L, path, a['meta_title'], a['meta_description'], main_html, b, nav, ld, alts if len(alts) > 1 else None, 'article', image=image))
            n += 1
    print(f'ok: {n} pages ({len(arts)} articles){" [preview -> _preview/]" if PREVIEW else ""}')


main()

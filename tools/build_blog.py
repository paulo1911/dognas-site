"""Blog pages: list (paginated) and articles at /blog/ (en, default), /pt/blog/, /es/blog/ from content/blog (see blog_content.py).
Run: python3 tools/build_blog.py            (published articles only; fails on any content error)
     python3 tools/build_blog.py --preview  (also drafts/review, written under _preview/, git-ignored)
Reuses the shell of the other generators. A language with no published article gets no blog pages."""
import os, sys, html, shutil
import seo, blog_content as bc
from build_home import inline_css, ROOT, GA_TAG, CSS_V, LANGS, NAMES, EMAIL, play

BLOG_CSS = inline_css('style.css', 'blog.css')
PREVIEW = '--preview' in sys.argv
OUT = os.path.join(ROOT, '_preview') if PREVIEW else ROOT
UI = {
 'pt': dict(about='Conhecer o DogNAS', blog='Blog', h1='Blog DogNAS', lead='Guias práticos para usar seu Android como armazenamento particular, sem nuvem.', home='Início', toc='Neste artigo',
   related='Leia também', get='Baixar o DogNAS', updated='Atualizado em', min='min de leitura', newer='← Mais recentes', older='Mais antigos →', privacy='Privacidade', cookies='Cookies',
   cta_server=('Quero instalar no meu Android agora', 'Instale o DogNAS no Android que vai guardar seus arquivos. Grátis.'),
   cta_client=('Acessar meus arquivos', 'Instale o DogNAS Client Lite no aparelho que vai acessar o seu DogNAS. Grátis.'), draft='RASCUNHO — não publicado'),
 'en': dict(about='About DogNAS', blog='Blog', h1='DogNAS Blog', lead='Practical guides to use your Android as private storage, with no cloud.', home='Home', toc='In this article',
   related='Keep reading', get='Get DogNAS', updated='Updated', min='min read', newer='← Newer', older='Older →', privacy='Privacy', cookies='Cookies',
   cta_server=('Install on my Android now', 'Install DogNAS on the Android that will keep your files. Free.'),
   cta_client=('Access my files', 'Install DogNAS Client Lite on the device that will reach your DogNAS. Free.'), draft='DRAFT — not published'),
 'es': dict(about='Conocer DogNAS', blog='Blog', h1='Blog DogNAS', lead='Guías prácticas para usar tu Android como almacenamiento privado, sin nube.', home='Inicio', toc='En este artículo',
   related='Sigue leyendo', get='Descargar DogNAS', updated='Actualizado el', min='min de lectura', newer='← Más recientes', older='Más antiguos →', privacy='Privacidad', cookies='Cookies',
   cta_server=('Quiero instalarlo en mi Android ahora', 'Instala DogNAS en el Android que guardará tus archivos. Gratis.'),
   cta_client=('Acceder a mis archivos', 'Instala DogNAS Client Lite en el dispositivo que accederá a tu DogNAS. Gratis.'), draft='BORRADOR — no publicado'),
}


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
{seo.meta(L, path, title, desc, alternates, og_type, noindex or PREVIEW, image)}{jsonld}<link rel="icon" type="image/png" href="{base}assets/icon-96.png">
{BLOG_CSS}
</head>
<body><div class="wrap">
<header class="top"><a class="brand" href="{home}"><img src="{base}assets/icon-80.webp" alt="" width="36" height="36"><span>Dog<b>NAS</b></span></a><nav class="lang"><a class="btn primary hdr-cta" data-ev="blog_server_download_click" data-loc="blog_header" href="{play('server', 'blog_header')}" rel="noopener">{t['get']}</a>{nav}</nav></header>
{main}
<footer><span>© 2026 DogNAS</span><span><a href="{base}{bc.blog_dir(L)}">{t['blog']}</a> · <a href="{base}privacy/#{L}">{t['privacy']}</a> · <a href="#" data-cookie-prefs>{t['cookies']}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span></footer>
</div></body></html>
'''


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
    by_group = {(a['group'], a['lang']): a for a in arts}
    n = 0
    for L in live:
        t, base = UI[L], '../' * (bc.blog_dir(L).count('/'))
        # list pages
        pages = [by_lang[L][i:i + bc.PER_PAGE] for i in range(0, len(by_lang[L]), bc.PER_PAGE)]
        for p, chunk in enumerate(pages, 1):
            path = bc.list_path(L, p)
            b = '../' * path.count('/')
            nav = ''.join(f'<a href="{b}{bc.list_path(l)}"{" class=on" if l == L else ""}>{NAMES[l]}</a>' if l in live else
                          f'<a href="{b}{LANGS[l][1]}"{" class=on" if l == L else ""}>{NAMES[l]}</a>' for l in LANGS)
            cards = ''.join(f'<a class="post" href="{b}{bc.article_path(a)}" data-ev="blog_list_article_click" data-loc="blog_list_{a["group"]}"><img src="{b}{a["cover"]}" alt="{html.escape(a.get("cover_alt", ""))}" width="640" height="360" loading="lazy"><span class="cat">{html.escape(a["category"])}</span><h2>{html.escape(a["title"])}</h2><p>{html.escape(a["summary"])}</p></a>'
                            if a.get('cover') else f'<a class="post" href="{b}{bc.article_path(a)}"><span class="cat">{html.escape(a["category"])}</span><h2>{html.escape(a["title"])}</h2><p>{html.escape(a["summary"])}</p></a>' for a in chunk)
            pager = ''
            if len(pages) > 1:
                prev = f'<a href="{b}{bc.list_path(L, p - 1)}">{t["newer"]}</a>' if p > 1 else ''
                nxt = f'<a href="{b}{bc.list_path(L, p + 1)}">{t["older"]}</a>' if p < len(pages) else ''
                pager = f'<nav class="pager">{prev}<span></span>{nxt}</nav>'
            title = t['h1'] + (f' — {p}' if p > 1 else '') + ' | DogNAS'
            alts = {l: bc.list_path(l) for l in live} if p == 1 else None
            ld = seo.ld([seo.ORG, seo.website(L, path)] + seo.webpage(L, path, title, t['lead'], [('DogNAS', LANGS[L][1]), (t['blog'], bc.list_path(L))]))
            main_html = f'<section class="blog-head"><h1>{t["h1"]}</h1><p>{t["lead"]}</p></section><div class="posts">{cards}</div>{pager}'
            write(path, shell(L, path, title, t['lead'], main_html, b, nav, ld, alts, noindex=p > 1))
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
            label, sub = t['cta_' + a['cta']]
            target = play('server' if a['cta'] == 'server' else 'lite', 'blog_' + a['group'])
            cta = f'<aside class="post-cta"><p>{sub}</p><a class="btn primary" href="{target}" rel="noopener" data-ev="blog_{a["cta"] if a["cta"] == "server" else "client"}_download_click" data-loc="blog_{a["group"]}_{a["cta"]}">{label}</a> <a class="more" href="{b}{LANGS[L][1]}" data-ev="blog_product_cta_click" data-loc="blog_{a["group"]}_product">{t["about"]}</a></aside>'
            rel = [by_group[(r, L)] for r in (a.get('related') or []) if (r, L) in by_group]
            rel_html = (f'<section class="related"><h2>{t["related"]}</h2><ul>' + ''.join(f'<li><a href="{b}{bc.article_path(r)}" data-ev="blog_related_article_click" data-loc="blog_{a["group"]}_related_{r["group"]}">{html.escape(r["title"])}</a></li>' for r in rel) + '</ul></section>') if rel else ''
            crumbs = f'<nav class="crumbs" aria-label="breadcrumb"><a href="{b}{LANGS[L][1]}">{t["home"]}</a> › <a href="{b}{bc.list_path(L)}">{t["blog"]}</a></nav>'
            cover = f'<figure class="cover"><img src="{b}{a["cover"]}" srcset="{b}{a["cover"][:-5]}-600.webp 600w, {b}{a["cover"][:-5]}-900.webp 900w, {b}{a["cover"]} 1200w" sizes="(max-width: 912px) calc(100vw - 32px), 880px" alt="{html.escape(a["cover_alt"])}" width="1200" height="630" fetchpriority="high"></figure>' if a.get('cover') else ''
            draft = f'<p class="draft-flag">{t["draft"]} ({a["status"]})</p>' if a['status'] != 'published' else ''
            upd = a.get('updated') or a['created']
            words = len(a['body'].split())
            main_html = f'''{crumbs}{draft}<article class="post-full"><header><span class="cat">{html.escape(a["category"])}</span><h1>{html.escape(a["title"])}</h1>
<p class="meta">{t["updated"]} {fmt(upd, L)} · {max(1, round(words / 200))} {t["min"]}</p></header>{cover}{toc_html}<div class="prose">{html_body}</div>{cta}</article>{rel_html}<script>(function(){{document.querySelectorAll('.carousel').forEach(function(c){{var t=c.querySelector('.track');[['prev','\u2039',-1],['next','\u203a',1]].forEach(function(b){{var x=document.createElement('button');x.type='button';x.className='nav '+b[0];x.textContent=b[1];x.setAttribute('aria-label',b[0]);x.onclick=function(){{t.scrollBy({{left:b[2]*t.clientWidth*.8,behavior:'smooth'}});}};c.appendChild(x);}});}});}})();</script><script>document.addEventListener('DOMContentLoaded',function(){{if(window.dnEvent)dnEvent('blog_article_view',{{article:'{a["group"]}',category:'{a["category"]}',cta:'{a["cta"]}',lang:'{L}'}});}});</script>'''
            image = a.get('social_image') or a.get('cover')
            ld = seo.ld([seo.ORG, seo.website(L, path)] + seo.webpage(L, path, a['meta_title'], a['meta_description'], [('DogNAS', LANGS[L][1]), (t['blog'], bc.list_path(L)), (a['title'], path)])
                        + [{'@type': 'BlogPosting', '@id': seo.SITE + path + '#post', 'headline': a['title'], 'description': a['meta_description'], 'inLanguage': seo.HREFLANG[L],
                            'datePublished': a.get('published') or a['created'], 'dateModified': upd, 'mainEntityOfPage': seo.SITE + path,
                            'author': {'@id': seo.SITE + '#org'}, 'publisher': {'@id': seo.SITE + '#org'}, **({'image': seo.SITE + image} if image else {})}])
            write(path, shell(L, path, a['meta_title'], a['meta_description'], main_html, b, nav, ld, alts if len(alts) > 1 else None, 'article', image=image))
            n += 1
    print(f'ok: {n} pages ({len(arts)} articles){" [preview -> _preview/]" if PREVIEW else ""}')


main()

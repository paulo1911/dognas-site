"""Downloads page: one dedicated page for the three apps in install order (server, Client, Client Lite).
en at /downloads/, pt at /pt/downloads/, es at /es/downloads/. Run: python3 tools/build_downloads.py (after tools/prepare_downloads.py).
Each app: Play-style screenshot carousel (CSS scroll-snap), benefit bullets, one store CTA (A red button / B official badge, same
html[data-pv] experiment as the home). cta_id = dl_<app> (hero: dl_hero_server); B adds the `_b` suffix. NOINDEX stays on until the
owner approves the page and the Client on Play has the features shown (scan, templates)."""
import os, json, html
import seo
from build_home import CSS_INLINE, blog_link, blog_nav, ROOT, GA_TAG, PV_SCRIPT, LANGS, NAMES, EMAIL, icon, play, client_play, BADGE, TM_NOTE
NOINDEX = True
CAPS = json.load(open(os.path.join(ROOT, 'content', 'downloads_captions.json'), encoding='utf-8'))
T = {
 'pt': dict(title='Baixar o DogNAS — servidor e apps para Android', desc='Baixe o DogNAS: o servidor que transforma um Android em armazenamento privado na sua rede Wi-Fi e os apps DogNAS Client e Client Lite para acessar seus arquivos.',
   h1='Baixe os apps do DogNAS', lead='O DogNAS transforma um Android parado em armazenamento privado na sua rede Wi-Fi. São três apps: o servidor fica em casa e os apps de acesso abrem seus arquivos no celular. Comece pelo servidor.',
   steps=[('1', 'Servidor', 'No Android que fica em casa'), ('2', 'Client', 'No celular do dia a dia'), ('3', 'Client Lite', 'Versão leve, opcional')],
   trust='Sem conta, sem anúncios e sem nuvem. Os apps não coletam dados.',
   apps={
    'server': dict(name='DogNAS', tag='Passo 1 · O servidor', role='Instale no Android que vai ficar em casa: ele guarda seus arquivos e os outros celulares se conectam a ele.',
      bullets=['Seu Android parado vira o servidor de arquivos da casa', 'Conecte outros celulares por QR Code e PIN, sem criar conta', 'Guarde no aparelho, num cartão SD ou num HD USB', 'Perfis para cada pessoa da casa, cada um com seu PIN', 'Funciona também em tablet e TV box Android'],
      cta='Baixar o servidor', note='Android 7.0 ou superior. Comece no plano Grátis; o Pro é opcional (compra única, sem assinatura).'),
    'client': dict(name='DogNAS Client', tag='Passo 2 · O app de acesso', role='Instale no celular que vai usar seus arquivos. É o app completo para abrir, enviar e organizar o que está no seu DogNAS.',
      bullets=['Escaneie documentos com a câmera e salve direto no DogNAS', 'Veja fotos, vídeos, músicas e PDFs sem baixar antes', 'Navegue com miniaturas, busque, renomeie, mova e apague', 'Fila de envios com pausa e retomada se o Wi-Fi cair', 'Pastas prontas para começar: Casa, Trabalho e Mínimo'],
      cta='Baixar o Client', note='Precisa do servidor DogNAS (passo 1) na mesma rede Wi-Fi. Android 7.0 ou superior.'),
    'lite': dict(name='DogNAS Client Lite', tag='Passo 2 · Versão leve', role='O app de acesso mais simples e leve, bom para celulares mais antigos ou com pouco espaço.',
      bullets=['Leve e direto, feito para aparelhos Android mais simples', 'Pareie pelo QR Code e abra seus arquivos', 'Modelos de pasta prontos para começar', 'Veja quanto espaço o seu perfil já usa', 'Baixe os arquivos para o celular'],
      cta='Baixar o Client Lite', note='Precisa do servidor DogNAS (passo 1) na mesma rede Wi-Fi. Android 7.0 ou superior.')},
   cmp_h='Client ou Client Lite?', cmp='O Client é o app completo: escanear documentos, ver arquivos sem baixar e miniaturas. O Client Lite é mais leve e simples, para aparelhos antigos. Os dois abrem o mesmo servidor, e você pode instalar os dois.',
   car='Capturas de tela', prev='Anterior', next='Próxima', back='Voltar ao início', privacy='Política de privacidade'),
 'en': dict(title='Download DogNAS — server and apps for Android', desc='Download DogNAS: the server that turns an Android into private storage on your Wi-Fi, and the DogNAS Client and Client Lite apps to reach your files.',
   h1='Download the DogNAS apps', lead='DogNAS turns an idle Android into private storage on your Wi-Fi. There are three apps: the server stays at home and the access apps open your files on your phone. Start with the server.',
   steps=[('1', 'Server', 'On the Android that stays home'), ('2', 'Client', 'On your everyday phone'), ('3', 'Client Lite', 'Light version, optional')],
   trust='No account, no ads and no cloud. The apps collect no data.',
   apps={
    'server': dict(name='DogNAS', tag='Step 1 · The server', role='Install it on the Android that will stay at home: it keeps your files and the other phones connect to it.',
      bullets=['Your idle Android becomes the home file server', 'Connect other phones with a QR Code and PIN, no account', 'Store on the device, an SD card or a USB drive', 'Profiles for each person at home, each with its own PIN', 'Also works on an Android tablet or TV box'],
      cta='Download the server', note='Android 7.0 or newer. Start on the Free plan; Pro is optional (one-time purchase, no subscription).'),
    'client': dict(name='DogNAS Client', tag='Step 2 · The access app', role='Install it on the phone you will use your files from. It is the full app to open, send and organize what is on your DogNAS.',
      bullets=['Scan documents with the camera and save them straight to your DogNAS', 'View photos, videos, music and PDFs without downloading first', 'Browse with thumbnails, search, rename, move and delete', 'Transfer queue with pause and resume if the Wi-Fi drops', 'Ready-made folders to start: Home, Work and Minimal'],
      cta='Download the Client', note='Needs the DogNAS server (step 1) on the same Wi-Fi network. Android 7.0 or newer.'),
    'lite': dict(name='DogNAS Client Lite', tag='Step 2 · Light version', role='The simpler, lighter access app, good for older phones or phones with little space.',
      bullets=['Light and direct, made for simpler Android devices', 'Pair with the QR Code and open your files', 'Ready-made folder templates to start', 'See how much space your profile already uses', 'Download files to your phone'],
      cta='Download the Client Lite', note='Needs the DogNAS server (step 1) on the same Wi-Fi network. Android 7.0 or newer.')},
   cmp_h='Client or Client Lite?', cmp='The Client is the full app: scan documents, view files without downloading and thumbnails. The Client Lite is lighter and simpler, for older devices. Both open the same server, and you can install both.',
   car='Screenshots', prev='Previous', next='Next', back='Back to home', privacy='Privacy policy'),
 'es': dict(title='Descargar DogNAS — servidor y apps para Android', desc='Descarga DogNAS: el servidor que convierte un Android en almacenamiento privado en tu Wi-Fi y las apps DogNAS Client y Client Lite para acceder a tus archivos.',
   h1='Descarga las apps de DogNAS', lead='DogNAS convierte un Android parado en almacenamiento privado en tu Wi-Fi. Son tres apps: el servidor se queda en casa y las apps de acceso abren tus archivos en el móvil. Empieza por el servidor.',
   steps=[('1', 'Servidor', 'En el Android que se queda en casa'), ('2', 'Client', 'En tu móvil de todos los días'), ('3', 'Client Lite', 'Versión ligera, opcional')],
   trust='Sin cuenta, sin anuncios y sin nube. Las apps no recogen datos.',
   apps={
    'server': dict(name='DogNAS', tag='Paso 1 · El servidor', role='Instálalo en el Android que se quedará en casa: guarda tus archivos y los demás móviles se conectan a él.',
      bullets=['Tu Android parado se convierte en el servidor de archivos de casa', 'Conecta otros móviles con código QR y PIN, sin crear cuenta', 'Guarda en el dispositivo, en una tarjeta SD o en un disco USB', 'Perfiles para cada persona de casa, cada uno con su PIN', 'También funciona en una tablet o TV box Android'],
      cta='Descargar el servidor', note='Android 7.0 o superior. Empieza en el plan Gratis; el Pro es opcional (compra única, sin suscripción).'),
    'client': dict(name='DogNAS Client', tag='Paso 2 · La app de acceso', role='Instálala en el móvil desde el que usarás tus archivos. Es la app completa para abrir, enviar y organizar lo que hay en tu DogNAS.',
      bullets=['Escanea documentos con la cámara y guárdalos directo en tu DogNAS', 'Mira fotos, vídeos, música y PDF sin descargar antes', 'Navega con miniaturas, busca, renombra, mueve y borra', 'Cola de envíos con pausa y reanudación si el Wi-Fi se cae', 'Carpetas listas para empezar: Casa, Trabajo y Mínimo'],
      cta='Descargar el Client', note='Necesita el servidor DogNAS (paso 1) en la misma red Wi-Fi. Android 7.0 o superior.'),
    'lite': dict(name='DogNAS Client Lite', tag='Paso 2 · Versión ligera', role='La app de acceso más simple y ligera, buena para móviles más antiguos o con poco espacio.',
      bullets=['Ligera y directa, hecha para dispositivos Android más sencillos', 'Empareja con el código QR y abre tus archivos', 'Plantillas de carpetas listas para empezar', 'Mira cuánto espacio usa ya tu perfil', 'Descarga los archivos al móvil'],
      cta='Descargar el Client Lite', note='Necesita el servidor DogNAS (paso 1) en la misma red Wi-Fi. Android 7.0 o superior.')},
   cmp_h='¿Client o Client Lite?', cmp='El Client es la app completa: escanear documentos, ver archivos sin descargar y miniaturas. El Client Lite es más ligero y simple, para dispositivos antiguos. Los dos abren el mismo servidor y puedes instalar los dos.',
   car='Capturas de pantalla', prev='Anterior', next='Siguiente', back='Volver al inicio', privacy='Política de privacidad'),
}
ICON = {'server': 'server', 'client': 'phone-free', 'lite': 'devices'}
ANCHOR = {'server': 'servidor', 'client': 'client', 'lite': 'lite'}
def store(app, loc):
    return client_play(loc) if app == 'client' else play(app, loc)
def cta(app, loc, label, L, base):
    f, alt = BADGE[L]
    ev = f'{app}_store_click'
    a = f'<a class="btn primary pv-a" data-ev="{ev}" data-loc="{loc}" href="{store(app, loc)}" rel="noopener">{label}</a>'
    b = f'<a class="pv-b" data-ev="{ev}" data-loc="{loc}_b" href="{store(app, loc + "_b")}" rel="noopener"><img src="{base}assets/badges/{f}.png" alt="{alt}" width="168" height="65"></a>'
    return f'<div class="cta">{a}{b}</div>'
def carousel(app, L, base, t):
    figs = ''
    for i, c in enumerate(CAPS[app][L]):
        stem = f'{base}assets/downloads/{app}/{L}/{c["n"]}'
        lazy = 'loading=lazy' if i > 1 or app != 'server' else ''
        figs += f'<figure><img src="{stem}-480.webp" srcset="{stem}-300.webp 300w, {stem}-480.webp 480w" sizes="240px" alt="{html.escape(c["alt"])}" width="480" height="853" {lazy}></figure>'
    return f'<div class="dl-carwrap" data-app="{app}"><div class="dl-car" tabindex="0" role="region" aria-label="{t["car"]}: {html.escape(t["apps"][app]["name"])}">{figs}</div><button type="button" class="dl-nav prev" aria-label="{t["prev"]}">‹</button><button type="button" class="dl-nav next" aria-label="{t["next"]}">›</button></div>'
JS = '''<script>
(function () {
  var L = (document.documentElement.lang || 'pt').slice(0, 2);
  document.querySelectorAll('.dl-carwrap').forEach(function (w) {
    var c = w.querySelector('.dl-car'), sent = 0;
    function go(d) { c.scrollBy({left: d * (c.querySelector('figure').offsetWidth + 12), behavior: 'smooth'}); }
    w.querySelector('.prev').addEventListener('click', function () { go(-1); });
    w.querySelector('.next').addEventListener('click', function () { go(1); });
    // GA4-only engagement signal, once per carousel and page view (consent-gated like the other events).
    c.addEventListener('scroll', function () { if (!sent && c.scrollLeft > 40) { sent = 1; if (window.dnEvent) window.dnEvent('carousel_interact', {app: w.getAttribute('data-app'), lang: L}); } }, {passive: true});
  });
})();
</script>'''
for L, t in T.items():
    base = '../' if L == 'en' else '../../'
    home = f'{base}{LANGS[L][1]}'
    path = LANGS[L][1] + 'downloads/'
    nav = blog_nav(L, base, 'downloads') + ''.join(f'<a href="{base}{LANGS[l][1]}downloads/"{" class=on" if l == L else ""}>{NAMES[l]}</a>' for l in LANGS)
    steps = ''.join(f'<li><a href="#{ANCHOR[k]}"><b>{n}</b><span><strong>{nm}</strong>{d}</span></a></li>' for (n, nm, d), k in zip(t['steps'], ['server', 'client', 'lite']))
    sections = ''
    for app in ('server', 'client', 'lite'):
        a = t['apps'][app]
        bullets = ''.join(f'<li>{x}</li>' for x in a['bullets'])
        sections += f'''<section class="dl-app card" id="{ANCHOR[app]}"><div class="dl-head">{icon(ICON[app])}<div><span class="dl-tag">{a['tag']}</span><h2>{a['name']}</h2></div></div><p class="dl-role">{a['role']}</p>
<div class="dl-body">{carousel(app, L, base, t)}<div class="dl-info"><ul class="points">{bullets}</ul>{cta(app, 'dl_' + app, a['cta'], L, base)}<p class="note">{a['note']}</p></div></div></section>
'''
    page = f'''<!doctype html>
<html lang="{LANGS[L][0]}">
<head>
<meta charset="utf-8">
{PV_SCRIPT}
{GA_TAG}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t['title'])}</title>
<meta name="description" content="{html.escape(t['desc'])}">
{seo.meta(L, path, t['title'], t['desc'], {l: LANGS[l][1] + 'downloads/' for l in LANGS}, noindex=NOINDEX)}{seo.ld([seo.ORG, seo.website(L, path)] + seo.webpage(L, path, t['title'], t['desc'], [('DogNAS', LANGS[L][1].lstrip('/')), ('Downloads', path)]))}
{CSS_INLINE}
</head>
<body><div class="wrap">
<header class="top"><a class="brand" href="{home}"><img src="{base}assets/icon-80.webp" alt="" width="36" height="36"><span>Dog<b>NAS</b></span></a><nav class="lang">{nav}</nav></header>
<section class="hero dl-hero"><h1>{t['h1']}</h1><p>{t['lead']}</p>
<ol class="dl-steps">{steps}</ol>
{cta('server', 'dl_hero_server', t['apps']['server']['cta'], L, base)}<p class="cta-sub">{t['trust']}</p></section>
{sections}
<h2>{t['cmp_h']}</h2><div class="card wide"><p>{t['cmp']}</p></div>
<p><a href="{home}">← {t['back']}</a></p>
<footer><span>© 2026 DogNAS · {TM_NOTE[L]}</span><span>{blog_link(L, base)}<a href="{base}privacy/#{L}">{t['privacy']}</a> · <a href="#" data-cookie-prefs>Cookies</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span></footer>
</div>{JS}</body>
</html>
'''
    out = os.path.join(ROOT, path, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(page)
print('ok')

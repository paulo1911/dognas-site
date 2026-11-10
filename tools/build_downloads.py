"""Downloads page: one dedicated page for the three apps in install order (server, Client, Client Lite).
en at /downloads/, pt at /pt/downloads/, es at /es/downloads/. Run: python3 tools/build_downloads.py (after tools/prepare_downloads.py).
Each app: Play-style screenshot carousel (CSS scroll-snap), benefit bullets, one store CTA (A red button / B official badge, same
html[data-pv] experiment as the home). cta_id = dl_<app> (hero: dl_hero_server); B adds the `_b` suffix. NOINDEX stays on until the
owner approves the page and the Client on Play has the features shown (scan, templates)."""
import os, json, html
import seo
from build_home import cards, CSS_INLINE, blog_link, blog_nav, ROOT, GA_TAG, PV_SCRIPT, LANGS, NAMES, EMAIL, icon, play, client_play, BADGE, TM_NOTE
NOINDEX = True
CAPS = json.load(open(os.path.join(ROOT, 'content', 'downloads_captions.json'), encoding='utf-8'))
T = {
 'pt': dict(title='Baixar o DogNAS — servidor e apps para Android', desc='Baixe o DogNAS: o servidor que transforma um Android em armazenamento privado na sua rede Wi-Fi e os apps DogNAS Client e Client Lite para acessar seus arquivos.',
   h1='Baixe os apps do DogNAS', lead='O DogNAS transforma um Android parado em armazenamento privado na sua rede Wi-Fi. São três apps: o servidor fica em casa e os apps de acesso abrem seus arquivos no celular. Comece pelo servidor.',
   steps=[('1', 'Servidor', 'No Android que fica em casa'), ('2', 'Client', 'No celular do dia a dia'), ('3', 'Client Lite', 'Versão leve, opcional')],
   trust='Sem conta, sem anúncios e sem nuvem. Os apps não coletam dados.',
   apps={
    'server': dict(name='DogNAS', tag='Passo 1 · O servidor', role='Instale no Android que vai ficar em casa: ele guarda seus arquivos e os outros celulares se conectam a ele.', gain='O que você ganha: um armazenamento privado em casa, com um Android que você já tem.',
      bullets=['Guarde fotos, vídeos e documentos em casa, sem mensalidade de nuvem', 'Conecte os outros celulares em segundos, por QR Code e PIN, sem criar conta', 'Escolha onde guardar: no aparelho, num cartão SD ou num HD USB', 'Cada pessoa da casa tem o seu espaço e o seu PIN', 'Funciona também em tablet e TV box Android'],
      cta='Baixar o servidor', note='Android 7.0 ou superior. Comece no plano Grátis; o Pro é opcional (compra única, sem assinatura).'),
    'client': dict(name='DogNAS Client', tag='Passo 2 · O app de acesso', role='Instale no celular que vai usar seus arquivos. É o app completo para abrir, enviar e organizar o que está no seu DogNAS.', gain='O que você ganha: seus arquivos de casa no celular e papéis escaneados direto para o DogNAS.',
      bullets=['Libere espaço no celular enviando fotos e vídeos para o DogNAS', 'Escaneie papéis com a câmera e guarde como PDF ou JPEG direto no DogNAS', 'Veja fotos, vídeos, músicas e PDFs na hora, sem baixar antes', 'Envios que continuam de onde pararam se o Wi-Fi cair', 'Comece organizado com pastas prontas: Casa, Trabalho e Mínimo'],
      cta='Baixar o Client', note='Precisa do servidor DogNAS (passo 1) na mesma rede Wi-Fi. Android 7.0 ou superior.'),
    'lite': dict(name='DogNAS Client Lite', tag='Passo 2 · Versão leve', role='O app de acesso mais simples e leve, bom para celulares mais antigos ou com pouco espaço.', gain='O que você ganha: acesso aos arquivos até em um celular antigo.',
      bullets=['Acesse seus arquivos mesmo em um celular mais antigo ou com pouco espaço', 'Conecte em segundos pelo QR Code', 'Comece com modelos de pasta prontos', 'Acompanhe quanto espaço o seu perfil já usa', 'Baixe os arquivos para o celular quando precisar'],
      cta='Baixar o Client Lite', note='Precisa do servidor DogNAS (passo 1) na mesma rede Wi-Fi. Android 7.0 ou superior.')},
   cmp_h='Client ou Client Lite?', cmp='O Client é o app completo: escanear documentos, ver arquivos sem baixar e miniaturas. O Client Lite é mais leve e simples, para aparelhos antigos. Os dois abrem o mesmo servidor, e você pode instalar os dois.',
   car='Capturas de tela', prev='Anterior', next='Próxima', back='Voltar ao início', privacy='Política de privacidade'),
 'en': dict(title='Download DogNAS — server and apps for Android', desc='Download DogNAS: the server that turns an Android into private storage on your Wi-Fi, and the DogNAS Client and Client Lite apps to reach your files.',
   h1='Download the DogNAS apps', lead='DogNAS turns an idle Android into private storage on your Wi-Fi. There are three apps: the server stays at home and the access apps open your files on your phone. Start with the server.',
   steps=[('1', 'Server', 'On the Android that stays home'), ('2', 'Client', 'On your everyday phone'), ('3', 'Client Lite', 'Light version, optional')],
   trust='No account, no ads and no cloud. The apps collect no data.',
   apps={
    'server': dict(name='DogNAS', tag='Step 1 · The server', role='Install it on the Android that will stay at home: it keeps your files and the other phones connect to it.', gain='What you get: private storage at home, using an Android you already own.',
      bullets=['Keep photos, videos and documents at home, with no cloud subscription', 'Connect the other phones in seconds, with a QR Code and PIN, no account', 'Choose where to store: on the device, an SD card or a USB drive', 'Everyone at home gets their own space and PIN', 'Also works on an Android tablet or TV box'],
      cta='Download the server', note='Android 7.0 or newer. Start on the Free plan; Pro is optional (one-time purchase, no subscription).'),
    'client': dict(name='DogNAS Client', tag='Step 2 · The access app', role='Install it on the phone you will use your files from. It is the full app to open, send and organize what is on your DogNAS.', gain='What you get: your home files on your phone, and scanned papers sent straight to your DogNAS.',
      bullets=['Free up phone storage by sending photos and videos to your DogNAS', 'Scan paper with the camera and save it as PDF or JPEG straight to your DogNAS', 'See photos, videos, music and PDFs right away, without downloading first', 'Uploads pick up where they stopped if the Wi-Fi drops', 'Start organized with ready-made folders: Home, Work and Minimal'],
      cta='Download the Client', note='Needs the DogNAS server (step 1) on the same Wi-Fi network. Android 7.0 or newer.'),
    'lite': dict(name='DogNAS Client Lite', tag='Step 2 · Light version', role='The simpler, lighter access app, good for older phones or phones with little space.', gain='What you get: access to your files even on an older phone.',
      bullets=['Reach your files even on an older phone or one with little space', 'Connect in seconds with the QR Code', 'Start with ready-made folder templates', 'See how much space your profile already uses', 'Download files to your phone when you need them'],
      cta='Download the Client Lite', note='Needs the DogNAS server (step 1) on the same Wi-Fi network. Android 7.0 or newer.')},
   cmp_h='Client or Client Lite?', cmp='The Client is the full app: scan documents, view files without downloading and thumbnails. The Client Lite is lighter and simpler, for older devices. Both open the same server, and you can install both.',
   car='Screenshots', prev='Previous', next='Next', back='Back to home', privacy='Privacy policy'),
 'es': dict(title='Descargar DogNAS — servidor y apps para Android', desc='Descarga DogNAS: el servidor que convierte un Android en almacenamiento privado en tu Wi-Fi y las apps DogNAS Client y Client Lite para acceder a tus archivos.',
   h1='Descarga las apps de DogNAS', lead='DogNAS convierte un Android parado en almacenamiento privado en tu Wi-Fi. Son tres apps: el servidor se queda en casa y las apps de acceso abren tus archivos en el móvil. Empieza por el servidor.',
   steps=[('1', 'Servidor', 'En el Android que se queda en casa'), ('2', 'Client', 'En tu móvil de todos los días'), ('3', 'Client Lite', 'Versión ligera, opcional')],
   trust='Sin cuenta, sin anuncios y sin nube. Las apps no recogen datos.',
   apps={
    'server': dict(name='DogNAS', tag='Paso 1 · El servidor', role='Instálalo en el Android que se quedará en casa: guarda tus archivos y los demás móviles se conectan a él.', gain='Lo que ganas: almacenamiento privado en casa, con un Android que ya tienes.',
      bullets=['Guarda fotos, vídeos y documentos en casa, sin suscripción de nube', 'Conecta los demás móviles en segundos, con código QR y PIN, sin crear cuenta', 'Elige dónde guardar: en el dispositivo, en una tarjeta SD o en un disco USB', 'Cada persona de casa tiene su espacio y su PIN', 'También funciona en una tablet o TV box Android'],
      cta='Descargar el servidor', note='Android 7.0 o superior. Empieza en el plan Gratis; el Pro es opcional (compra única, sin suscripción).'),
    'client': dict(name='DogNAS Client', tag='Paso 2 · La app de acceso', role='Instálala en el móvil desde el que usarás tus archivos. Es la app completa para abrir, enviar y organizar lo que hay en tu DogNAS.', gain='Lo que ganas: tus archivos de casa en el móvil y papeles escaneados directo a tu DogNAS.',
      bullets=['Libera espacio en el móvil enviando fotos y vídeos a tu DogNAS', 'Escanea papeles con la cámara y guárdalos como PDF o JPEG directo en tu DogNAS', 'Mira fotos, vídeos, música y PDF al momento, sin descargar antes', 'Los envíos continúan donde se quedaron si el Wi-Fi se cae', 'Empieza ordenado con carpetas listas: Casa, Trabajo y Mínimo'],
      cta='Descargar el Client', note='Necesita el servidor DogNAS (paso 1) en la misma red Wi-Fi. Android 7.0 o superior.'),
    'lite': dict(name='DogNAS Client Lite', tag='Paso 2 · Versión ligera', role='La app de acceso más simple y ligera, buena para móviles más antiguos o con poco espacio.', gain='Lo que ganas: acceso a tus archivos hasta en un móvil antiguo.',
      bullets=['Accede a tus archivos incluso en un móvil antiguo o con poco espacio', 'Conecta en segundos con el código QR', 'Empieza con plantillas de carpetas listas', 'Mira cuánto espacio usa ya tu perfil', 'Descarga los archivos al móvil cuando los necesites'],
      cta='Descargar el Client Lite', note='Necesita el servidor DogNAS (paso 1) en la misma red Wi-Fi. Android 7.0 o superior.')},
   cmp_h='¿Client o Client Lite?', cmp='El Client es la app completa: escanear documentos, ver archivos sin descargar y miniaturas. El Client Lite es más ligero y simple, para dispositivos antiguos. Los dos abren el mismo servidor y puedes instalar los dos.',
   car='Capturas de pantalla', prev='Anterior', next='Siguiente', back='Volver al inicio', privacy='Política de privacidad'),
}
GAINS = {'pt': ('O que você ganha com o DogNAS', [('phone-free', 'Mais espaço no celular', 'Mande fotos, vídeos e documentos para o DogNAS e apague do celular quando quiser.'), ('devices', 'Uma nova vida para um Android parado', 'O celular ou tablet esquecido na gaveta vira o armazenamento da casa.'), ('no-cloud', 'Sem mensalidade de nuvem', 'Seus arquivos ficam em casa, na sua rede Wi-Fi. O Pro é opcional e de compra única.'), ('people', 'Privado e para a família toda', 'Sem conta e sem anúncios. Cada pessoa tem o seu perfil, com PIN.')]), 'en': ('What you get with DogNAS', [('phone-free', 'More space on your phone', 'Send photos, videos and documents to your DogNAS and delete them from your phone whenever you want.'), ('devices', 'A second life for an idle Android', 'The phone or tablet forgotten in a drawer becomes your home storage.'), ('no-cloud', 'No cloud subscription', 'Your files stay at home, on your Wi-Fi. Pro is optional and a one-time purchase.'), ('people', 'Private, for the whole family', 'No account and no ads. Everyone gets their own profile, with a PIN.')]), 'es': ('Lo que ganas con DogNAS', [('phone-free', 'Más espacio en el móvil', 'Envía fotos, vídeos y documentos a tu DogNAS y bórralos del móvil cuando quieras.'), ('devices', 'Una nueva vida para un Android parado', 'El móvil o tablet olvidado en un cajón se convierte en el almacenamiento de casa.'), ('no-cloud', 'Sin suscripción de nube', 'Tus archivos se quedan en casa, en tu Wi-Fi. El Pro es opcional y de compra única.'), ('people', 'Privado y para toda la familia', 'Sin cuenta y sin anuncios. Cada persona tiene su perfil, con PIN.')])}
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
    gh, gi = GAINS[L]
    gains = f'<h2>{gh}</h2><div class="dl-gains">' + cards([(h, p) for _, h, p in gi], [k for k, _, _ in gi]) + '</div>'
    sections = ''
    for app in ('server', 'client', 'lite'):
        a = t['apps'][app]
        bullets = ''.join(f'<li>{x}</li>' for x in a['bullets'])
        sections += f'''<section class="dl-app card" id="{ANCHOR[app]}"><div class="dl-head">{icon(ICON[app])}<div><span class="dl-tag">{a['tag']}</span><h2>{a['name']}</h2></div></div><p class="dl-role">{a['role']}</p><p class="dl-gain">{a['gain']}</p>
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
{gains}
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

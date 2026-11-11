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
 'pt': dict(title='Baixar o DogNAS — servidor e apps para Android', desc='Baixe o DogNAS: o servidor que transforma um Android antigo em armazenamento da casa e os apps DogNAS Client e Client Lite para usar no seu celular do dia a dia.',
   h1='Baixe os apps do DogNAS', lead='Use um Android antigo ou parado como o armazenamento da sua casa. Instale o DogNAS nele: é o servidor. No seu celular do dia a dia, instale o DogNAS Client para passar fotos, vídeos e documentos para o servidor pelo Wi-Fi.',
   steps=[('1', 'Android antigo ou parado', 'Instale o servidor DogNAS: ele guarda os arquivos'), ('2', 'Seu celular do dia a dia', 'Instale o Client: ele passa arquivos para o servidor'), ('3', 'Alternativa leve ao Client', 'Client Lite, para um celular mais simples')],
   trust='Sem conta, sem anúncios e sem nuvem. Os apps não coletam dados.',
   apps={
    'server': dict(name='DogNAS (servidor)', tag='Passo 1 · No Android antigo ou parado', role='Instale este app no Android antigo ou parado que vai ficar em casa. Ele vira o armazenamento da casa e guarda os arquivos de todos.', gain='O que você ganha: um armazenamento privado em casa, num Android que estava parado.',
      bullets=['Transforme um Android parado no armazenamento da casa', 'Conecte os celulares da família por QR Code e PIN, sem criar conta', 'Um perfil para cada pessoa, cada um com o seu espaço e o seu PIN', 'Guarde no próprio aparelho, num cartão SD ou num HD USB', 'Funciona também em tablet e TV box Android'],
      cta='Baixar o servidor', note='Instale no aparelho que fica em casa, ligado e no Wi-Fi. Android 7.0 ou superior. Comece no plano Grátis; o Pro é opcional (compra única, sem assinatura).'),
    'client': dict(name='DogNAS Client', tag='Passo 2 · No seu celular do dia a dia', role='Instale este app no celular que você usa todo dia. Ele se conecta ao servidor DogNAS (o Android antigo da casa) pelo Wi-Fi: você passa arquivos para lá e abre os que estão lá.', gain='O que você ganha: espaço livre no celular do dia a dia, com os arquivos guardados no DogNAS.',
      bullets=['Passe fotos e vídeos do celular para o DogNAS e libere espaço no aparelho', 'Escaneie papéis com a câmera e guarde como PDF ou JPEG direto no DogNAS', 'Abra fotos, vídeos, músicas e PDFs que estão no DogNAS sem baixar antes', 'Se o Wi-Fi cair, o envio continua de onde parou', 'Comece organizado com pastas prontas: Casa, Trabalho e Mínimo'],
      cta='Baixar o Client', note='Precisa do servidor DogNAS (passo 1) rodando em outro Android, na mesma rede Wi-Fi. Android 7.0 ou superior.'),
    'lite': dict(name='DogNAS Client Lite', tag='Passo 2 · Alternativa leve ao Client', role='Faz o mesmo papel do Client: roda no seu celular e acessa o servidor DogNAS. É mais simples e leve, bom para um celular antigo ou com pouco espaço.', gain='O que você ganha: acesso aos arquivos do DogNAS até em um celular simples ou antigo.',
      bullets=['Acesse os arquivos do DogNAS num celular mais simples ou com pouco espaço', 'Conecte em segundos pelo QR Code do servidor', 'Comece com modelos de pasta prontos', 'Veja quanto espaço o seu perfil já usa no servidor', 'Baixe os arquivos do DogNAS para o celular quando precisar'],
      cta='Baixar o Client Lite', note='Precisa do servidor DogNAS (passo 1) rodando em outro Android, na mesma rede Wi-Fi. Android 7.0 ou superior.')},
   cmp_h='Client ou Client Lite?', cmp='Os dois rodam no seu celular e acessam o mesmo servidor. O Client é o completo (escanear documentos, ver arquivos sem baixar, miniaturas); o Client Lite é mais leve e simples. Escolha um, ou instale os dois.',
   car='Capturas de tela', prev='Anterior', next='Próxima', back='Voltar ao início', privacy='Política de privacidade'),
 'en': dict(title='Download DogNAS — server and apps for Android', desc='Download DogNAS: the server that turns an old Android into your home storage, and the DogNAS Client and Client Lite apps to use on your everyday phone.',
   h1='Download the DogNAS apps', lead='Use an old or idle Android as your home storage. Install DogNAS on it: that is the server. On your everyday phone, install the DogNAS Client to move photos, videos and documents to the server over Wi-Fi.',
   steps=[('1', 'Old or idle Android', 'Install the DogNAS server: it keeps the files'), ('2', 'Your everyday phone', 'Install the Client: it moves files to the server'), ('3', 'Light alternative to the Client', 'Client Lite, for a simpler phone')],
   trust='No account, no ads and no cloud. The apps collect no data.',
   apps={
    'server': dict(name='DogNAS (server)', tag='Step 1 · On the old or idle Android', role='Install this app on the old or idle Android that will stay at home. It becomes the home storage and keeps everyone’s files.', gain='What you get: private storage at home, on an Android that was sitting idle.',
      bullets=['Turn an idle Android into the home storage', 'Connect the family’s phones with a QR Code and PIN, no account', 'One profile per person, each with its own space and PIN', 'Store on the device itself, an SD card or a USB drive', 'Also works on an Android tablet or TV box'],
      cta='Download the server', note='Install it on the device that stays at home, powered on and on the Wi-Fi. Android 7.0 or newer. Start on the Free plan; Pro is optional (one-time purchase, no subscription).'),
    'client': dict(name='DogNAS Client', tag='Step 2 · On your everyday phone', role='Install this app on the phone you use every day. It connects to the DogNAS server (the old Android at home) over Wi-Fi: you move files there and open the ones stored there.', gain='What you get: free space on your everyday phone, with your files kept on DogNAS.',
      bullets=['Move photos and videos from your phone to DogNAS and free up space on it', 'Scan paper with the camera and save it as PDF or JPEG straight to DogNAS', 'Open photos, videos, music and PDFs stored on DogNAS without downloading first', 'If the Wi-Fi drops, the upload continues where it stopped', 'Start organized with ready-made folders: Home, Work and Minimal'],
      cta='Download the Client', note='Needs the DogNAS server (step 1) running on another Android, on the same Wi-Fi network. Android 7.0 or newer.'),
    'lite': dict(name='DogNAS Client Lite', tag='Step 2 · Light alternative to the Client', role='Does the same job as the Client: it runs on your phone and reaches the DogNAS server. It is simpler and lighter, good for an older phone or one with little space.', gain='What you get: access to your DogNAS files even on a simple or older phone.',
      bullets=['Reach your DogNAS files on a simpler phone or one with little space', 'Connect in seconds with the server’s QR Code', 'Start with ready-made folder templates', 'See how much space your profile already uses on the server', 'Download files from DogNAS to your phone when you need them'],
      cta='Download the Client Lite', note='Needs the DogNAS server (step 1) running on another Android, on the same Wi-Fi network. Android 7.0 or newer.')},
   cmp_h='Client or Client Lite?', cmp='Both run on your phone and reach the same server. The Client is the full app (scan documents, view files without downloading, thumbnails); the Client Lite is lighter and simpler. Pick one, or install both.',
   car='Screenshots', prev='Previous', next='Next', back='Back to home', privacy='Privacy policy'),
 'es': dict(title='Descargar DogNAS — servidor y apps para Android', desc='Descarga DogNAS: el servidor que convierte un Android antiguo en el almacenamiento de casa y las apps DogNAS Client y Client Lite para usar en tu móvil de todos los días.',
   h1='Descarga las apps de DogNAS', lead='Usa un Android antiguo o parado como el almacenamiento de tu casa. Instala DogNAS en él: es el servidor. En tu móvil de todos los días, instala DogNAS Client para pasar fotos, vídeos y documentos al servidor por Wi-Fi.',
   steps=[('1', 'Android antiguo o parado', 'Instala el servidor DogNAS: guarda los archivos'), ('2', 'Tu móvil de todos los días', 'Instala el Client: pasa archivos al servidor'), ('3', 'Alternativa ligera al Client', 'Client Lite, para un móvil más sencillo')],
   trust='Sin cuenta, sin anuncios y sin nube. Las apps no recogen datos.',
   apps={
    'server': dict(name='DogNAS (servidor)', tag='Paso 1 · En el Android antiguo o parado', role='Instala esta app en el Android antiguo o parado que se quedará en casa. Se convierte en el almacenamiento de casa y guarda los archivos de todos.', gain='Lo que ganas: almacenamiento privado en casa, en un Android que estaba parado.',
      bullets=['Convierte un Android parado en el almacenamiento de casa', 'Conecta los móviles de la familia con código QR y PIN, sin crear cuenta', 'Un perfil para cada persona, cada uno con su espacio y su PIN', 'Guarda en el propio dispositivo, en una tarjeta SD o en un disco USB', 'También funciona en una tablet o TV box Android'],
      cta='Descargar el servidor', note='Instálalo en el dispositivo que se queda en casa, encendido y con Wi-Fi. Android 7.0 o superior. Empieza en el plan Gratis; el Pro es opcional (compra única, sin suscripción).'),
    'client': dict(name='DogNAS Client', tag='Paso 2 · En tu móvil de todos los días', role='Instala esta app en el móvil que usas todos los días. Se conecta al servidor DogNAS (el Android antiguo de casa) por Wi-Fi: pasas archivos allí y abres los que están allí.', gain='Lo que ganas: espacio libre en tu móvil de todos los días, con los archivos guardados en DogNAS.',
      bullets=['Pasa fotos y vídeos del móvil a DogNAS y libera espacio en el aparato', 'Escanea papeles con la cámara y guárdalos como PDF o JPEG directo en DogNAS', 'Abre fotos, vídeos, música y PDF guardados en DogNAS sin descargar antes', 'Si el Wi-Fi se cae, el envío continúa donde se quedó', 'Empieza ordenado con carpetas listas: Casa, Trabajo y Mínimo'],
      cta='Descargar el Client', note='Necesita el servidor DogNAS (paso 1) funcionando en otro Android, en la misma red Wi-Fi. Android 7.0 o superior.'),
    'lite': dict(name='DogNAS Client Lite', tag='Paso 2 · Alternativa ligera al Client', role='Cumple el mismo papel que el Client: funciona en tu móvil y accede al servidor DogNAS. Es más simple y ligera, buena para un móvil antiguo o con poco espacio.', gain='Lo que ganas: acceso a los archivos de DogNAS hasta en un móvil sencillo o antiguo.',
      bullets=['Accede a los archivos de DogNAS en un móvil más sencillo o con poco espacio', 'Conecta en segundos con el código QR del servidor', 'Empieza con plantillas de carpetas listas', 'Mira cuánto espacio usa ya tu perfil en el servidor', 'Descarga los archivos de DogNAS al móvil cuando los necesites'],
      cta='Descargar el Client Lite', note='Necesita el servidor DogNAS (paso 1) funcionando en otro Android, en la misma red Wi-Fi. Android 7.0 o superior.')},
   cmp_h='¿Client o Client Lite?', cmp='Los dos funcionan en tu móvil y acceden al mismo servidor. El Client es la app completa (escanear documentos, ver archivos sin descargar, miniaturas); el Client Lite es más ligero y simple. Elige uno, o instala los dos.',
   car='Capturas de pantalla', prev='Anterior', next='Siguiente', back='Volver al inicio', privacy='Política de privacidad'),
}
GAINS = {
 'pt': ('O que você ganha com o DogNAS', [('phone-free', 'Libere espaço no celular do dia a dia', 'Passe fotos, vídeos e documentos do seu celular para o DogNAS, que roda no Android antigo da casa. Confira que chegaram e apague do celular o que já está guardado.'), ('devices', 'Dê nova vida a um Android parado', 'O celular ou tablet que está na gaveta vira o armazenamento da casa: é nele que o DogNAS (servidor) roda.'), ('people', 'Arquivos organizados em perfis', 'Cada pessoa da casa tem o seu perfil, com espaço e PIN próprios.'), ('no-cloud', 'Sem mensalidade de nuvem', 'Os arquivos ficam no seu Android, na sua rede Wi-Fi. Sem conta e sem anúncios.')]),
 'en': ('What you get with DogNAS', [('phone-free', 'Free up your everyday phone', 'Move photos, videos and documents from your phone to DogNAS, which runs on the old Android at home. Check they arrived, then delete from your phone what is already stored.'), ('devices', 'Give an idle Android a new life', 'The phone or tablet in the drawer becomes the home storage: it is where DogNAS (the server) runs.'), ('people', 'Files organized in profiles', 'Everyone at home has their own profile, with its own space and PIN.'), ('no-cloud', 'No cloud subscription', 'Files stay on your Android, on your Wi-Fi. No account and no ads.')]),
 'es': ('Lo que ganas con DogNAS', [('phone-free', 'Libera espacio en tu móvil de todos los días', 'Pasa fotos, vídeos y documentos de tu móvil a DogNAS, que funciona en el Android antiguo de casa. Comprueba que llegaron y borra del móvil lo que ya está guardado.'), ('devices', 'Dale nueva vida a un Android parado', 'El móvil o tablet del cajón se convierte en el almacenamiento de casa: ahí funciona DogNAS (el servidor).'), ('people', 'Archivos organizados en perfiles', 'Cada persona de casa tiene su perfil, con espacio y PIN propios.'), ('no-cloud', 'Sin suscripción de nube', 'Los archivos se quedan en tu Android, en tu Wi-Fi. Sin cuenta y sin anuncios.')]),
}
FLOW = {
 'pt': dict(h='Como os dois aparelhos trabalham juntos', client_tag='No seu celular do dia a dia', client_name='DogNAS Client', server_tag='No Android antigo ou parado', server_name='DogNAS (servidor)',
   client=['Passe fotos, vídeos e documentos para o DogNAS', 'Libere espaço: apague do celular o que já está guardado', 'Abra os arquivos guardados, no Wi-Fi da casa'],
   server=['Guarda os arquivos de toda a família', 'Cada pessoa tem o seu perfil, com espaço e PIN', 'Sem mensalidade de nuvem'],
   wifi='Wi-Fi da sua casa', wifi_sub='Sem nuvem no meio', result='O resultado: o celular do dia a dia com espaço livre e os arquivos guardados em casa.',
   alt_c='Captura real do DogNAS Client no celular: pasta de fotos com miniaturas', alt_s='Captura real do servidor DogNAS no Android antigo: servidor online, um cliente transferindo e o armazenamento da casa'),
 'en': dict(h='How the two devices work together', client_tag='On your everyday phone', client_name='DogNAS Client', server_tag='On the old or idle Android', server_name='DogNAS (server)',
   client=['Move photos, videos and documents to DogNAS', 'Free up space: delete from your phone what is already stored', 'Open the stored files, on the home Wi-Fi'],
   server=['Keeps the whole family’s files', 'Everyone gets their own profile, with space and PIN', 'No cloud subscription'],
   wifi='Your home Wi-Fi', wifi_sub='No cloud in between', result='The result: your everyday phone with free space and your files kept at home.',
   alt_c='Real screenshot of DogNAS Client on the phone: photo folder with thumbnails', alt_s='Real screenshot of the DogNAS server on the old Android: server online, one client transferring and the home storage'),
 'es': dict(h='Cómo trabajan juntos los dos dispositivos', client_tag='En tu móvil de todos los días', client_name='DogNAS Client', server_tag='En el Android antiguo o parado', server_name='DogNAS (servidor)',
   client=['Pasa fotos, vídeos y documentos a DogNAS', 'Libera espacio: borra del móvil lo que ya está guardado', 'Abre los archivos guardados, con el Wi-Fi de casa'],
   server=['Guarda los archivos de toda la familia', 'Cada persona tiene su perfil, con espacio y PIN', 'Sin suscripción de nube'],
   wifi='El Wi-Fi de tu casa', wifi_sub='Sin nube de por medio', result='El resultado: tu móvil de todos los días con espacio libre y tus archivos guardados en casa.',
   alt_c='Captura real de DogNAS Client en el móvil: carpeta de fotos con miniaturas', alt_s='Captura real del servidor DogNAS en el Android antiguo: servidor online, un cliente transfiriendo y el almacenamiento de casa'),
}
def flow(L, base):
    f = FLOW[L]
    def dev(kind, tag, name, items, alt):
        stem = f'{base}assets/downloads/diagram/{L}/{kind}'
        lis = ''.join(f'<li>{x}</li>' for x in items)
        return (f'<div class="dl-dev dl-{kind}"><span class="dl-tag">{tag}</span><h3>{name}</h3>'
                f'<div class="dl-ph"><img src="{stem}-480.webp" srcset="{stem}-320.webp 320w, {stem}-480.webp 480w" sizes="260px" alt="{html.escape(alt)}" width="480" height="{1370 * 480 // 1080 if kind == "client" else 1760 * 480 // 1080}" loading="lazy"></div>'
                f'<ul class="points">{lis}</ul></div>')
    arrow = (f'<div class="dl-link" aria-hidden="true"><svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5a10 10 0 0 1 14 0"/><path d="M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19" r="1"/></svg>'
             f'<span class="dl-arrows">⇄</span><strong>{f["wifi"]}</strong><span>{f["wifi_sub"]}</span></div>')
    return (f'<section class="dl-flow"><h2>{f["h"]}</h2><div class="dl-flow-grid">'
            + dev('client', f['client_tag'], f['client_name'], f['client'], f['alt_c']) + arrow
            + dev('server', f['server_tag'], f['server_name'], f['server'], f['alt_s'])
            + f'</div><p class="dl-result">{f["result"]}</p></section>')
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
{flow(L, base)}
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

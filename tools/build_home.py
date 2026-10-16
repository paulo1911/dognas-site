"""Landing pages (pt at /, en at /en/, es at /es/) with the store screenshots — 2026-10-16.
Run: python3 tools/build_home.py (screenshots live in assets/shots/<lang>/)."""
import os, html, hashlib
ROOT = os.path.expanduser('~/workspace/dognas/dognas-site')
EMAIL = 'me.pauloleite.dev@gmail.com'
# Cache busting (2026-10-16): Pages caches files for 10 min; a new page with a cached old
# stylesheet broke the layout. The CSS URL changes whenever its content does.
CSS_V = hashlib.sha1(open(os.path.join(ROOT, 'assets/style.css'), 'rb').read()).hexdigest()[:8]
LANGS = {'pt': ('pt-BR', ''), 'en': ('en', 'en/'), 'es': ('es', 'es/')}
NAMES = {'pt': 'Português', 'en': 'English', 'es': 'Español'}
T = {
 'pt': dict(title='DogNAS — Seus arquivos em casa', desc='Transforme um Android num armazenamento particular na sua rede Wi-Fi, sem nuvem.',
   h1='Seus arquivos em casa.', lead='O DogNAS transforma um Android que você já tem num armazenamento particular para a sua casa: seus arquivos ficam com você, na sua rede Wi-Fi, sem nuvem e sem mensalidade.',
   soon='Em breve na Google Play', how='Como funciona', alt1='Servidor DogNAS online', alt2='Arquivos no DogNAS Lite',
   steps=[('Ligue o servidor', 'Instale o DogNAS no Android que vai guardar os arquivos — no aparelho, num cartão SD ou num HD USB — e toque em Iniciar.', 'server-status'),
          ('Conecte seu celular', 'Gere o QR Code de um perfil e leia com o DogNAS Lite. Cada perfil tem seu PIN e seu espaço.', 'server-qr'),
          ('Use seus arquivos', 'Navegue, envie e baixe pelo Wi-Fi de casa. PCs e Macs conectam por SFTP.', 'lite-files')],
   watch='Acompanhe tudo', cap1='Transferências e clientes no servidor', cap2='Fila de transferências no celular',
   feats=[('Sem nuvem', 'Os arquivos trafegam só entre os seus aparelhos, na sua rede, com conexão cifrada.'), ('Perfis para a família', 'Cada perfil tem seu próprio espaço e seu PIN.'), ('Sem conta e sem anúncios', 'Nada de cadastro, anúncios ou coleta de dados.'), ('Reaproveite um Android', 'Aquele celular parado na gaveta vira o armazenamento da casa.')],
   plans='Grátis para começar', planhead=('', 'Grátis', 'Pro'),
   rows=[('Armazenamento', '64 GB', 'Todo o aparelho'), ('Perfis', 'Casa + 2', 'Ilimitados'), ('Dispositivos pareados', '3', 'Ilimitados'), ('Performance', 'Boa', 'Máxima otimizada'), ('Com o app fechado', 'Pausam', 'Continuam'), ('Após reiniciar', 'Toque para iniciar', 'Inicia sozinho')],
   plannote='DogNAS Pro: compra única, sem assinatura. O DogNAS Lite é sempre gratuito.',
   apps='Dois apps', app1='O servidor: instale no Android que vai guardar os arquivos.', app2='O app de acesso: instale no celular para ver, enviar e baixar os arquivos.', privacy='Política de privacidade'),
 'en': dict(title='DogNAS — Your files at home', desc='Turn an Android into private storage on your Wi-Fi, with no cloud.',
   h1='Your files at home.', lead='DogNAS turns an Android you already own into private storage for your home: your files stay with you, on your Wi-Fi, with no cloud and no monthly fee.',
   soon='Coming soon to Google Play', how='How it works', alt1='DogNAS server online', alt2='Files in DogNAS Lite',
   steps=[('Start the server', 'Install DogNAS on the Android that will keep your files — on the device, an SD card or a USB drive — and tap Start.', 'server-status'),
          ('Connect your phone', "Generate a profile's QR Code and scan it with DogNAS Lite. Each profile has its own PIN and space.", 'server-qr'),
          ('Use your files', 'Browse, upload and download over your home Wi-Fi. PCs and Macs connect via SFTP.', 'lite-files')],
   watch='Follow everything', cap1='Transfers and clients on the server', cap2='Transfer queue on your phone',
   feats=[('No cloud', 'Files travel only between your own devices, on your network, encrypted.'), ('Profiles for the family', 'Each profile has its own space and its own PIN.'), ('No account, no ads', 'No sign-up, no ads, no data collection.'), ('Reuse an Android', 'That phone sitting in a drawer becomes your home storage.')],
   plans='Free to start', planhead=('', 'Free', 'Pro'),
   rows=[('Storage', '64 GB', 'All of it'), ('Profiles', 'Home + 2', 'Unlimited'), ('Paired devices', '3', 'Unlimited'), ('Performance', 'Good', 'Maximum, optimized'), ('With the app closed', 'Pause', 'Keep going'), ('After a reboot', 'Tap to start', 'Starts by itself')],
   plannote='DogNAS Pro: one-time purchase, no subscription. DogNAS Lite is always free.',
   apps='Two apps', app1='The server: install it on the Android that will keep your files.', app2='The access app: install it on your phone to browse, upload and download.', privacy='Privacy policy'),
 'es': dict(title='DogNAS — Tus archivos en casa', desc='Convierte un Android en un almacenamiento privado en tu Wi-Fi, sin nube.',
   h1='Tus archivos en casa.', lead='DogNAS convierte un Android que ya tienes en un almacenamiento privado para tu casa: tus archivos se quedan contigo, en tu Wi-Fi, sin nube y sin cuotas mensuales.',
   soon='Próximamente en Google Play', how='Cómo funciona', alt1='Servidor DogNAS en línea', alt2='Archivos en DogNAS Lite',
   steps=[('Enciende el servidor', 'Instala DogNAS en el Android que guardará los archivos — en el dispositivo, una tarjeta SD o un disco USB — y toca Iniciar.', 'server-status'),
          ('Conecta tu teléfono', 'Genera el código QR de un perfil y escanéalo con DogNAS Lite. Cada perfil tiene su PIN y su espacio.', 'server-qr'),
          ('Usa tus archivos', 'Navega, sube y descarga por el Wi-Fi de casa. PC y Mac se conectan por SFTP.', 'lite-files')],
   watch='Sigue todo', cap1='Transferencias y clientes en el servidor', cap2='Cola de transferencias en el teléfono',
   feats=[('Sin nube', 'Los archivos viajan solo entre tus dispositivos, en tu red, cifrados.'), ('Perfiles para la familia', 'Cada perfil tiene su propio espacio y su PIN.'), ('Sin cuenta ni anuncios', 'Sin registro, sin anuncios, sin recopilación de datos.'), ('Reutiliza un Android', 'Ese teléfono olvidado en un cajón se convierte en el almacenamiento de casa.')],
   plans='Gratis para empezar', planhead=('', 'Gratis', 'Pro'),
   rows=[('Almacenamiento', '64 GB', 'Todo el dispositivo'), ('Perfiles', 'Casa + 2', 'Ilimitados'), ('Dispositivos vinculados', '3', 'Ilimitados'), ('Rendimiento', 'Bueno', 'Máximo optimizado'), ('Con la app cerrada', 'Se pausan', 'Continúan'), ('Tras reiniciar', 'Toca para iniciar', 'Se inicia solo')],
   plannote='DogNAS Pro: compra única, sin suscripción. DogNAS Lite siempre es gratis.',
   apps='Dos apps', app1='El servidor: instálalo en el Android que guardará los archivos.', app2='La app de acceso: instálala en tu teléfono para ver, subir y descargar archivos.', privacy='Política de privacidad'),
}
def phone(src, alt): return f'<div class="phone"><img src="{src}" alt="{html.escape(alt)}" width="540" height="1080" loading="lazy"></div>'
for L, t in T.items():
    base = '' if L == 'pt' else '../'
    sh = f'{base}assets/shots/{L}/'
    nav = ''.join(f'<a href="{base}{LANGS[l][1]}"{" class=on" if l == L else ""}>{NAMES[l]}</a>' for l in LANGS)
    steps = ''.join(f'<div class="step"><div class="num">{i}</div><h3>{h}</h3><p>{p}</p>{phone(sh + img + ".webp", h)}</div>' for i, (h, p, img) in enumerate(t['steps'], 1))
    feats = ''.join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in t['feats'])
    rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in t['rows'])
    head = ''.join(f'<th>{h}</th>' for h in t['planhead'])
    page = f'''<!doctype html>
<html lang="{LANGS[L][0]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t['title'])}</title>
<meta name="description" content="{html.escape(t['desc'])}">
<meta property="og:title" content="{html.escape(t['title'])}">
<meta property="og:description" content="{html.escape(t['desc'])}">
<meta property="og:image" content="https://dognas.app/assets/og-{L}.jpg">
<meta property="og:url" content="https://dognas.app/{LANGS[L][1]}">
<meta name="twitter:card" content="summary_large_image">
''' + ''.join(f'<link rel="alternate" hreflang="{LANGS[l][0]}" href="https://dognas.app/{LANGS[l][1]}">\n' for l in LANGS) + f'''<link rel="icon" href="{base}assets/icon.png">
<link rel="stylesheet" href="{base}assets/style.css?v={CSS_V}">
</head>
<body><div class="wrap">
<header class="top"><a class="brand" href="{base}{LANGS[L][1]}"><img src="{base}assets/icon.png" alt=""><span>Dog<b>NAS</b></span></a><nav class="lang">{nav}</nav></header>
<div class="hero-grid">
<section class="hero"><img class="logo" src="{base}assets/icon.png" alt="DogNAS"><h1>{t['h1']}</h1><p>{t['lead']}</p>
<div class="cta"><span class="btn primary soon">{t['soon']}</span><a class="btn" href="#how">{t['how']}</a></div></section>
<div class="phones">{phone(sh + 'server-status.webp', t['alt1'])}{phone(sh + 'lite-files.webp', t['alt2'])}</div>
</div>
<h2 id="how">{t['how']}</h2><div class="steps">{steps}</div>
<div class="grid">{feats}</div>
<h2>{t['watch']}</h2>
<div class="twoup"><figure>{phone(sh + 'server-monitor.webp', t['cap1'])}<figcaption>{t['cap1']}</figcaption></figure><figure>{phone(sh + 'lite-transfers.webp', t['cap2'])}<figcaption>{t['cap2']}</figcaption></figure></div>
<h2>{t['plans']}</h2>
<div class="table-wrap"><table class="plans"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
<p class="note">{t['plannote']}</p>
<h2>{t['apps']}</h2>
<div class="grid apps"><div class="card"><img src="{base}assets/icon.png" alt=""><div><h3>DogNAS</h3><p>{t['app1']}</p></div></div><div class="card"><img src="{base}assets/icon-lite.png" alt=""><div><h3>DogNAS Lite</h3><p>{t['app2']}</p></div></div></div>
<footer><span>© 2026 DogNAS</span><span><a href="{base}privacy/#{L}">{t['privacy']}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span></footer>
</div></body></html>
'''
    out = os.path.join(ROOT, 'index.html' if L == 'pt' else f'{L}/index.html')
    open(out, 'w').write(page)
print('ok')

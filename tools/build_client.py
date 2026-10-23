"""DogNAS Client app page (pt at /client/, en at /en/client/, es at /es/client/).
Run: python3 tools/build_client.py. Reuses the shell of build_home.py. Store links stay
"Coming soon" until the app is published (BACKLOG REL-7 / FC-74): then fill STORE below."""
import os, html
from build_home import ROOT, GA_TAG, CSS_V, LANGS, NAMES, EMAIL, icon, cards, phone
# Fill with the real URLs when published; empty = shows "Coming soon".
STORE = {'play': '', 'apple': ''}
T = {
 'pt': dict(title='DogNAS Client — O app completo para acessar seu DogNAS', desc='DogNAS Client: o app gratuito para Android e iPhone que acessa seus arquivos no DogNAS pelo Wi-Fi de casa. Sem nuvem.',
   h1='DogNAS Client', lead='O app completo para acessar os arquivos do seu DogNAS, no Android e no iPhone, pelo Wi-Fi da sua casa. Sem nuvem e sem conta.',
   play='Google Play', apple='App Store', soon='Em breve', note_soon='Ainda não está nas lojas. Enquanto isso, o DogNAS Client Lite já acessa o seu DogNAS no Android.',
   feats_h='O que ele faz',
   feats=[('Pareamento por QR Code', 'Aponte a câmera para o QR Code do perfil no servidor e digite o PIN. Cada perfil tem seu espaço.'),
          ('Navegue e organize', 'Veja as pastas, crie, renomeie e apague arquivos direto no seu DogNAS.'),
          ('Envie e baixe', 'Mande fotos, vídeos e documentos para o servidor e baixe de volta, com fila de transferências.'),
          ('Só na sua rede', 'Os arquivos ficam no seu Android DogNAS e trafegam pelo Wi-Fi de casa, cifrados (SSH/SFTP). Nada passa por nuvem.')],
   icons=['qr', 'devices', 'phone-free', 'no-cloud'],
   plans_h='Grátis, com o Pro no servidor',
   plans='O DogNAS Client é gratuito. Os limites e o Pro (compra única, sem assinatura) pertencem ao servidor DogNAS: no plano Grátis, 64 GB, perfil Casa + 2 e 3 dispositivos; no Pro, o aparelho inteiro e transferências que continuam com o app fechado.',
   req_h='Requisitos', req='Um servidor DogNAS na mesma rede Wi-Fi. Android e iPhone (iOS 15 ou mais recente).',
   lite_h='E o Client Lite?', lite='O DogNAS Client Lite continua disponível na Google Play: é o app leve, ideal para aparelhos mais simples.',
   back='Voltar ao início', privacy='Política de privacidade'),
 'en': dict(title='DogNAS Client — The full app to reach your DogNAS', desc='DogNAS Client: the free app for Android and iPhone that reaches your files on DogNAS over your home Wi-Fi. No cloud.',
   h1='DogNAS Client', lead='The full app to reach the files on your DogNAS, on Android and iPhone, over your home Wi-Fi. No cloud, no account.',
   play='Google Play', apple='App Store', soon='Coming soon', note_soon='Not in the stores yet. Meanwhile, DogNAS Client Lite already reaches your DogNAS on Android.',
   feats_h='What it does',
   feats=[('Pair with a QR code', 'Point the camera at the profile’s QR code on the server and enter the PIN. Each profile has its own space.'),
          ('Browse and organize', 'See your folders; create, rename and delete files right on your DogNAS.'),
          ('Upload and download', 'Send photos, videos and documents to the server and download them back, with a transfer queue.'),
          ('Only on your network', 'Files stay on your DogNAS Android and travel over your home Wi-Fi, encrypted (SSH/SFTP). Nothing goes through a cloud.')],
   icons=['qr', 'devices', 'phone-free', 'no-cloud'],
   plans_h='Free, with Pro on the server',
   plans='DogNAS Client is free. The limits and Pro (one-time purchase, no subscription) belong to the DogNAS server: Free means 64 GB, Home + 2 profiles and 3 devices; Pro means the whole device and transfers that keep going with the app closed.',
   req_h='Requirements', req='A DogNAS server on the same Wi-Fi network. Android and iPhone (iOS 15 or newer).',
   lite_h='What about Client Lite?', lite='DogNAS Client Lite stays available on Google Play: it is the light app, ideal for simpler devices.',
   back='Back to home', privacy='Privacy policy'),
 'es': dict(title='DogNAS Client — La app completa para acceder a tu DogNAS', desc='DogNAS Client: la app gratuita para Android y iPhone que accede a tus archivos en DogNAS por el Wi-Fi de casa. Sin nube.',
   h1='DogNAS Client', lead='La app completa para acceder a los archivos de tu DogNAS, en Android y iPhone, por el Wi-Fi de tu casa. Sin nube y sin cuenta.',
   play='Google Play', apple='App Store', soon='Próximamente', note_soon='Aún no está en las tiendas. Mientras tanto, DogNAS Client Lite ya accede a tu DogNAS en Android.',
   feats_h='Qué hace',
   feats=[('Emparejamiento por código QR', 'Apunta la cámara al código QR del perfil en el servidor e ingresa el PIN. Cada perfil tiene su espacio.'),
          ('Navega y organiza', 'Mira las carpetas; crea, renombra y borra archivos directamente en tu DogNAS.'),
          ('Sube y descarga', 'Envía fotos, videos y documentos al servidor y descárgalos de vuelta, con cola de transferencias.'),
          ('Solo en tu red', 'Los archivos quedan en tu Android DogNAS y viajan por el Wi-Fi de casa, cifrados (SSH/SFTP). Nada pasa por una nube.')],
   icons=['qr', 'devices', 'phone-free', 'no-cloud'],
   plans_h='Gratis, con el Pro en el servidor',
   plans='DogNAS Client es gratuito. Los límites y el Pro (compra única, sin suscripción) pertenecen al servidor DogNAS: en el plan Gratis, 64 GB, perfil Casa + 2 y 3 dispositivos; en el Pro, todo el dispositivo y transferencias que continúan con la app cerrada.',
   req_h='Requisitos', req='Un servidor DogNAS en la misma red Wi-Fi. Android y iPhone (iOS 15 o más reciente).',
   lite_h='¿Y Client Lite?', lite='DogNAS Client Lite sigue disponible en Google Play: es la app ligera, ideal para dispositivos más sencillos.',
   back='Volver al inicio', privacy='Política de privacidad'),
}
def btn(label, url, soon):
    return f'<a class="btn primary" href="{url}">{label}</a>' if url else f'<span class="btn soon">{label} · {soon}</span>'
for L, t in T.items():
    base = '../' if L == 'pt' else '../../'
    home = base if L == 'pt' else f'{base}{LANGS[L][1]}'
    path = LANGS[L][1] + 'client/'
    nav = ''.join(f'<a href="{base}{LANGS[l][1]}client/"{" class=on" if l == L else ""}>{NAMES[l]}</a>' for l in LANGS)
    ctas = btn(t['play'], STORE['play'], t['soon']) + btn(t['apple'], STORE['apple'], t['soon'])
    soon_note = '' if all(STORE.values()) else f'<p class="note">{t["note_soon"]}</p>'
    page = f'''<!doctype html>
<html lang="{LANGS[L][0]}">
<head>
{GA_TAG}<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t['title'])}</title>
<meta name="description" content="{html.escape(t['desc'])}">
<meta property="og:title" content="{html.escape(t['title'])}">
<meta property="og:description" content="{html.escape(t['desc'])}">
<meta property="og:image" content="https://dognas.app/assets/og-{L}.jpg">
<meta property="og:url" content="https://dognas.app/{path}">
<meta name="twitter:card" content="summary_large_image">
''' + ''.join(f'<link rel="alternate" hreflang="{LANGS[l][0]}" href="https://dognas.app/{LANGS[l][1]}client/">\n' for l in LANGS) + f'''<link rel="icon" href="{base}assets/icon.png">
<link rel="stylesheet" href="{base}assets/style.css?v={CSS_V}">
</head>
<body><div class="wrap">
<header class="top"><a class="brand" href="{home}"><img src="{base}assets/icon.png" alt=""><span>Dog<b>NAS</b></span></a><nav class="lang">{nav}</nav></header>
<section class="hero"><img class="logo" src="{base}assets/icon.png" alt="DogNAS Client"><h1>{t['h1']}</h1><p>{t['lead']}</p>
<div class="cta" style="justify-content:center">{ctas}</div>{soon_note}</section>
<h2>{t['feats_h']}</h2>
{cards(t['feats'], t['icons'])}
<h2>{t['plans_h']}</h2><div class="card wide"><p>{t['plans']}</p></div>
<h2>{t['req_h']}</h2><p>{t['req']}</p>
<h2>{t['lite_h']}</h2><p>{t['lite']}</p>
<p><a href="{home}">← {t['back']}</a></p>
<footer><span>© 2026 DogNAS</span><span><a href="{base}privacy/#{L}">{t['privacy']}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span></footer>
</div></body></html>
'''
    out = os.path.join(ROOT, path, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(page)
print('ok')

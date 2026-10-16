"""Privacy page (PT, EN, ES in one page at /privacy/). Run: python3 tools/build_privacy.py"""
import os, html, hashlib
ROOT = os.path.expanduser('~/workspace/dognas/dognas-site')
EMAIL = 'me.pauloleite.dev@gmail.com'
# Google Analytics 4 on the site only (2026-10-16) — the apps collect nothing; see the privacy page.
GA_TAG = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-HJDFSS9D15"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-HJDFSS9D15');
</script>
'''
# Cache busting (2026-10-16): Pages caches files for 10 min; a new page with a cached old
# stylesheet broke the layout. The CSS URL changes whenever its content does.
CSS_V = hashlib.sha1(open(os.path.join(ROOT, 'assets/style.css'), 'rb').read()).hexdigest()[:8]
LANGS = {'pt': ('pt-BR', '/', 'Português'), 'en': ('en', '/en/', 'English'), 'es': ('es', '/es/', 'Español')}

def page(lang, title, desc, body, base):
    nav = ''.join(f'<a href="{base}{LANGS[l][1].lstrip("/")}"{" class=on" if l == lang else ""}>{LANGS[l][2]}</a>' for l in LANGS)
    priv = {'pt': 'Política de privacidade', 'en': 'Privacy policy', 'es': 'Política de privacidad'}[lang]
    return f'''<!doctype html>
<html lang="{LANGS[lang][0]}">
<head>
{GA_TAG}<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="icon" href="{base}assets/icon.png">
<link rel="stylesheet" href="{base}assets/style.css?v={CSS_V}">
</head>
<body><div class="wrap">
<header class="top"><a class="brand" href="{base}{LANGS[lang][1].lstrip("/")}"><img src="{base}assets/icon.png" alt=""><span>Dog<b>NAS</b></span></a><nav class="lang">{nav}</nav></header>
{body}
<footer><span>© 2026 DogNAS</span><span><a href="{base}privacy/#{lang}">{priv}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span></footer>
</div></body></html>
'''

HOME = {
 'pt': ('DogNAS — Seus arquivos em casa', 'Transforme um Android num armazenamento particular na sua rede Wi-Fi, sem nuvem.',
        'Seus arquivos em casa.', 'O DogNAS transforma um Android que você já tem num armazenamento particular para a sua casa: seus arquivos ficam com você, na sua rede Wi-Fi, sem nuvem e sem mensalidade.',
        [('Sem nuvem', 'Os arquivos trafegam só entre os seus aparelhos, na sua rede, com conexão cifrada.'),
         ('Perfis para a família', 'Cada perfil tem seu próprio espaço e seu PIN.'),
         ('Conecte em segundos', 'Celulares com QR Code pelo DogNAS Lite; PCs e Macs por SFTP.'),
         ('Grátis para começar', '64 GB grátis. O DogNAS Pro libera tudo, com compra única.')],
        'Dois apps', [('DogNAS', 'O servidor: instale no Android que vai guardar os arquivos.'), ('DogNAS Lite', 'O app de acesso: instale no celular para ver, enviar e baixar os arquivos.')]),
 'en': ('DogNAS — Your files at home', 'Turn an Android into private storage on your Wi-Fi, with no cloud.',
        'Your files at home.', 'DogNAS turns an Android you already own into private storage for your home: your files stay with you, on your Wi-Fi, with no cloud and no monthly fee.',
        [('No cloud', 'Files travel only between your own devices, on your network, encrypted.'),
         ('Profiles for the family', 'Each profile has its own space and its own PIN.'),
         ('Connect in seconds', 'Phones with a QR Code through DogNAS Lite; PCs and Macs via SFTP.'),
         ('Free to start', '64 GB free. DogNAS Pro unlocks everything, as a one-time purchase.')],
        'Two apps', [('DogNAS', 'The server: install it on the Android that will keep your files.'), ('DogNAS Lite', 'The access app: install it on your phone to browse, upload and download.')]),
 'es': ('DogNAS — Tus archivos en casa', 'Convierte un Android en un almacenamiento privado en tu Wi-Fi, sin nube.',
        'Tus archivos en casa.', 'DogNAS convierte un Android que ya tienes en un almacenamiento privado para tu casa: tus archivos se quedan contigo, en tu Wi-Fi, sin nube y sin cuotas mensuales.',
        [('Sin nube', 'Los archivos viajan solo entre tus dispositivos, en tu red, cifrados.'),
         ('Perfiles para la familia', 'Cada perfil tiene su propio espacio y su PIN.'),
         ('Conecta en segundos', 'Teléfonos con código QR mediante DogNAS Lite; PC y Mac por SFTP.'),
         ('Gratis para empezar', '64 GB gratis. DogNAS Pro lo libera todo, con compra única.')],
        'Dos apps', [('DogNAS', 'El servidor: instálalo en el Android que guardará los archivos.'), ('DogNAS Lite', 'La app de acceso: instálala en tu teléfono para ver, subir y descargar archivos.')]),
}
POLICY = {
'pt': ('Política de privacidade', 'Última atualização: 16 de outubro de 2026', '''
<p>Esta política vale para os dois apps: <b>DogNAS</b> (o servidor, <code>com.dognas.server</code>) e <b>DogNAS Lite</b> (o app de acesso, <code>com.dognas.client.lite</code>).</p>
<h3>Resumo</h3><ul>
<li>Seus arquivos ficam <b>nos seus aparelhos</b>. Não existe servidor ou nuvem do DogNAS.</li>
<li>Os apps <b>não coletam, não enviam e não vendem</b> dados pessoais. Não há anúncios, contas, analytics nem SDKs de terceiros que coletem dados.</li>
<li>Toda transferência acontece <b>na sua rede local</b>, entre os seus aparelhos, cifrada (SSH/SFTP).</li></ul>
<h3>O que fica guardado, e onde</h3><p>Tudo abaixo fica <b>somente no aparelho</b> onde o app está instalado.</p>
<p><b>DogNAS (servidor)</b></p><ul>
<li>Os arquivos que você e seus dispositivos guardam na pasta escolhida (armazenamento interno, cartão SD ou HD USB).</li>
<li>Nomes dos perfis, PINs dos perfis e senhas dos dispositivos pareados — PINs e senhas apenas como <i>hash</i> (não é possível recuperá-los a partir do que fica salvo).</li>
<li>Nome informado por cada dispositivo pareado, data do pareamento e da última conexão, e um registro técnico de criação/remoção de credenciais (só os nomes de usuário internos), para você ver e revogar o acesso de cada dispositivo.</li>
<li>Estatísticas de uso do próprio servidor (velocidade, espaço, clientes conectados), mostradas na tela e não enviadas a lugar nenhum.</li></ul>
<p><b>DogNAS Lite (app de acesso)</b></p><ul>
<li>A lista dos DogNAS pareados (nome, endereço na rede local, porta, nome de usuário).</li>
<li>A senha de cada pareamento e a impressão digital da chave do servidor, <b>cifradas</b> com o Android Keystore, e o <i>hash</i> do PIN de cada perfil.</li>
<li>A fila de transferências e suas preferências.</li></ul>
<h3>Permissões e para que servem</h3><ul>
<li><b>Câmera</b> (DogNAS Lite): só para ler o QR Code de pareamento. As imagens são processadas no aparelho e não são guardadas nem enviadas.</li>
<li><b>Acesso a arquivos / armazenamento</b> (DogNAS): guardar e ler os arquivos na pasta que você escolher. O acesso a todos os arquivos é opcional e serve para gravar direto na pasta, mais rápido; o app só usa a pasta DogNAS.</li>
<li><b>Rede e Wi-Fi</b>: comunicação entre seus aparelhos na rede local e descoberta do servidor na mesma rede.</li>
<li><b>Notificações e serviço em primeiro plano</b>: manter o servidor e as transferências ativos e mostrar o andamento.</li>
<li><b>Iniciar após reiniciar</b> (DogNAS): ligar o servidor sozinho, se você ativar a opção.</li></ul>
<h3>Serviços do Google</h3><ul>
<li><b>Compras</b> (DogNAS Pro): são processadas pelo Google Play. O app só recebe a confirmação de que a compra existe; dados de pagamento ficam com o Google, conforme a <a href="https://policies.google.com/privacy">política de privacidade do Google</a>.</li>
<li><b>Estabilidade</b>: o Google Play pode coletar relatórios de falhas e de desempenho do Android (Android Vitals), conforme as configurações de "uso e diagnóstico" do seu aparelho. Os apps não incluem nenhuma ferramenta própria de telemetria.</li></ul>
<h3>Seus controles</h3><ul>
<li>Revogue o acesso de um dispositivo no DogNAS (Perfis → Dispositivos autorizados) ou remova um DogNAS no DogNAS Lite (pede o PIN do perfil).</li>
<li>Desinstalar um app apaga os dados dele no aparelho. Os seus arquivos na pasta DogNAS <b>não</b> são apagados — eles são seus.</li></ul>
<h3>Este site (dognas.app)</h3><p>O site usa o <b>Google Analytics</b> para contar visitas e entender quais páginas são lidas (páginas vistas, país aproximado, tipo de aparelho e navegador). Isso vale só para o site — os apps não usam o Google Analytics nem enviam dados. Saiba mais na <a href="https://policies.google.com/technologies/partner-sites">página do Google sobre dados de sites parceiros</a>.</p>
<h3>Crianças</h3><p>Os apps não são direcionados a crianças e não coletam dados de ninguém.</p>
<h3>Mudanças e contato</h3><p>Se esta política mudar, a nova versão será publicada neste mesmo endereço, com a data acima atualizada. Dúvidas: <a href="mailto:EMAIL">EMAIL</a>.</p>'''),
'en': ('Privacy policy', 'Last updated: October 16, 2026', '''
<p>Applies to both apps: <b>DogNAS</b> (the server, <code>com.dognas.server</code>) and <b>DogNAS Lite</b> (the access app, <code>com.dognas.client.lite</code>).</p>
<h3>Summary</h3><ul>
<li>Your files stay <b>on your own devices</b>. There is no DogNAS server or cloud.</li>
<li>The apps <b>do not collect, send or sell</b> personal data. No ads, accounts, analytics or third-party data-collecting SDKs.</li>
<li>Transfers happen <b>on your local network</b>, between your devices, encrypted (SSH/SFTP).</li></ul>
<h3>What is stored, and where</h3><p>Everything below stays <b>only on the device</b> where the app is installed.</p>
<p><b>DogNAS (server)</b></p><ul>
<li>The files you and your devices keep in the folder you pick (internal storage, SD card or USB drive).</li>
<li>Profile names, profile PINs and paired-device passwords — PINs and passwords as <i>hashes</i> only (they can't be recovered from what is stored).</li>
<li>The name each paired device reports, its pairing and last-connection dates, and a technical log of credential creation/removal (internal user names only), so you can see and revoke each device's access.</li>
<li>The server's own usage statistics (speed, space, connected clients), shown on screen and sent nowhere.</li></ul>
<p><b>DogNAS Lite (access app)</b></p><ul>
<li>The list of paired DogNAS (name, local network address, port, user name).</li>
<li>Each pairing's password and the server key fingerprint, <b>encrypted</b> with the Android Keystore, and each profile PIN's <i>hash</i>.</li>
<li>The transfer queue and your settings.</li></ul>
<h3>Permissions and what they are for</h3><ul>
<li><b>Camera</b> (DogNAS Lite): only to read the pairing QR Code. Frames are processed on the device, never stored or sent.</li>
<li><b>Files / storage</b> (DogNAS): keep and read files in the folder you pick. All Files Access is optional and only used to write directly to the folder, faster; the app only uses the DogNAS folder.</li>
<li><b>Network and Wi-Fi</b>: communication between your devices on the local network and finding the server on the same network.</li>
<li><b>Notifications and foreground service</b>: keep the server and transfers running and show progress.</li>
<li><b>Start after reboot</b> (DogNAS): start the server by itself, if you turn it on.</li></ul>
<h3>Google services</h3><ul>
<li><b>Purchases</b> (DogNAS Pro) are processed by Google Play. The app only receives the confirmation that a purchase exists; payment data stays with Google, under the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>.</li>
<li><b>Stability</b>: Google Play may collect Android crash and performance reports (Android Vitals) according to your device's usage &amp; diagnostics settings. The apps include no telemetry of their own.</li></ul>
<h3>Your controls</h3><ul>
<li>Revoke a device in DogNAS (Profiles → Authorized devices) or remove a DogNAS in DogNAS Lite (asks for the profile PIN).</li>
<li>Uninstalling an app deletes its data on the device. Your files in the DogNAS folder are <b>not</b> deleted — they are yours.</li></ul>
<h3>This website (dognas.app)</h3><p>The website uses <b>Google Analytics</b> to count visits and see which pages are read (page views, approximate country, device type and browser). This applies to the website only — the apps don't use Google Analytics and send no data. Learn more on <a href="https://policies.google.com/technologies/partner-sites">Google's page about data from partner sites</a>.</p>
<h3>Children</h3><p>The apps are not directed to children and collect no data from anyone.</p>
<h3>Changes and contact</h3><p>If this policy changes, the new version will be published at this same address with an updated date. Questions: <a href="mailto:EMAIL">EMAIL</a>.</p>'''),
'es': ('Política de privacidad', 'Última actualización: 16 de octubre de 2026', '''
<p>Se aplica a las dos apps: <b>DogNAS</b> (el servidor, <code>com.dognas.server</code>) y <b>DogNAS Lite</b> (la app de acceso, <code>com.dognas.client.lite</code>).</p>
<h3>Resumen</h3><ul>
<li>Tus archivos se quedan <b>en tus dispositivos</b>. No existe un servidor ni una nube de DogNAS.</li>
<li>Las apps <b>no recopilan, no envían ni venden</b> datos personales. Sin anuncios, cuentas, analítica ni SDK de terceros que recopilen datos.</li>
<li>Las transferencias ocurren <b>en tu red local</b>, entre tus dispositivos, cifradas (SSH/SFTP).</li></ul>
<h3>Qué se guarda y dónde</h3><p>Todo lo siguiente se queda <b>solo en el dispositivo</b> donde está instalada la app.</p>
<p><b>DogNAS (servidor)</b></p><ul>
<li>Los archivos que tú y tus dispositivos guardan en la carpeta elegida (almacenamiento interno, tarjeta SD o disco USB).</li>
<li>Nombres de los perfiles, PIN de los perfiles y contraseñas de los dispositivos vinculados — PIN y contraseñas solo como <i>hash</i> (no se pueden recuperar a partir de lo guardado).</li>
<li>El nombre que informa cada dispositivo vinculado, las fechas de vinculación y de última conexión, y un registro técnico de creación/eliminación de credenciales (solo los nombres de usuario internos), para que veas y revoques el acceso de cada dispositivo.</li>
<li>Estadísticas de uso del propio servidor (velocidad, espacio, clientes conectados), mostradas en pantalla y no enviadas a ningún lugar.</li></ul>
<p><b>DogNAS Lite (app de acceso)</b></p><ul>
<li>La lista de DogNAS vinculados (nombre, dirección en la red local, puerto, nombre de usuario).</li>
<li>La contraseña de cada vinculación y la huella de la clave del servidor, <b>cifradas</b> con el Android Keystore, y el <i>hash</i> del PIN de cada perfil.</li>
<li>La cola de transferencias y tus preferencias.</li></ul>
<h3>Permisos y para qué sirven</h3><ul>
<li><b>Cámara</b> (DogNAS Lite): solo para leer el código QR de vinculación. Las imágenes se procesan en el dispositivo y no se guardan ni se envían.</li>
<li><b>Archivos / almacenamiento</b> (DogNAS): guardar y leer archivos en la carpeta que elijas. El acceso a todos los archivos es opcional y sirve para escribir directamente en la carpeta, más rápido; la app solo usa la carpeta DogNAS.</li>
<li><b>Red y Wi-Fi</b>: comunicación entre tus dispositivos en la red local y localización del servidor en la misma red.</li>
<li><b>Notificaciones y servicio en primer plano</b>: mantener activos el servidor y las transferencias y mostrar el progreso.</li>
<li><b>Iniciar tras reiniciar</b> (DogNAS): encender el servidor solo, si activas la opción.</li></ul>
<h3>Servicios de Google</h3><ul>
<li><b>Compras</b> (DogNAS Pro): las procesa Google Play. La app solo recibe la confirmación de que la compra existe; los datos de pago se quedan con Google, según la <a href="https://policies.google.com/privacy">política de privacidad de Google</a>.</li>
<li><b>Estabilidad</b>: Google Play puede recopilar informes de fallos y rendimiento de Android (Android Vitals), según la configuración de "uso y diagnóstico" de tu dispositivo. Las apps no incluyen ninguna herramienta propia de telemetría.</li></ul>
<h3>Tus controles</h3><ul>
<li>Revoca el acceso de un dispositivo en DogNAS (Perfiles → Dispositivos autorizados) o elimina un DogNAS en DogNAS Lite (pide el PIN del perfil).</li>
<li>Desinstalar una app borra sus datos en el dispositivo. Tus archivos en la carpeta DogNAS <b>no</b> se borran — son tuyos.</li></ul>
<h3>Este sitio (dognas.app)</h3><p>El sitio usa <b>Google Analytics</b> para contar visitas y saber qué páginas se leen (páginas vistas, país aproximado, tipo de dispositivo y navegador). Esto se aplica solo al sitio: las apps no usan Google Analytics ni envían datos. Más información en la <a href="https://policies.google.com/technologies/partner-sites">página de Google sobre datos de sitios asociados</a>.</p>
<h3>Menores</h3><p>Las apps no están dirigidas a menores y no recopilan datos de nadie.</p>
<h3>Cambios y contacto</h3><p>Si esta política cambia, la nueva versión se publicará en esta misma dirección, con la fecha actualizada. Dudas: <a href="mailto:EMAIL">EMAIL</a>.</p>'''),
}
sections = ''.join(f'<section class="legal" id="{l}"><h2>{t}</h2><p class="meta">{m}</p>{b.replace("EMAIL", EMAIL)}</section>' for l, (t, m, b) in POLICY.items())
jump = '<p class="meta"><a href="#pt">Português</a> · <a href="#en">English</a> · <a href="#es">Español</a></p>'
open(os.path.join(ROOT, 'privacy/index.html'), 'w').write(page('pt', 'DogNAS — Política de privacidade / Privacy policy', 'Política de privacidade do DogNAS e do DogNAS Lite.', '<h1 style="margin-top:32px">Política de privacidade · Privacy policy · Política de privacidad</h1>' + jump + sections, '../'))
print('ok')

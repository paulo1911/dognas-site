"""Landing pages (pt at /, en at /en/, es at /es/) for two audiences: home users and tech /
smart-home users. Run: python3 tools/build_home.py (screenshots live in assets/shots/<lang>/)."""
import os, html, hashlib, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo
from home_copy import NEW
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL = 'me.pauloleite.dev@gmail.com'
# Google Analytics 4 on the site only — the apps collect nothing; see the privacy page.
GA_TAG = '''<script>
// Google Analytics 4 runs only after the visitor accepts (nothing is loaded before). Site only: the apps collect nothing.
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('consent', 'default', {analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied'});
(function () {
  var KEY = 'dognas_consent', ID = 'G-HJDFSS9D15', L = (document.documentElement.lang || 'pt').slice(0, 2);
  var TXT = {
    pt: ['Usamos o Google Analytics, só neste site, para entender quais páginas e botões ajudam as pessoas. Os apps não coletam nada.', 'Aceitar', 'Recusar', 'Saiba mais', 'Preferências de cookies'],
    en: ['We use Google Analytics, on this website only, to learn which pages and buttons help people. The apps collect nothing.', 'Accept', 'Decline', 'Learn more', 'Cookie preferences'],
    es: ['Usamos Google Analytics, solo en este sitio, para saber qué páginas y botones ayudan a las personas. Las apps no recogen nada.', 'Aceptar', 'Rechazar', 'Más información', 'Preferencias de cookies']
  }[L] || [];
  function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function write(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function load() {
    if (window.__dnGA) return; window.__dnGA = 1;
    gtag('consent', 'update', {analytics_storage: 'granted'});
    var s = document.createElement('script'); s.async = 1; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + ID; document.head.appendChild(s);
    gtag('js', new Date()); gtag('config', ID);
  }
  // One shape for every click and view so GA4 can rank CTAs: cta_id (position on the page), cta_text, cta_target, lang, page_depth.
  function ctaParams(a) {
    var h = document.documentElement, depth = Math.round(100 * (window.scrollY + window.innerHeight) / Math.max(h.scrollHeight, 1));
    return {cta_id: a.getAttribute('data-loc') || '', cta_text: (a.textContent || '').trim().slice(0, 60), cta_target: (a.getAttribute('data-ev') || '').replace(/_(store_)?click$/, ''), lang: L, page_depth: Math.min(depth, 100)};
  }
  window.dnEvent = function (name, params) { if (window.__dnGA) gtag('event', name, params || {}); };
  function banner() {
    var old = document.getElementById('dn-consent'); if (old) old.remove();
    var d = document.createElement('div'); d.id = 'dn-consent'; d.setAttribute('role', 'dialog'); d.setAttribute('aria-label', 'Cookies');
    d.innerHTML = '<p>' + TXT[0] + ' <a href="/privacy/#' + L + '">' + TXT[3] + '</a></p><div><button type="button" data-v="granted">' + TXT[1] + '</button><button type="button" data-v="denied">' + TXT[2] + '</button></div>';
    d.addEventListener('click', function (e) { var v = e.target.getAttribute && e.target.getAttribute('data-v'); if (!v) return; write(v); d.remove(); if (v === 'granted') { load(); window.dnEvent('page_view'); } });
    document.body.appendChild(d);
  }
  if (read() === 'granted') load();
  document.addEventListener('DOMContentLoaded', function () {
    if (!read()) banner();
    document.addEventListener('click', function (e) {
      var prefs = e.target.closest && e.target.closest('[data-cookie-prefs]'); if (prefs) { e.preventDefault(); banner(); return; }
      var a = e.target.closest && e.target.closest('[data-ev]'); if (a) window.dnEvent(a.getAttribute('data-ev'), ctaParams(a));
    });
    // cta_view = a CTA was actually on screen (>= 60 %), once per id and page view: clicks / views = that CTA's click rate.
    if ('IntersectionObserver' in window) {
      var seen = {}, vio = new IntersectionObserver(function (es) { es.forEach(function (x) { var a = x.target, id = a.getAttribute('data-loc'); if (x.isIntersecting && !seen[id]) { seen[id] = 1; window.dnEvent('cta_view', ctaParams(a)); } }); }, {threshold: .6});
      document.querySelectorAll('a[data-loc][data-ev$="_click"]:not([data-ev=lang_switch]):not([data-ev=support_click]):not([data-ev=requirements_click])').forEach(function (n) { vio.observe(n); });
    }
    var plans = document.getElementById('planos');
    if (plans && 'IntersectionObserver' in window) { var io = new IntersectionObserver(function (en) { if (en[0].isIntersecting) { window.dnEvent('pro_view', {lang: L}); io.disconnect(); } }, {threshold: .4}); io.observe(plans); }
    document.addEventListener('toggle', function (e) { var d = e.target; if (d && d.tagName === 'DETAILS' && d.open) window.dnEvent('faq_open', {question: Array.prototype.indexOf.call(d.parentNode.children, d), lang: L}); }, true);
    document.querySelectorAll('[data-cookie-prefs]').forEach(function (n) { if (TXT[4]) n.textContent = TXT[4]; });
  });
})();
</script>
'''
# Pages caches files for 10 min: the CSS URL changes whenever its content does, so a new page
# never renders with a cached old stylesheet.
CSS_V = hashlib.sha1(open(os.path.join(ROOT, 'assets/style.css'), 'rb').read()).hexdigest()[:8]
LANGS = {'pt': ('pt-BR', ''), 'en': ('en', 'en/'), 'es': ('es', 'es/')}
NAMES = {'pt': 'Português', 'en': 'English', 'es': 'Español'}
# Inline SVG icons (24×24, stroke = currentColor), one per feature card and audience.
ICONS = {
 'phone-free': '<rect x="6" y="2" width="12" height="20" rx="2.5"/><path d="M10 18.5h4"/><path d="m9 10 2 2 4-4"/>',
 'people': '<circle cx="9" cy="8" r="3"/><path d="M3.5 19a5.5 5.5 0 0 1 11 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.2A4.5 4.5 0 0 1 21 18.5"/>',
 'qr': '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3h-3zM20 14v.01M14 20h.01M17 20h4v-3"/>',
 'no-cloud': '<path d="M7 18h10a4 4 0 0 0 .7-7.94A6 6 0 0 0 6.2 9.1 4.5 4.5 0 0 0 7 18z"/><path d="m3 3 18 18"/>',
 'server': '<rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><path d="M7 7.5h.01M7 16.5h.01M11 7.5h6M11 16.5h6"/>',
 'smart-home': '<path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><path d="M9.5 15.5a3.5 3.5 0 0 1 5 0M8 13.2a6 6 0 0 1 8 0"/><path d="M12 18h.01"/>',
 'shield': '<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.4 7.5 9.5 4.3-1.1 7.5-4.9 7.5-9.5V6z"/><path d="m8.5 12 2.5 2.5 4.5-4.5"/>',
 'power': '<path d="M12 3v8"/><path d="M6.6 6.6a8 8 0 1 0 10.8 0"/>',
 'ssd': '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M7 10h6M7 14h3"/><path d="M17 10v4"/>',
 'hdd': '<rect x="4" y="3" width="16" height="18" rx="2"/><circle cx="12" cy="10" r="4"/><circle cx="12" cy="10" r=".6"/><path d="M8 17.5h8"/>',
 'sd': '<path d="M7 3h7l4 4v13a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z"/><path d="M10 3v4M13 3v4"/><path d="M9 14h6"/>',
 'devices': '<rect x="2" y="6" width="7" height="13" rx="1.5"/><rect x="15" y="6" width="7" height="13" rx="1.5"/><path d="M9 12.5h6"/><path d="M12 9v7"/>',
 'briefcase': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M3 13h18"/><path d="M11 13v2h2v-2"/>',
 'home': '<path d="M3 11 12 4l9 7"/><path d="M5 10v10h5v-6h4v6h5V10"/>',
 'terminal': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="m7 9 3 3-3 3M12.5 15H17"/>',
}
def icon(k): return f'<span class="ico"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[k]}</svg></span>'
PLAY = {'server': 'https://play.google.com/store/apps/details?id=com.dognas.server',
        'lite': 'https://play.google.com/store/apps/details?id=com.dognas.client.lite'}
# DogNAS Client (Flutter) Play URL: fill when it is published — the secondary CTA then points to it and the Lite becomes the "lightweight alternative".
CLIENT_PLAY = ''
def play(app, loc):
    # `referrer` lets Play Console attribute store visits to this site (the apps themselves collect nothing).
    return f"{PLAY[app]}&referrer=utm_source%3Ddognas.app%26utm_medium%3Dwebsite%26utm_campaign%3D{loc}"
T = {
 'pt': dict(title='DogNAS — Seu celular antigo. Seu armazenamento particular.', desc='Transforme um celular ou tablet Android em armazenamento particular pelo Wi-Fi: fotos, vídeos e documentos em casa. Sem nuvem, sem mensalidade e sem comprar um NAS.',
   h1='Seu celular antigo. Seu armazenamento particular.', lead='Transforme um celular ou tablet Android compatível em um espaço para guardar e acessar fotos, vídeos e documentos pelo Wi-Fi. Sem nuvem, sem mensalidade e sem precisar comprar um NAS.',
   points=['Use um Android que você já tem', 'Conecte outros celulares por QR Code', 'Comece grátis, sem assinatura'], cta='Baixar o DogNAS grátis',
   micro='Confira os requisitos de compatibilidade antes de instalar.', sub='Já tem o servidor? Baixe o Client Lite', sub_client='Já tem o servidor? Baixe o DogNAS Client', lite_alt='Prefere algo mais leve? Use o Client Lite',
   important='Seus arquivos ficam no armazenamento configurado no seu dispositivo servidor. O acesso depende da configuração de rede e das credenciais do DogNAS. Para arquivos importantes, mantenha uma cópia de backup independente.', important_h='Importante', cookies='Preferências de cookies',
   soon='Em breve na Google Play', get_server='Baixar o DogNAS (servidor)', get_lite='Baixar o DogNAS Client Lite', alt1='Servidor DogNAS online', alt2='Arquivos no DogNAS Client Lite',
   who='Para quem é o DogNAS?',
   ben_kicker='Benefícios', ben_h2='Os problemas que o DogNAS resolve', ben_lead='Em casa, no home office ou na casa inteligente, o DogNAS acaba com dores do dia a dia usando um Android que você já tem.',
   ben=[('home', 'Uso doméstico', [
          ('Celular sempre cheio, sem espaço para fotos e vídeos.', 'Envie fotos e vídeos para o DogNAS pelo Wi-Fi e libere espaço no celular. Mantenha também uma cópia independente do que é importante.'),
          ('Mensalidade de nuvem que só aumenta.', 'Use o Android parado na gaveta: o Grátis guarda até 64 GB e o Pro é compra única, sem assinatura.'),
          ('Fotos da família espalhadas e guardadas em servidores de terceiros.', 'Tudo num lugar só, dentro de casa: um perfil e um PIN para cada pessoa, sem nuvem e sem conta.')]),
        ('briefcase', 'Home office', [
          ('Arquivos de trabalho presos em pendrives e em e-mails para si mesmo.', 'Abra do PC, do Mac, do tablet ou do celular pela rede: FileZilla, WinSCP, Cyberduck ou DogNAS Client Lite.'),
          ('NAS tradicional caro e difícil de configurar.', 'Instale um app, toque em Iniciar e pareie com QR Code e PIN. Sem mexer no roteador.'),
          ('Documentos de clientes em nuvem pública.', 'Ficam na sua rede, cifrados no caminho (SSH/SFTP), com uma credencial por aparelho que você revoga quando quiser.')]),
        ('smart-home', 'Smart home', [
          ('Gravações das câmeras presas à nuvem paga do fabricante.', 'Câmeras e NVRs com envio por SFTP gravam direto no DogNAS, na sua rede.'),
          ('Automações sem um lugar para guardar arquivos.', 'Home Assistant, Node-RED, rclone e scripts enviam e buscam arquivos por SFTP.'),
          ('Servidor que para quando falta luz.', 'O celular tem bateria própria e, no Pro, o DogNAS pode iniciar sozinho depois de reiniciar (depende do aparelho e das permissões do Android).')])],
   aud=[('casa', 'Para sua casa', 'Seu Android antigo vira o armazenamento da família, pelo Wi-Fi. Sem complicação.', 'Ver como funciona'),
        ('tech', 'Para quem é de tecnologia', 'Um servidor SFTP sempre ligado: NAS em casa ou no escritório, smart home e IoT.', 'Ver detalhes técnicos')],
   home_kicker='Para sua casa', home_h2='Seu Android antigo como armazenamento da casa, pelo Wi-Fi',
   home_lead='Aquele celular parado na gaveta passa a guardar as fotos, os vídeos e os documentos de todo mundo. Você acessa pelo celular, de qualquer cômodo, sem cabos e sem pagar nuvem.',
   home_feats=[('Libere espaço no seu celular!', 'Use o DogNAS Client Lite para mandar fotos e vídeos do seu celular para o DogNAS, que guarda tudo no seu perfil. Antes de apagar do celular, confira se os arquivos estão no DogNAS e mantenha uma cópia independente do que é importante.'),
               ('Um espaço para cada pessoa', 'Cada perfil tem seu PIN e suas pastas. Ninguém vê os arquivos dos outros.'),
               ('Fácil de conectar', 'Use o DogNAS Client Lite para se conectar ao seu servidor DogNAS: aponte a câmera para o QR Code, digite o PIN e pronto.'),
               ('Sem nuvem e sem mensalidade', 'Os arquivos ficam no armazenamento do seu Android DogNAS, acessíveis pelo Wi-Fi da sua casa. Nada de conta, anúncios ou cobrança todo mês. Use todo o espaço do aparelho: 32, 64, 128, 256 GB e até mais (acima de 64 GB com o DogNAS Pro).')],
   how='Como funciona',
   steps=[('Ligue o servidor', 'Instale o DogNAS no Android que vai guardar os arquivos — no aparelho, num cartão SD ou num HD USB — e toque em Iniciar.', 'server-status'),
          ('Conecte seu celular', 'Gere o QR Code de um perfil e leia com o DogNAS Client Lite. Cada perfil tem seu PIN e seu espaço.', 'server-qr'),
          ('Use seus arquivos', 'Navegue, envie e baixe pelo Wi-Fi de casa. PCs e Macs conectam por SFTP.', 'lite-files')],
   tech_kicker='Para tech, smart home e escritório', tech_h2='Um servidor SFTP no Android, sempre ligado',
   tech_lead='Um NAS leve para casa ou escritório: qualquer dispositivo, script ou automação que fale SFTP envia e busca arquivos pela rede Wi-Fi.',
   tech_feats=[('NAS em casa ou no escritório', 'Pastas por perfil, acessadas de PC, Mac e Linux com FileZilla, WinSCP, Cyberduck, rclone ou o sftp do OpenSSH.'),
               ('Smart home e IoT', 'Receba arquivos de câmeras e NVRs com envio por SFTP, backups de outros servidores e scripts de automação (Home Assistant, Node-RED, cron).'),
               ('Cifrado no caminho', 'SSH-2 com AES-GCM ou ChaCha20, chave do servidor fixada no pareamento e uma credencial por dispositivo, revogável a qualquer hora.'),
               ('Pensado para ficar ligado', 'Grava na memória interna, num cartão SD ou num HD ou pendrive USB. No Pro, pode iniciar sozinho depois de reiniciar. Alguns fabricantes limitam apps em segundo plano: veja os requisitos.')],
   prod=('Produtividade no escritório', 'Ideal para quem trabalha com fotos, vídeos e documentos e precisa organizar tudo: os arquivos ficam acessíveis no PC, no tablet e no smartphone, sem pendrives nem cabos. O DogNAS é toda a facilidade pelo seu Wi-Fi.'),
   specs_h3='Especificações',
   specs=[('Protocolo', 'SFTP sobre SSH-2'), ('Autenticação', 'Usuário e senha — uma credencial por dispositivo, revogável'),
          ('Armazenamento', 'Memória interna, cartão SD, HD ou pendrive USB'), ('Clientes', 'DogNAS Client Lite, FileZilla, WinSCP, Cyberduck, rclone, OpenSSH e scripts'),
          ('Requisitos', 'Android 7.0 ou mais recente, na mesma rede')],
   more_kicker='Para todos', more_h2='Mais espaço para o seu DogNAS', more_lead='Quer mais espaço? Ligue um SSD externo ou até aquele HD que você tirou do notebook antigo. Cada disco é um armazenamento independente: o DogNAS não junta vários discos num único volume.',
   more_feats=[('SSD externo', 'Ligue um SSD USB e ganhe espaço e velocidade para guardar tudo da casa.'), ('O HD do notebook antigo', 'Coloque o HD trocado do notebook numa case USB e dê uma nova vida a ele como armazenamento da casa.'), ('Cartão SD ou pendrive', 'O jeito mais simples de aumentar o espaço do celular que virou servidor.'), ('Vários DogNAS na casa', 'Tem mais de um Android parado? Cada um pode ser um DogNAS; o DogNAS Client Lite mostra todos em “Meus armazenamentos”.')],
   more_note='Discos USB precisam de um celular com USB OTG. HDs mecânicos podem pedir mais energia do que o celular fornece: nesse caso, use um hub USB com fonte. No plano Grátis, o DogNAS gerencia até 64 GB; no Pro, o disco inteiro. Um único disco pode falhar: mantenha uma cópia independente dos arquivos importantes.',
   tech_photo='O Monitor do servidor: velocidade, clientes conectados e sessões TCP em tempo real.',
   more_photo='Servidor com um HD externo numa dock USB, acessado pelo celular.',
   watch='Acompanhe tudo', cap1='Transferências e clientes no servidor', cap2='Fila de transferências no celular',
   plans='Grátis para começar', planhead=('', 'Grátis', 'Pro'),
   rows=[('Armazenamento', '64 GB', 'Todo o aparelho'), ('Perfis', 'Casa + 2', 'Ilimitados'), ('Dispositivos pareados', '3', 'Ilimitados'), ('Performance', 'Boa', 'Máxima otimizada'), ('Transferências no app cliente, com o app fechado', 'Pausam', 'Continuam'), ('Após reiniciar', 'Toque para iniciar', 'Inicia sozinho')],
   plannote='DogNAS Pro: compra única, sem assinatura. O DogNAS Client Lite é sempre gratuito.',
   apps='Os apps', app1='O servidor: instale no Android que vai guardar os arquivos.', app2='O app de acesso: instale no celular para ver, enviar e baixar os arquivos.', app3='Novo: o app completo para Android e iPhone, em breve.', privacy='Política de privacidade'),
 'en': dict(title='DogNAS — Your old phone. Your private storage.', desc='Turn an Android phone or tablet into private storage over Wi-Fi: photos, videos and documents at home. No cloud, no monthly fee, and no NAS to buy.',
   h1='Your old phone. Your private storage.', lead='Turn a compatible Android phone or tablet into a space to keep and reach photos, videos and documents over Wi-Fi. No cloud, no monthly fee, and no need to buy a NAS.',
   points=['Use an Android you already own', 'Connect other phones with a QR Code', 'Start free, no subscription'], cta='Download DogNAS free',
   micro='Check the compatibility requirements before installing.', sub='Already have the server? Get DogNAS Client Lite', sub_client='Already have the server? Get DogNAS Client', lite_alt='Want something lighter? Use Client Lite',
   important='Your files stay in the storage set up on your server device. Access depends on your network setup and your DogNAS credentials. For important files, keep an independent backup copy.', important_h='Important', cookies='Cookie preferences',
   soon='Coming soon to Google Play', get_server='Get DogNAS (server)', get_lite='Get DogNAS Client Lite', alt1='DogNAS server online', alt2='Files in DogNAS Client Lite',
   who='Who is DogNAS for?',
   ben_kicker='Benefits', ben_h2='The problems DogNAS solves', ben_lead='At home, in your home office or in your smart home, DogNAS ends everyday headaches with an Android you already own.',
   ben=[('home', 'Home use', [
          ('Your phone is always full, with no room for photos and videos.', 'Send photos and videos to DogNAS over Wi-Fi and free up space on your phone. Keep an independent copy of what matters, too.'),
          ('A cloud subscription that keeps going up.', 'Use the Android sitting in a drawer: Free keeps up to 64 GB and Pro is a one-time purchase, no subscription.'),
          ('Family photos scattered around and kept on someone else’s servers.', 'Everything in one place, inside your home: a profile and a PIN for each person, no cloud and no account.')]),
        ('briefcase', 'Home office', [
          ('Work files stuck on USB sticks and in emails to yourself.', 'Open them from your PC, Mac, tablet or phone over the network: FileZilla, WinSCP, Cyberduck or DogNAS Client Lite.'),
          ('A traditional NAS is expensive and hard to set up.', 'Install an app, tap Start and pair with a QR Code and a PIN. No router settings.'),
          ('Client documents on a public cloud.', 'They stay on your network, encrypted in transit (SSH/SFTP), with one credential per device that you can revoke at any time.')]),
        ('smart-home', 'Smart home', [
          ('Camera recordings locked into the maker’s paid cloud.', 'Cameras and NVRs that upload over SFTP record straight to DogNAS, on your network.'),
          ('Automations with nowhere to keep files.', 'Home Assistant, Node-RED, rclone and scripts send and fetch files over SFTP.'),
          ('A server that stops when the power goes out.', 'The phone has its own battery and, on Pro, DogNAS can start by itself after a reboot (it depends on the device and Android permissions).')])],
   aud=[('casa', 'For your home', 'Your old Android becomes the family’s storage, over Wi-Fi. No hassle.', 'See how it works'),
        ('tech', 'For tech people', 'An always-on SFTP server: a NAS for home or office, smart home and IoT.', 'See the tech details')],
   home_kicker='For your home', home_h2='Your old Android as home storage, over Wi-Fi',
   home_lead='That phone sitting in a drawer starts keeping everyone’s photos, videos and documents. You reach them from your phone, in any room, with no cables and no cloud bill.',
   home_feats=[('Free up space on your phone!', 'Use DogNAS Client Lite to send photos and videos from your phone to DogNAS, which keeps them in your profile. Before deleting them from your phone, check that they are in DogNAS and keep an independent copy of what matters.'),
               ('A space for each person', 'Each profile has its own PIN and folders. Nobody sees anyone else’s files.'),
               ('Easy to connect', 'Use DogNAS Client Lite to connect to your DogNAS server: point the camera at the QR Code, type the PIN, done.'),
               ('No cloud, no monthly fee', 'Your files stay in the storage of your DogNAS Android, reachable over your home Wi-Fi. No account, no ads, no monthly charge. Use all of the device’s space: 32, 64, 128, 256 GB and beyond (over 64 GB with DogNAS Pro).')],
   how='How it works',
   steps=[('Start the server', 'Install DogNAS on the Android that will keep your files — on the device, an SD card or a USB drive — and tap Start.', 'server-status'),
          ('Connect your phone', "Generate a profile's QR Code and scan it with DogNAS Client Lite. Each profile has its own PIN and space.", 'server-qr'),
          ('Use your files', 'Browse, upload and download over your home Wi-Fi. PCs and Macs connect via SFTP.', 'lite-files')],
   tech_kicker='For tech, smart home and office', tech_h2='An always-on SFTP server on Android',
   tech_lead='A lightweight NAS for home or office: any device, script or automation that speaks SFTP can send and fetch files over Wi-Fi.',
   tech_feats=[('NAS for home or office', 'Per-profile folders, reached from PC, Mac and Linux with FileZilla, WinSCP, Cyberduck, rclone or OpenSSH’s sftp.'),
               ('Smart home and IoT', 'Receive files from cameras and NVRs that upload over SFTP, backups from other servers, and automation scripts (Home Assistant, Node-RED, cron).'),
               ('Encrypted in transit', 'SSH-2 with AES-GCM or ChaCha20, the server key pinned at pairing, and one credential per device, revocable at any time.'),
               ('Made to stay on', 'Stores to internal memory, an SD card or a USB drive. With Pro it can start by itself after a reboot. Some makers limit background apps: see the requirements.')],
   prod=('Productivity at the office', 'Ideal for anyone who works with photos, videos and documents and needs to keep it all organized: your files stay reachable from PC, tablet and smartphone, with no USB sticks or cables. DogNAS makes it easy, over your Wi-Fi.'),
   specs_h3='Specifications',
   specs=[('Protocol', 'SFTP over SSH-2'), ('Authentication', 'Username and password — one credential per device, revocable'),
          ('Storage', 'Internal memory, SD card, USB drive'), ('Clients', 'DogNAS Client Lite, FileZilla, WinSCP, Cyberduck, rclone, OpenSSH and scripts'),
          ('Requirements', 'Android 7.0 or newer, on the same network')],
   more_kicker='For everyone', more_h2='More room for your DogNAS', more_lead='Want more room? Plug in an external SSD, or even the hard drive you took out of your old laptop. Each drive is an independent storage: DogNAS does not combine several drives into one volume.',
   more_feats=[('External SSD', 'Plug in a USB SSD for room and speed to keep everything at home.'), ('Your old laptop’s hard drive', 'Put the drive you swapped out of your laptop in a USB enclosure and give it a new life as home storage.'), ('SD card or USB stick', 'The simplest way to add space to the phone that became a server.'), ('Several DogNAS at home', 'More than one Android in a drawer? Each can be a DogNAS; DogNAS Client Lite shows them all in “My storages”.')],
   more_note='USB drives need a phone with USB OTG. Spinning hard drives may need more power than the phone provides — use a powered USB hub in that case. On the Free plan DogNAS manages up to 64 GB; with Pro, the whole drive. A single drive can fail: keep an independent copy of your important files.',
   tech_photo='The server Monitor: speed, connected clients and TCP sessions in real time.',
   more_photo='A server with an external drive in a USB dock, reached from the phone.',
   watch='Follow everything', cap1='Transfers and clients on the server', cap2='Transfer queue on your phone',
   plans='Free to start', planhead=('', 'Free', 'Pro'),
   rows=[('Storage', '64 GB', 'All of it'), ('Profiles', 'Home + 2', 'Unlimited'), ('Paired devices', '3', 'Unlimited'), ('Performance', 'Good', 'Maximum, optimized'), ('Client app transfers, with the app closed', 'Pause', 'Keep going'), ('After a reboot', 'Tap to start', 'Starts by itself')],
   plannote='DogNAS Pro: one-time purchase, no subscription. DogNAS Client Lite is always free.',
   apps='The apps', app1='The server: install it on the Android that will keep your files.', app2='The access app: install it on your phone to browse, upload and download.', app3='New: the full app for Android and iPhone, coming soon.', privacy='Privacy policy'),
 'es': dict(title='DogNAS — Tu móvil viejo. Tu almacenamiento privado.', desc='Convierte un móvil o tableta Android en almacenamiento privado por Wi-Fi: fotos, vídeos y documentos en casa. Sin nube, sin cuotas mensuales y sin comprar un NAS.',
   h1='Tu móvil viejo. Tu almacenamiento privado.', lead='Convierte un móvil o tableta Android compatible en un espacio para guardar y acceder a fotos, vídeos y documentos por Wi-Fi. Sin nube, sin cuotas mensuales y sin comprar un NAS.',
   points=['Usa un Android que ya tienes', 'Conecta otros móviles con un código QR', 'Empieza gratis, sin suscripción'], cta='Descargar DogNAS gratis',
   micro='Consulta los requisitos de compatibilidad antes de instalar.', sub='¿Ya tienes el servidor? Descarga DogNAS Client Lite', sub_client='¿Ya tienes el servidor? Descarga DogNAS Client', lite_alt='¿Prefieres algo más ligero? Usa Client Lite',
   important='Tus archivos se guardan en el almacenamiento configurado en tu dispositivo servidor. El acceso depende de la configuración de tu red y de las credenciales de DogNAS. Para archivos importantes, mantén una copia de respaldo independiente.', important_h='Importante', cookies='Preferencias de cookies',
   soon='Próximamente en Google Play', get_server='Descargar DogNAS (servidor)', get_lite='Descargar DogNAS Client Lite', alt1='Servidor DogNAS en línea', alt2='Archivos en DogNAS Client Lite',
   who='¿Para quién es DogNAS?',
   ben_kicker='Beneficios', ben_h2='Los problemas que DogNAS resuelve', ben_lead='En casa, en la oficina en casa o en tu casa inteligente, DogNAS acaba con molestias diarias usando un Android que ya tienes.',
   ben=[('home', 'Uso doméstico', [
          ('El teléfono siempre lleno, sin espacio para fotos y videos.', 'Envía fotos y videos a DogNAS por Wi-Fi y libera espacio en el teléfono. Mantén también una copia independiente de lo importante.'),
          ('Una suscripción de nube que no deja de subir.', 'Usa el Android olvidado en un cajón: Gratis guarda hasta 64 GB y Pro es una compra única, sin suscripción.'),
          ('Fotos de la familia dispersas y guardadas en servidores ajenos.', 'Todo en un solo lugar, dentro de casa: un perfil y un PIN para cada persona, sin nube y sin cuenta.')]),
        ('briefcase', 'Oficina en casa', [
          ('Archivos de trabajo atrapados en memorias USB y en correos a ti mismo.', 'Ábrelos desde el PC, el Mac, la tablet o el teléfono por la red: FileZilla, WinSCP, Cyberduck o DogNAS Client Lite.'),
          ('Un NAS tradicional es caro y difícil de configurar.', 'Instala una app, toca Iniciar y vincula con un código QR y un PIN. Sin tocar el router.'),
          ('Documentos de clientes en una nube pública.', 'Se quedan en tu red, cifrados en tránsito (SSH/SFTP), con una credencial por dispositivo que revocas cuando quieras.')]),
        ('smart-home', 'Casa inteligente', [
          ('Grabaciones de cámaras atadas a la nube de pago del fabricante.', 'Las cámaras y NVR que envían por SFTP graban directo en DogNAS, en tu red.'),
          ('Automatizaciones sin un lugar donde guardar archivos.', 'Home Assistant, Node-RED, rclone y scripts envían y buscan archivos por SFTP.'),
          ('Un servidor que se detiene cuando se va la luz.', 'El teléfono tiene su propia batería y, en Pro, DogNAS puede arrancar solo tras reiniciar (depende del dispositivo y de los permisos de Android).')])],
   aud=[('casa', 'Para tu casa', 'Tu Android viejo se convierte en el almacenamiento de la familia, por Wi-Fi. Sin complicaciones.', 'Ver cómo funciona'),
        ('tech', 'Para gente de tecnología', 'Un servidor SFTP siempre encendido: NAS en casa o en la oficina, casa inteligente e IoT.', 'Ver detalles técnicos')],
   home_kicker='Para tu casa', home_h2='Tu Android viejo como almacenamiento de casa, por Wi-Fi',
   home_lead='Ese teléfono olvidado en un cajón empieza a guardar las fotos, los videos y los documentos de todos. Los ves desde tu teléfono, en cualquier habitación, sin cables y sin pagar nube.',
   home_feats=[('¡Libera espacio en tu teléfono!', 'Usa DogNAS Client Lite para enviar fotos y videos de tu teléfono a DogNAS, que los guarda en tu perfil. Antes de borrarlos del teléfono, comprueba que están en DogNAS y mantén una copia independiente de lo importante.'),
               ('Un espacio para cada persona', 'Cada perfil tiene su PIN y sus carpetas. Nadie ve los archivos de los demás.'),
               ('Fácil de conectar', 'Usa DogNAS Client Lite para conectarte a tu servidor DogNAS: apunta la cámara al código QR, escribe el PIN y listo.'),
               ('Sin nube y sin cuotas', 'Tus archivos se guardan en el almacenamiento de tu Android DogNAS, accesibles por el Wi-Fi de tu casa. Sin cuenta, sin anuncios, sin cobros mensuales. Usa todo el espacio del dispositivo: 32, 64, 128, 256 GB y más (más de 64 GB con DogNAS Pro).')],
   how='Cómo funciona',
   steps=[('Enciende el servidor', 'Instala DogNAS en el Android que guardará los archivos — en el dispositivo, una tarjeta SD o un disco USB — y toca Iniciar.', 'server-status'),
          ('Conecta tu teléfono', 'Genera el código QR de un perfil y escanéalo con DogNAS Client Lite. Cada perfil tiene su PIN y su espacio.', 'server-qr'),
          ('Usa tus archivos', 'Navega, sube y descarga por el Wi-Fi de casa. PC y Mac se conectan por SFTP.', 'lite-files')],
   tech_kicker='Para tecnología, casa inteligente y oficina', tech_h2='Un servidor SFTP en Android, siempre encendido',
   tech_lead='Un NAS ligero para casa u oficina: cualquier dispositivo, script o automatización que hable SFTP envía y recoge archivos por Wi-Fi.',
   tech_feats=[('NAS en casa o en la oficina', 'Carpetas por perfil, accesibles desde PC, Mac y Linux con FileZilla, WinSCP, Cyberduck, rclone o el sftp de OpenSSH.'),
               ('Casa inteligente e IoT', 'Recibe archivos de cámaras y NVR que suben por SFTP, copias de seguridad de otros servidores y scripts de automatización (Home Assistant, Node-RED, cron).'),
               ('Cifrado en tránsito', 'SSH-2 con AES-GCM o ChaCha20, la clave del servidor fijada al vincular y una credencial por dispositivo, revocable en cualquier momento.'),
               ('Pensado para estar encendido', 'Guarda en la memoria interna, en una tarjeta SD o en un disco o pendrive USB. Con Pro puede arrancar solo tras reiniciar. Algunos fabricantes limitan las apps en segundo plano: consulta los requisitos.')],
   prod=('Productividad en la oficina', 'Ideal para quien trabaja con fotos, videos y documentos y necesita organizarlo todo: los archivos quedan accesibles desde el PC, la tableta y el smartphone, sin pendrives ni cables. DogNAS es toda la facilidad por tu Wi-Fi.'),
   specs_h3='Especificaciones',
   specs=[('Protocolo', 'SFTP sobre SSH-2'), ('Autenticación', 'Usuario y contraseña — una credencial por dispositivo, revocable'),
          ('Almacenamiento', 'Memoria interna, tarjeta SD, disco o pendrive USB'), ('Clientes', 'DogNAS Client Lite, FileZilla, WinSCP, Cyberduck, rclone, OpenSSH y scripts'),
          ('Requisitos', 'Android 7.0 o más reciente, en la misma red')],
   more_kicker='Para todos', more_h2='Más espacio para tu DogNAS', more_lead='¿Quieres más espacio? Conecta un SSD externo o incluso el disco duro que sacaste de tu portátil viejo. Cada disco es un almacenamiento independiente: DogNAS no junta varios discos en un solo volumen.',
   more_feats=[('SSD externo', 'Conecta un SSD USB y gana espacio y velocidad para guardar todo lo de casa.'), ('El disco del portátil viejo', 'Pon el disco que cambiaste del portátil en una carcasa USB y dale una nueva vida como almacenamiento de casa.'), ('Tarjeta SD o pendrive', 'La forma más sencilla de ampliar el espacio del teléfono que se convirtió en servidor.'), ('Varios DogNAS en casa', '¿Tienes más de un Android olvidado? Cada uno puede ser un DogNAS; DogNAS Client Lite los muestra todos en “Mis almacenamientos”.')],
   more_note='Los discos USB necesitan un teléfono con USB OTG. Los discos mecánicos pueden pedir más energía de la que da el teléfono: en ese caso, usa un hub USB con alimentación. En el plan Gratis, DogNAS gestiona hasta 64 GB; con Pro, el disco entero. Un solo disco puede fallar: mantén una copia independiente de tus archivos importantes.',
   tech_photo='El Monitor del servidor: velocidad, clientes conectados y sesiones TCP en tiempo real.',
   more_photo='Un servidor con un disco externo en un dock USB, al que se accede desde el teléfono.',
   watch='Sigue todo', cap1='Transferencias y clientes en el servidor', cap2='Cola de transferencias en el teléfono',
   plans='Gratis para empezar', planhead=('', 'Gratis', 'Pro'),
   rows=[('Almacenamiento', '64 GB', 'Todo el dispositivo'), ('Perfiles', 'Casa + 2', 'Ilimitados'), ('Dispositivos vinculados', '3', 'Ilimitados'), ('Rendimiento', 'Bueno', 'Máximo optimizado'), ('Transferencias de la app cliente, con la app cerrada', 'Se pausan', 'Continúan'), ('Tras reiniciar', 'Toca para iniciar', 'Se inicia solo')],
   plannote='DogNAS Pro: compra única, sin suscripción. DogNAS Client Lite siempre es gratis.',
   apps='Las apps', app1='El servidor: instálalo en el Android que guardará los archivos.', app2='La app de acceso: instálala en tu teléfono para ver, subir y descargar archivos.', app3='Nuevo: la app completa para Android y iPhone, próximamente.', privacy='Política de privacidad'),
}
# Real photos from tools/build_photos.py (900 px wide WebP); sizes keep the layout from jumping.
PHOTO_H = {'always-on': 1129, 'usb-drive': 1347}
def photo(base, name, cap): return f'<figure class="real"><img src="{base}assets/photos/{name}.webp" alt="{html.escape(cap)}" width="900" height="{PHOTO_H[name]}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
def benefits(groups): return '<div class="benefits">' + ''.join(
    f'<div class="bcard">{icon(k)}<h3>{h}</h3><ul>' + ''.join(f'<li><span class="pain">{a}</span><span class="fix">{b}</span></li>' for a, b in items) + '</ul></div>'
    for k, h, items in groups) + '</div>'
def phone(src, alt, eager=False): return f'<div class="phone"><img src="{src}" alt="{html.escape(alt)}" width="540" height="1080" {"fetchpriority=high" if eager else "loading=lazy"}></div>'
PRIV_ICONS = ['no-cloud', 'shield', 'people', 'qr']
HOME_ICONS = ['phone-free', 'people', 'qr', 'no-cloud']
MORE_ICONS = ['ssd', 'hdd', 'sd', 'devices']
TECH_ICONS = ['server', 'smart-home', 'shield', 'power']
def cards(items, keys): return '<div class="grid feats">' + ''.join(f'<div class="card">{icon(k)}<h3>{h}</h3><p>{p}</p></div>' for k, (h, p) in zip(keys, items)) + '</div>'
for L, t in T.items():
    t = {**t, **NEW[L]}
    base = '' if L == 'pt' else '../'
    sh = f'{base}assets/shots/{L}/'
    nav = ''.join(f'<a data-ev="lang_switch" data-loc="{l}" href="{base}{LANGS[l][1]}"{" class=on" if l == L else ""}>{NAMES[l]}</a>' for l in LANGS)
    jsonld = seo.ld([seo.ORG, seo.website(L, LANGS[L][1])] + seo.webpage(L, LANGS[L][1], t['title'], t['desc']) + [
        seo.app('DogNAS', {'pt': 'Servidor de arquivos para Android: transforma um Android compatível em armazenamento particular na rede Wi-Fi, com SFTP.', 'en': 'File server for Android: turns a compatible Android into private storage on your Wi-Fi network, with SFTP.', 'es': 'Servidor de archivos para Android: convierte un Android compatible en almacenamiento privado en tu red Wi-Fi, con SFTP.'}[L], seo.PLAY_SERVER, L, app_id='#app-server'),
        seo.app('DogNAS Client Lite', {'pt': 'App leve e gratuito para Android que acessa os arquivos do seu DogNAS pelo Wi-Fi de casa.', 'en': 'Lightweight, free Android app that reaches your DogNAS files over your home Wi-Fi.', 'es': 'App ligera y gratuita para Android que accede a los archivos de tu DogNAS por el Wi-Fi de casa.'}[L], seo.PLAY_LITE, L, app_id='#app-lite')])
    faq_ld = seo.ld([seo.faq(t['faq'])])
    points = ''.join(f'<li>{x}</li>' for x in t['points'])
    if CLIENT_PLAY:
        sub_cta = f'<a data-ev="client_store_click" data-loc="hero_client" href="{CLIENT_PLAY}" rel="noopener">{t["sub_client"]}</a> · <a data-ev="lite_store_click" data-loc="hero_lite" href="{play("lite", "hero_lite")}" rel="noopener">{t["lite_alt"]}</a>'
    else:
        sub_cta = f'<a data-ev="lite_store_click" data-loc="hero_secondary" href="{play("lite", "hero_secondary")}" rel="noopener">{t["sub"]}</a>'
    aud = ''.join(f'<a class="aud aud-{k}" href="#{k}">{icon("home" if k == "casa" else "terminal")}<h3>{h}</h3><p>{p}</p><span>{more} →</span></a>' for k, h, p, more in t['aud'])
    def band(i, loc):
        h, btn = t['bands'][i]
        return f'<div class="cta-band"><p>{h}</p><a class="btn primary" data-ev="server_store_click" data-loc="{loc}" href="{play("server", loc)}" rel="noopener">{btn}</a></div>'
    goals = ''.join(f'<div class="goal goal-{i}"><span class="tag">{n}</span><h3>{tag}</h3><p>{txt}</p></div>' for i, (n, tag, txt) in enumerate(t['goals']))
    req = ''.join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in t['req'])
    faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in t['faq'])
    trust = ''.join(f'<a class="btn{" primary" if i == 0 else ""}" data-ev="support_click" data-loc="support_{i}" href="{u.format(EMAIL=EMAIL, base=base)}">{n}</a>' for i, (n, u) in enumerate(t['trust_links']))
    steps = ''.join(f'<div class="step"><div class="num">{i}</div><h3>{h}</h3><p>{p}</p>{phone(sh + img + ".webp", h)}</div>' for i, (h, p, img) in enumerate(t['steps'], 1))
    specs = ''.join(f'<tr><th>{a}</th><td>{b}</td></tr>' for a, b in t['specs'])
    rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in t['rows'])
    head = ''.join(f'<th>{h}</th>' for h in t['planhead'])
    page = f'''<!doctype html>
<html lang="{LANGS[L][0]}">
<head>
{GA_TAG}<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t['title'])}</title>
<meta name="description" content="{html.escape(t['desc'])}">
{seo.meta(L, LANGS[L][1], t['title'], t['desc'], {l: LANGS[l][1] for l in LANGS})}{jsonld}{faq_ld}<link rel="icon" href="{base}assets/icon-192.png">
<link rel="stylesheet" href="{base}assets/style.css?v={CSS_V}">
</head>
<body><div class="wrap">
<header class="top"><a class="brand" href="{base}{LANGS[L][1]}"><img src="{base}assets/icon-192.png" alt="" width="36" height="36"><span>Dog<b>NAS</b></span></a><nav class="lang">{nav}</nav></header>
<div class="hero-grid">
<section class="hero"><img class="logo" src="{base}assets/icon-192.png" alt="DogNAS" width="120" height="120"><h1>{t['h1']}</h1><p>{t['lead']}</p>
<ul class="points">{points}</ul>
<div class="cta"><a class="btn primary" data-ev="server_store_click" data-loc="hero_primary" href="{play('server', 'hero_primary')}" rel="noopener">{t['cta']}</a></div>
<p class="micro"><a data-ev="requirements_click" href="#requisitos">{t['micro']}</a></p>
<p class="cta-sub">{sub_cta}</p></section>
<div class="phones">{phone(sh + 'server-status.webp', t['alt1'], True)}{phone(sh + 'lite-files.webp', t['alt2'], True)}</div>
</div>
<section id="como-funciona" class="audience">
<h2>{t['how_h2']}</h2><p class="lead">{t['how_lead']}</p>
<div class="steps">{steps}</div>
<p class="note"><a href="#tech">{t['adv_link']}</a></p>
{band(0, 'mid_how')}
</section>
<section id="beneficios" class="audience benefits-sec">
<p class="kicker">{t['ben_kicker']}</p><h2>{t['ben_h2']}</h2><p class="lead">{t['ben_lead']}</p>
{benefits(t['ben'])}
</section>
<section id="casa" class="audience">
<p class="kicker">{t['home_kicker']}</p><h2>{t['home_h2']}</h2><p class="lead">{t['home_lead']}</p>
{cards(t['home_feats'], HOME_ICONS)}
</section>
<h2>{t['watch']}</h2>
<div class="twoup"><figure>{phone(sh + 'server-monitor.webp', t['cap1'])}<figcaption>{t['cap1']}</figcaption></figure><figure>{phone(sh + 'lite-transfers.webp', t['cap2'])}<figcaption>{t['cap2']}</figcaption></figure></div>
<section id="privacidade" class="audience">
<p class="kicker">{t['priv_kicker']}</p><h2>{t['priv_h2']}</h2><p class="lead">{t['priv_lead']}</p>
{cards(t['priv'], PRIV_ICONS)}
<p class="note backup">{t['important']}</p>
</section>
<section id="planos" class="audience">
<h2>{t['plans_h2']}</h2>
<div class="goals">{goals}</div>
<div class="table-wrap"><table class="plans"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
<p class="note">{t['plannote']}</p>
{band(1, 'mid_plans')}
</section>
<section id="tech" class="audience tech">
<p class="kicker">{t['tech_kicker']}</p><h2>{t['tech_h2']}</h2><p class="lead">{t['tech_lead']}</p>
<div class="split">{photo(base, 'always-on', t['tech_photo'])}{cards(t['tech_feats'], TECH_ICONS)}</div>
<div class="card wide">{icon('briefcase')}<h3>{t['prod'][0]}</h3><p>{t['prod'][1]}</p></div>
<h3 class="sub">{t['specs_h3']}</h3>
<div class="table-wrap"><table class="plans specs"><tbody>{specs}</tbody></table></div>
</section>
<section id="mais" class="audience more">
<p class="kicker">{t['more_kicker']}</p><h2>{t['more_h2']}</h2><p class="lead">{t['more_lead']}</p>
<div class="split">{photo(base, 'usb-drive', t['more_photo'])}{cards(t['more_feats'], MORE_ICONS)}</div>
<p class="note">{t['more_note']}</p>
</section>
<section id="requisitos" class="audience">
<p class="kicker">{t['req_kicker']}</p><h2>{t['req_h2']}</h2>
<div class="grid feats">{req}</div>
<h3 class="sub" id="faq">{t['faq_h2']}</h3>
<div class="faq">{faq}</div>
{band(2, 'mid_faq')}
</section>
<section id="suporte" class="audience">
<h2>{t['trust_h2']}</h2><p class="lead">{t['trust_lead']}</p>
<div class="cta">{trust}</div>
</section>
<h2>{t['apps']}</h2>
<div class="grid apps"><a class="card" data-ev="server_store_click" data-loc="apps_server" href="{play('server', 'apps_card')}" rel="noopener"><img src="{base}assets/icon.png" alt=""><div><h3>DogNAS</h3><p>{t['app1']}</p></div></a><a class="card" data-ev="lite_store_click" data-loc="apps_lite" href="{play('lite', 'apps_card')}" rel="noopener"><img src="{base}assets/icon-lite.png" alt=""><div><h3>DogNAS Client Lite</h3><p>{t['app2']}</p></div></a><a class="card" data-ev="client_page_click" data-loc="apps_client" href="{base}{LANGS[L][1]}client/"><img src="{base}assets/icon.png" alt=""><div><h3>DogNAS Client</h3><p>{t['app3']}</p></div></a></div>
<section class="final"><h2>{t['final_h2']}</h2><p>{t['final_lead']}</p>
<div class="cta"><a class="btn primary" data-ev="server_store_click" data-loc="final" href="{play('server', 'final_cta')}" rel="noopener">{t['cta']}</a></div>
<p class="micro"><a data-ev="requirements_click" href="#requisitos">{t['micro']}</a></p></section>
<footer><span>© 2026 DogNAS</span><span><a href="{base}privacy/#{L}">{t['privacy']}</a> · <a href="#" data-cookie-prefs>{t['cookies']}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span></footer>
</div>
<div class="float-cta" hidden><a class="btn primary" data-ev="server_store_click" data-loc="float" href="{play('server', 'float_cta')}" rel="noopener">{t['cta']}</a></div>
<script>
// Floating CTA: shown only after the hero button scrolled away, never while the cookie banner is open, and hidden
// while an in-page CTA (bands / final) is on screen so it never stacks with them.
(function () {{
  var f = document.querySelector('.float-cta'), hero = document.querySelector('.hero .cta'); if (!f || !hero || !('IntersectionObserver' in window)) return;
  var heroPast = false, busy = 0;
  function update() {{ f.hidden = !(heroPast && !busy && !document.getElementById('dn-consent')); }}
  new IntersectionObserver(function (e) {{ heroPast = !e[0].isIntersecting && e[0].boundingClientRect.top < 0; update(); }}).observe(hero);
  var io = new IntersectionObserver(function (es) {{ es.forEach(function (x) {{ busy += x.isIntersecting ? 1 : -1; }}); busy = Math.max(0, busy); update(); }});
  document.querySelectorAll('.cta-band, .final').forEach(function (n) {{ io.observe(n); }});
  new MutationObserver(update).observe(document.body, {{childList: true}});
}})();
</script>
</body></html>
'''
    out = os.path.join(ROOT, 'index.html' if L == 'pt' else f'{L}/index.html')
    open(out, 'w').write(page)
print('ok')

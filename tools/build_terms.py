"""Terms of Service (PT, EN, ES in one page at /terms/), the URL for the Play Console "Terms of Service" field.
Run: python3 tools/build_terms.py. Keep it short and specific to the apps (no account, no service, no cloud); the privacy facts live in /privacy/."""
import os, html
import seo
from build_home import GA_TAG, CSS_INLINE, blog_link, blog_nav
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL = 'me.pauloleite.dev@gmail.com'
LANGS = {'en': ('en', '/', 'English'), 'pt': ('pt-BR', '/pt/', 'Português'), 'es': ('es', '/es/', 'Español')}
TITLE = 'DogNAS — Termos de Serviço / Terms of Service'
DESC = 'Termos de Serviço do DogNAS, do DogNAS Client Lite e do DogNAS Client. Terms of Service for DogNAS, DogNAS Client Lite and DogNAS Client.'
LINKS = {'pt': ('Política de privacidade', 'Termos de Serviço'), 'en': ('Privacy policy', 'Terms of Service'), 'es': ('Política de privacidad', 'Términos del servicio')}

def page(body):
    base = '../'
    nav = blog_nav('en', base, 'terms') + ''.join(f'<a href="{base}{LANGS[l][1].lstrip("/")}">{LANGS[l][2]}</a>' for l in LANGS)
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
{GA_TAG}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(TITLE)}</title>
<meta name="description" content="{html.escape(DESC)}">
{seo.meta('pt', 'terms/', TITLE, DESC, None)}<link rel="icon" type="image/png" href="{base}assets/icon-96.png">
{CSS_INLINE}
</head>
<body><div class="wrap">
<header class="top"><a class="brand" href="{base}"><img src="{base}assets/icon-80.webp" alt="" width="36" height="36"><span>Dog<b>NAS</b></span></a><nav class="lang">{nav}</nav></header>
{body}
<footer><span>© 2026 DogNAS</span><span>{blog_link('en', base)}<a href="{base}privacy/">Privacy · Privacidade</a> · <a href="#" data-cookie-prefs>Cookies</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></span></footer>
</div></body></html>
'''

TERMS = {
'pt': ('Termos de Serviço', 'Última atualização: 11 de novembro de 2026', '''
<p>Estes termos valem para os três apps: <b>DogNAS</b> (o servidor, <code>com.dognas.server</code>), <b>DogNAS Client Lite</b> (<code>com.dognas.client.lite</code>) e <b>DogNAS Client</b> (<code>com.dognas.client</code>). Ao instalar ou usar um deles, você concorda com estes termos.</p>
<h3>1. O que é o DogNAS</h3><p>O DogNAS transforma um Android num servidor de arquivos na sua rede Wi-Fi, e os apps Client acessam esse servidor. Não existe conta, nuvem ou servidor do DogNAS: os arquivos ficam nos seus aparelhos e trafegam só na sua rede.</p>
<h3>2. Seus arquivos e sua responsabilidade</h3><ul>
<li>Os arquivos são seus. O DogNAS não os lê, não os envia a terceiros e não adquire nenhum direito sobre eles.</li>
<li><b>Armazenamento não é backup.</b> Aparelhos podem quebrar, ser perdidos, ficar sem bateria ou ter o armazenamento corrompido. Mantenha cópias do que é importante e confira se um arquivo chegou ao DogNAS antes de apagá-lo do celular.</li>
<li>Guarde com segurança os PINs e as senhas dos seus perfis e dispositivos. Quem os tiver acessa os arquivos do perfil.</li></ul>
<h3>3. Uso permitido</h3><p>Use os apps só com arquivos e aparelhos seus ou que você tem autorização para usar, e de acordo com a lei. Não use o DogNAS para guardar ou compartilhar conteúdo ilegal, nem para violar direitos de outras pessoas, e não tente burlar os limites, a segurança ou os planos dos apps.</p>
<h3>4. Planos Grátis e Pro</h3><ul>
<li>O DogNAS pode ser usado no plano <b>Grátis</b>, com os limites mostrados no app. O <b>Pro</b> é opcional, uma <b>compra única</b>, sem assinatura.</li>
<li>A compra, o pagamento e o reembolso são feitos pelo Google Play e seguem as regras dele. O Pro fica ligado à sua conta Google do Play e pode ser restaurado nela.</li>
<li>Os recursos de cada plano podem evoluir com o tempo; o que está descrito no app e na página do app na Play vale na data da sua compra.</li></ul>
<h3>5. Desempenho e disponibilidade</h3><p>A velocidade e a disponibilidade dependem dos seus aparelhos, do cartão SD ou HD, do Wi-Fi e das regras de economia de bateria do Android, que podem pausar o servidor. Não garantimos velocidade, funcionamento ininterrupto nem compatibilidade com todos os aparelhos.</p>
<h3>6. Privacidade</h3><p>O que os apps e o site tratam está na <a href="../privacy/#pt">Política de privacidade</a>.</p>
<h3>7. Componentes de código aberto</h3><p>Os apps usam bibliotecas de código aberto (como o Apache MINA SSHD), cada uma sob a sua licença.</p>
<h3>8. Sem garantias e limite de responsabilidade</h3><p>Os apps são fornecidos “como estão”. Na medida permitida pela lei, o desenvolvedor não responde por perda de dados, lucros cessantes ou danos indiretos decorrentes do uso dos apps ou da impossibilidade de usá-los. Isso não afasta direitos que a lei garante a você como consumidor.</p>
<h3>9. Mudanças, lei aplicável e contato</h3><p>Se estes termos mudarem, a nova versão será publicada neste endereço, com a data atualizada; continuar usando os apps depois disso significa aceitar a versão nova. Estes termos são regidos pela legislação brasileira. Dúvidas: <a href="mailto:EMAIL">EMAIL</a>.</p>'''),
'en': ('Terms of Service', 'Last updated: November 11, 2026', '''
<p>These terms apply to all three apps: <b>DogNAS</b> (the server, <code>com.dognas.server</code>), <b>DogNAS Client Lite</b> (<code>com.dognas.client.lite</code>) and <b>DogNAS Client</b> (<code>com.dognas.client</code>). By installing or using any of them, you agree to these terms.</p>
<h3>1. What DogNAS is</h3><p>DogNAS turns an Android into a file server on your Wi-Fi, and the Client apps access that server. There is no DogNAS account, cloud or server: your files stay on your own devices and travel only on your network.</p>
<h3>2. Your files and your responsibility</h3><ul>
<li>The files are yours. DogNAS does not read them, does not send them to third parties and acquires no rights over them.</li>
<li><b>Storage is not a backup.</b> Devices can break, get lost, run out of battery or have their storage corrupted. Keep copies of what matters and check that a file reached DogNAS before deleting it from your phone.</li>
<li>Keep the PINs and passwords of your profiles and devices safe. Anyone who has them can access the profile’s files.</li></ul>
<h3>3. Acceptable use</h3><p>Use the apps only with files and devices that are yours or that you are authorized to use, and in line with the law. Do not use DogNAS to store or share illegal content, to violate other people’s rights, or to bypass the apps’ limits, security or plans.</p>
<h3>4. Free and Pro plans</h3><ul>
<li>DogNAS can be used on the <b>Free</b> plan, with the limits shown in the app. <b>Pro</b> is optional, a <b>one-time purchase</b>, with no subscription.</li>
<li>Purchase, payment and refunds are handled by Google Play and follow its rules. Pro is tied to your Google Play account and can be restored on it.</li>
<li>The features of each plan may evolve over time; what the app and its Play page describe applies on the date of your purchase.</li></ul>
<h3>5. Performance and availability</h3><p>Speed and availability depend on your devices, the SD card or drive, your Wi-Fi and Android’s battery-saving rules, which may pause the server. We do not guarantee speed, uninterrupted operation or compatibility with every device.</p>
<h3>6. Privacy</h3><p>What the apps and the website handle is described in the <a href="../privacy/#en">Privacy policy</a>.</p>
<h3>7. Open-source components</h3><p>The apps use open-source libraries (such as Apache MINA SSHD), each under its own license.</p>
<h3>8. No warranty and limit of liability</h3><p>The apps are provided “as is”. To the extent permitted by law, the developer is not liable for loss of data, lost profits or indirect damages arising from the use of, or inability to use, the apps. This does not affect any rights that the law gives you as a consumer.</p>
<h3>9. Changes, governing law and contact</h3><p>If these terms change, the new version will be published at this address with the date updated; continuing to use the apps afterwards means accepting the new version. These terms are governed by Brazilian law. Questions: <a href="mailto:EMAIL">EMAIL</a>.</p>'''),
'es': ('Términos del servicio', 'Última actualización: 11 de noviembre de 2026', '''
<p>Estos términos se aplican a las tres apps: <b>DogNAS</b> (el servidor, <code>com.dognas.server</code>), <b>DogNAS Client Lite</b> (<code>com.dognas.client.lite</code>) y <b>DogNAS Client</b> (<code>com.dognas.client</code>). Al instalar o usar cualquiera de ellas, aceptas estos términos.</p>
<h3>1. Qué es DogNAS</h3><p>DogNAS convierte un Android en un servidor de archivos en tu Wi-Fi, y las apps Client acceden a ese servidor. No existe cuenta, nube ni servidor de DogNAS: tus archivos se quedan en tus dispositivos y viajan solo por tu red.</p>
<h3>2. Tus archivos y tu responsabilidad</h3><ul>
<li>Los archivos son tuyos. DogNAS no los lee, no los envía a terceros y no adquiere ningún derecho sobre ellos.</li>
<li><b>El almacenamiento no es una copia de seguridad.</b> Los dispositivos pueden romperse, perderse, quedarse sin batería o corromper su almacenamiento. Conserva copias de lo importante y comprueba que un archivo llegó a DogNAS antes de borrarlo del móvil.</li>
<li>Guarda con seguridad los PIN y las contraseñas de tus perfiles y dispositivos. Quien los tenga accede a los archivos del perfil.</li></ul>
<h3>3. Uso permitido</h3><p>Usa las apps solo con archivos y dispositivos tuyos o que estés autorizado a usar, y conforme a la ley. No uses DogNAS para guardar o compartir contenido ilegal, para vulnerar derechos de otras personas ni para eludir los límites, la seguridad o los planes de las apps.</p>
<h3>4. Planes Gratis y Pro</h3><ul>
<li>DogNAS puede usarse en el plan <b>Gratis</b>, con los límites que muestra la app. El <b>Pro</b> es opcional, una <b>compra única</b>, sin suscripción.</li>
<li>La compra, el pago y los reembolsos los gestiona Google Play y siguen sus reglas. El Pro queda vinculado a tu cuenta de Google Play y se puede restaurar en ella.</li>
<li>Las funciones de cada plan pueden evolucionar con el tiempo; lo que describen la app y su página en Play vale en la fecha de tu compra.</li></ul>
<h3>5. Rendimiento y disponibilidad</h3><p>La velocidad y la disponibilidad dependen de tus dispositivos, de la tarjeta SD o el disco, de tu Wi-Fi y de las reglas de ahorro de batería de Android, que pueden pausar el servidor. No garantizamos velocidad, funcionamiento ininterrumpido ni compatibilidad con todos los dispositivos.</p>
<h3>6. Privacidad</h3><p>Lo que tratan las apps y el sitio está en la <a href="../privacy/#es">Política de privacidad</a>.</p>
<h3>7. Componentes de código abierto</h3><p>Las apps usan bibliotecas de código abierto (como Apache MINA SSHD), cada una bajo su propia licencia.</p>
<h3>8. Sin garantías y límite de responsabilidad</h3><p>Las apps se ofrecen «tal cual». En la medida permitida por la ley, el desarrollador no responde por pérdida de datos, lucro cesante ni daños indirectos derivados del uso de las apps o de la imposibilidad de usarlas. Esto no afecta a los derechos que la ley te otorga como consumidor.</p>
<h3>9. Cambios, ley aplicable y contacto</h3><p>Si estos términos cambian, la nueva versión se publicará en esta misma dirección, con la fecha actualizada; seguir usando las apps después significa aceptar la versión nueva. Estos términos se rigen por la legislación brasileña. Dudas: <a href="mailto:EMAIL">EMAIL</a>.</p>'''),
}
sections = ''.join(f'<section class="legal" id="{l}"><h2>{t}</h2><p class="meta">{m}</p>{b.replace("EMAIL", EMAIL)}</section>' for l, (t, m, b) in TERMS.items())
jump = '<p class="meta"><a href="#pt">Português</a> · <a href="#en">English</a> · <a href="#es">Español</a></p>'
out = os.path.join(ROOT, 'terms', 'index.html')
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w').write(page('<h1 style="margin-top:32px">Termos de Serviço · Terms of Service · Términos del servicio</h1>' + jump + sections))
print('ok')

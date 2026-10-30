"""Trust page of the blog (BLOG-13): "How we test" per language, the team byline and the "Tested on" labels.
Facts here must stay true: the test devices are the ones in the workspace CLAUDE.md; update both together."""
TEAM = {'en': 'DogNAS Team', 'pt': 'Equipe DogNAS', 'es': 'Equipo DogNAS'}
SLUG = {'en': 'how-we-test', 'pt': 'como-testamos', 'es': 'como-probamos'}
LABEL = {'en': dict(by='By', tested='Tested on', how='How we test'), 'pt': dict(by='Por', tested='Testado em', how='Como testamos'), 'es': dict(by='Por', tested='Probado en', how='Cómo probamos')}

PAGE = {
 'en': dict(title='How we test and write the DogNAS guides', desc='Who writes the DogNAS blog, which Android devices we test on, how we handle limits and mistakes, and how to report a correction.',
  body="""DogNAS is made by a small independent team. The guides on this blog are prepared by the team that builds the app, and the procedures they describe are checked against the app itself.

## What we test on

The devices we keep for testing DogNAS, all real hardware:

- **Samsung Galaxy S20 FE** (Android 13), the phone that runs our own server.
- **Moto G100** (Android 12), used as a client.
- **Moto G Play** (Android 7.1.1), the weakest device we keep, to see what an old phone can really do.
- **EASYTECH E13** tablet (Android 7) with an SD card, to check storage on old hardware.

When a guide has a "Tested on" line, it names the device, the Android version and the date of the test.

## What we promise

- **Limits come first.** If DogNAS is the wrong tool for something (RAID, many users watching video at once, a replacement for backups), the guide says so.
- **No invented numbers.** Speeds and times come from our own measurements or are described as approximate.
- **Dates are real.** Each article shows when it was last updated, and we update it when the app or Android changes the steps.
- **Prices and plans** match what is on Google Play at the time of writing.

## Translations

Guides are available in Portuguese, English and Spanish. Each translation is reviewed before it is published.

## Spotted a mistake?

Write to us at the address in the footer. We fix factual errors quickly and update the date of the article.""",
  ),
 'pt': dict(title='Como testamos e escrevemos os guias do DogNAS', desc='Quem escreve o blog do DogNAS, em quais aparelhos Android testamos, como tratamos limites e erros e como pedir uma correção.',
  body="""O DogNAS é feito por uma equipe pequena e independente. Os guias deste blog são preparados pela equipe que faz o app, e os procedimentos descritos são conferidos no próprio app.

## Em que testamos

Os aparelhos que mantemos para testar o DogNAS, todos reais:

- **Samsung Galaxy S20 FE** (Android 13), o celular que roda o nosso próprio servidor.
- **Moto G100** (Android 12), usado como cliente.
- **Moto G Play** (Android 7.1.1), o aparelho mais fraco que mantemos, para ver o que um celular antigo realmente aguenta.
- **Tablet EASYTECH E13** (Android 7) com cartão SD, para conferir o armazenamento em hardware antigo.

Quando um guia traz a linha "Testado em", ela informa o aparelho, a versão do Android e a data do teste.

## O que prometemos

- **Os limites vêm primeiro.** Se o DogNAS é a ferramenta errada para algo (RAID, muita gente assistindo vídeo ao mesmo tempo, substituir backup), o guia diz.
- **Sem números inventados.** Velocidades e tempos vêm de medições nossas ou são descritos como aproximados.
- **As datas são reais.** Cada artigo mostra quando foi atualizado pela última vez, e atualizamos quando o app ou o Android mudam os passos.
- **Preços e planos** batem com o que está no Google Play na data do texto.

## Traduções

Os guias estão em português, inglês e espanhol. Cada tradução é revisada antes de ser publicada.

## Achou um erro?

Escreva para o endereço que aparece no rodapé. Corrigimos erros factuais rapidamente e atualizamos a data do artigo.""",
  ),
 'es': dict(title='Cómo probamos y escribimos las guías de DogNAS', desc='Quién escribe el blog de DogNAS, en qué dispositivos Android probamos, cómo tratamos los límites y los errores y cómo pedir una corrección.',
  body="""DogNAS lo hace un equipo pequeño e independiente. Las guías de este blog las prepara el equipo que hace la app, y los procedimientos que describen se comprueban en la propia app.

## En qué probamos

Los dispositivos que mantenemos para probar DogNAS, todos reales:

- **Samsung Galaxy S20 FE** (Android 13), el celular que ejecuta nuestro propio servidor.
- **Moto G100** (Android 12), usado como cliente.
- **Moto G Play** (Android 7.1.1), el dispositivo más débil que conservamos, para ver qué aguanta realmente un celular viejo.
- **Tablet EASYTECH E13** (Android 7) con tarjeta SD, para revisar el almacenamiento en hardware antiguo.

Cuando una guía trae la línea "Probado en", indica el dispositivo, la versión de Android y la fecha de la prueba.

## Qué prometemos

- **Los límites van primero.** Si DogNAS es la herramienta equivocada para algo (RAID, muchas personas viendo video a la vez, reemplazar una copia de seguridad), la guía lo dice.
- **Sin números inventados.** Las velocidades y los tiempos salen de mediciones nuestras o se describen como aproximados.
- **Las fechas son reales.** Cada artículo muestra cuándo se actualizó por última vez, y lo actualizamos cuando la app o Android cambian los pasos.
- **Precios y planes** coinciden con lo que hay en Google Play en la fecha del texto.

## Traducciones

Las guías están en portugués, inglés y español. Cada traducción se revisa antes de publicarse.

## ¿Encontraste un error?

Escríbenos a la dirección que aparece en el pie de página. Corregimos rápido los errores de hecho y actualizamos la fecha del artículo.""",
  ),
}

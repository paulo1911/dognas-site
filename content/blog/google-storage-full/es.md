---
slug: google-drive-fotos-lleno-guardar-en-casa
title: ¿Google Drive o Google Fotos lleno? Cómo sacar todo de ahí y guardarlo en casa
summary: Cómo exportar tus fotos y archivos de Google, guardarlos en un servidor tuyo en casa y recién entonces liberar espacio en la cuenta, sin pagar más cada mes.
meta_title: Google Fotos lleno: guarda tus fotos en casa | DogNAS
meta_description: ¿Google Drive o Fotos lleno? Exporta con Google Takeout, guarda todo en un servidor tuyo en casa y libera espacio en la cuenta sin pagar más.
pillar: storage
tags: [google fotos lleno, google drive lleno, google takeout, almacenamiento en la nube, servidor en casa]
cover: assets/blog/google-storage-full/cover-es.webp
cover_alt: Un móvil con el servidor DogNAS conectado por cable, junto a un disco duro en un soporte, sobre una mesa
social_image: assets/blog/google-storage-full/social-es.jpg
cta: server
related: [android-nas-server, cloud-subscription-savings, free-phone-space, pc-phone-transfer, sftp-clients]
status: review
translation_review: pending
created: 2026-11-26
published: 2026-11-26
updated: 2026-11-26
---
Llega el aviso: "tu almacenamiento está casi lleno". Gmail puede dejar de recibir correos y Google Fotos deja de guardar lo que sacas. La salida más rápida es pagar un plan más grande. Pero la cuota no termina nunca, y el espacio de una cuenta siempre se vuelve a llenar.

Hay otro camino: sacar lo pesado de ahí, guardarlo en casa y dejar la cuenta limpia. Da algo de trabajo al principio, pero se hace una sola vez. Abajo va un orden que tiene sentido, con los cuidados que casi todos olvidan.

> [!takeaways]
> - Exportar con **Google Takeout** crea una copia. Nada sale de tu cuenta hasta que tú lo borres.
> - Guarda esa copia en un servidor tuyo (un Android parado en un cajón sirve) y **compruébala** antes de borrar nada en Google.
> - Un servidor en casa no es un respaldo. Para lo que no se puede reemplazar, guarda una segunda copia en otro lugar.

## Primero: qué está ocupando el espacio

El espacio gratis (hoy 15 GB, una cifra que Google puede cambiar) se comparte entre Gmail, Drive y Fotos. Abre la pantalla de almacenamiento de la cuenta y mira cuál de los tres pesa más. Casi siempre es Fotos, y a veces una carpeta olvidada en Drive o adjuntos viejos en Gmail.

Esto importa porque cambia lo que vas a exportar. Si el problema es un vídeo de 4 GB en Drive, ni necesitas Takeout: descargas el archivo y listo.

## Paso 1: ten dónde guardarlo

Antes de descargar nada, decide adónde va. Puede ser un disco duro, pero si ya tienes un móvil o una tableta Android en un cajón, puedes convertirlo en un servidor de archivos en tu Wi-Fi. Lo explicamos en [cómo convertir un Android viejo en servidor de archivos](/blog/convertir-android-viejo-en-servidor-de-archivos/) y en la [guía completa del servidor NAS en Android](/blog/servidor-nas-android-guia-completa/).

Haz una cuenta rápida de tamaño. El plan Gratis de DogNAS gestiona hasta 64 GB. Si tu biblioteca de Google tiene 150 GB, necesitarás el Pro (compra única, sin suscripción), que usa todo el almacenamiento del dispositivo, incluida una tarjeta SD o un disco USB.

## Paso 2: exporta con Google Takeout

Takeout es la herramienta de Google para descargar tus datos (takeout.google.com).

1. Entra con la cuenta que está llena y deja marcado solo lo que quieres: **Google Fotos**, **Drive**, o los dos. Desmarcar el resto hace la exportación mucho más ligera.
2. En Drive y en Fotos puedes elegir solo algunos álbumes o carpetas. Si la biblioteca es enorme, conviene hacerlo por etapas.
3. Elige el formato del archivo y el tamaño de las partes. Partes más pequeñas (2 GB, por ejemplo) son más fáciles de descargar y de repetir si una falla.
4. Pide la exportación y espera. En bibliotecas grandes puede tardar de horas a unos días. Google te avisa por correo.
5. Descarga todas las partes. El enlace funciona por tiempo limitado, así que no lo dejes para después.

> [!note]
> Las fotos suelen venir con archivos `.json` que guardan la fecha y el lugar originales. Si abres la carpeta y te preguntas qué son, son esos. No los borres antes de ver cómo tu programa de fotos trata las fechas.

## Paso 3: llévalo a tu servidor

Cuando termines de descargar, descomprime y copia al servidor. Dos formas sencillas:

- **Desde el ordenador:** conéctate al servidor con un programa como FileZilla o WinSCP y arrastra las carpetas. Está todo en [cómo acceder a DogNAS con FileZilla, WinSCP, Cyberduck y rclone](/blog/acceder-a-dognas-con-filezilla-winscp-cyberduck-rclone/). Otra vía es el [Wi-Fi entre PC y móvil](/blog/transferir-archivos-entre-pc-y-celular-por-wifi/).
- **Desde el móvil:** si descargaste el Takeout directo en el móvil, envía las carpetas con DogNAS Client.

Una transferencia grande por Wi-Fi es lenta de verdad. Deja el ordenador encendido y el servidor enchufado, y no lo toques mientras copia.

## Paso 4: comprueba antes de borrar

Es el paso que nadie quiere hacer y que todos deberían. Antes de quitar nada de Google:

- Compara cantidades: cuántos archivos decía Google que tenías y cuántos llegaron.
- Abre algunas fotos y vídeos de épocas distintas, mejor los más pesados. ¿Se reproducen?
- Busca una carpeta que sabes que existe, de un evento concreto.
- Si puedes, copia también a un segundo lugar (un disco externo). El servidor en casa guarda tus archivos, pero no se respalda solo, y los discos fallan.

## Paso 5: libera espacio en la cuenta

Solo ahora borra, y poco a poco. En Google Fotos, lo que va a la papelera sigue contando hasta que la vacías. En Drive es igual. Y "liberar espacio" en la app del móvil suele quitar solo la copia local, sin tocar lo que está en la nube. Lee qué hace el botón antes de tocarlo.

Borrar poco a poco tiene una ventaja: si notas que falta algo, todavía puedes volver atrás.

## ¿Y si sigo usando Google Fotos?

Mucha gente lo hace, y está bien. Fotos es excelente para ver las fotos desde cualquier lugar y compartir un álbum. El servidor en casa es bueno para el volumen y la privacidad, pero solo se accede desde dentro de la red de casa. Un punto medio habitual: dejar los últimos meses en la nube y mandar el resto a casa de vez en cuando.

Si el objetivo es pagar menos, lee también [cómo ahorrar en suscripciones de almacenamiento en la nube](/blog/como-ahorrar-en-suscripciones-de-almacenamiento-en-la-nube/) y [cómo liberar espacio en el celular Android](/blog/como-liberar-espacio-en-el-celular-android/).

## Preguntas rápidas

?? ¿Exportar con Takeout borra mis archivos de Google?
No. Takeout solo crea una copia para que la descargues. Tus fotos y archivos siguen en la cuenta hasta que los borres.

?? ¿Puedo hacerlo solo desde el móvil?
Puedes, pero la exportación es grande y copiar desde un móvil es más lento. Con bibliotecas grandes, un ordenador lo facilita.

?? ¿Mi servidor puede ser un móvil que ya no uso?
Sí. Un Android 7.0 o más nuevo, enchufado y en tu Wi-Fi, ya sirve. La [guía del servidor NAS en Android](/blog/servidor-nas-android-guia-completa/) muestra qué funciona y dónde se detiene.

?? ¿Esto es un respaldo?
No por sí solo. Es una copia en casa, que depende del dispositivo y del disco. Para lo irreemplazable, guarda una segunda copia en otro lugar.

## Por dónde empezar

Abre la pantalla de almacenamiento de tu cuenta de Google, mira qué pesa y empieza con una exportación pequeña, solo para ver cómo funciona. Cuando el primer lote llegue bien al servidor, lo demás es repetir.

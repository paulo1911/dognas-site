---
slug: whatsapp-llenando-el-celular-liberar-espacio
title: WhatsApp llenando el celular: cómo sacar fotos y vídeos sin perder tus chats
summary: WhatsApp suele ser lo que más espacio ocupa en Android. Dónde están sus archivos, cómo copiarlos a un servidor tuyo en casa y solo entonces borrarlos del celular.
meta_title: WhatsApp llenando el celular: liberar espacio | DogNAS
meta_description: ¿Memoria llena por WhatsApp? Mira dónde están sus archivos, cómo copiarlos a tu servidor en casa con DogNAS y liberar espacio sin borrar tus chats.
pillar: storage
tags: [whatsapp, liberar espacio, almacenamiento, android, fotos y vídeos]
tested: Moto G100 · Android 12 · DogNAS Client 1.0.1 enviando a un servidor DogNAS (E13) · 2026-11-02
cover: assets/blog/free-phone-space/cover-es.webp
cover_alt: Ilustración de un celular con una flecha que saca archivos, junto a la pantalla de DogNAS Client Lite
social_image: assets/blog/free-phone-space/social-es.jpg
cta: client
related: [free-phone-space, old-android-server, pc-phone-transfer]
status: review
translation_review: pending
created: 2026-11-01
updated: 2026-11-01
---
**WhatsApp llena el celular porque, por defecto, descarga y guarda en el aparato las fotos, vídeos, audios y documentos que pasan por tus grupos**, incluso los que nunca abriste. La salida que conserva lo importante es copiar esos archivos a un lugar tuyo, comprobarlos y solo entonces borrarlos del celular. Las conversaciones de texto siguen en la app.

> [!takeaways]
> - Los archivos están en carpetas normales del celular que puedes copiar. Android 11 o más nuevo: `Android/media/com.whatsapp/WhatsApp/Media`. Android 10 o más antiguo: `WhatsApp/Media`.
> - Puedes copiar esas carpetas a un servidor tuyo en casa con DogNAS, sin nube ni mensualidad, y después borrarlas del celular.
> - Borrar los archivos **no borra el texto** del chat, pero el archivo puede no volver. Si quien lo envió también lo borró, no podrás descargarlo otra vez. Comprueba la copia antes.
> - Esto copia **archivos multimedia**. No es copia de seguridad ni restauración del historial de chats, y DogNAS no lo promete.

## Por qué WhatsApp ocupa tanto

Por defecto WhatsApp descarga las fotos automáticamente y, según tu configuración, también vídeos y documentos. Los grupos de familia, trabajo y vecinos envían decenas de archivos al día y todo queda en el celular. Con el tiempo la app llega a gigabytes sin que lo notes.

Empieza viendo el tamaño del problema: en WhatsApp abre Ajustes, Almacenamiento y datos, y Administrar almacenamiento. Lista los chats que más ocupan y los archivos grandes o reenviados muchas veces. Los nombres de los menús cambian un poco según la versión.

## Dónde están los archivos

Las rutas dependen de la versión de Android:

| | Android 11 o más nuevo | Android 10 o más antiguo |
|---|---|---|
| WhatsApp | `Android/media/com.whatsapp/WhatsApp/Media` | `WhatsApp/Media` |
| WhatsApp Business | `Android/media/com.whatsapp.w4b/WhatsApp Business/Media` | `WhatsApp Business/Media` |

Dentro de `Media` hay una carpeta por tipo: `WhatsApp Images`, `WhatsApp Video`, `WhatsApp Audio`, `WhatsApp Voice Notes`, `WhatsApp Documents` y una subcarpeta `Sent` con lo que enviaste. Los nombres pueden variar según el idioma y la versión de la app.

> [!note]
> En versiones recientes de Android, el selector de archivos del sistema puede no mostrar `Android/media`. Si te pasa, usa un administrador de archivos para copiarla a una carpeta normal, como Descargas, y envíala desde ahí. En nuestra prueba, en Android 12, el selector de DogNAS Client llegó a `Android/media` sin este paso; no probamos otras versiones ni fabricantes.

## Paso a paso con DogNAS

Necesitas un servidor DogNAS en casa. Un [Android viejo sirve de servidor de archivos](/es/blog/convertir-android-viejo-en-servidor-de-archivos/) y, con un disco o una memoria USB, tienes más espacio. En el celular lleno usa DogNAS Client (o el más ligero DogNAS Client Lite), gratuito.

1. **Mira qué pesa.** En WhatsApp abre Administrar almacenamiento y anota los chats más grandes.
2. **Crea una carpeta en el servidor**, por ejemplo `WhatsApp-2026`, y empareja el celular con el código QR y el PIN del perfil.
3. **Envía los archivos** con Nuevo, Subir. Se abre el selector de archivos del celular: ve a la carpeta, mantén pulsado un archivo, elige "Seleccionar todo" y envía. Repite para cada carpeta (`WhatsApp Images`, `WhatsApp Video` y, si quieres, `Documents`, `Voice Notes` y `Sent`). La subida es por archivos, no por carpeta entera. La cola de transferencias muestra el progreso y se reanuda si el Wi-Fi se corta.
4. **Comprueba en el servidor.** Abre algunas fotos y vídeos y compara el número y el tamaño de los archivos con el celular.
5. **Solo entonces borra del celular**, desde WhatsApp (Administrar almacenamiento) o borrando las carpetas copiadas.


![El selector de archivos de DogNAS Client en una carpeta de prueba con la misma estructura que la de WhatsApp (Android/media/…/WhatsApp/Media/WhatsApp Images), con seis fotos seleccionadas para subir.](assets/blog/whatsapp-media/picker-es.webp)

## Cuidados importantes

- **Comprueba antes de borrar.** Es el paso que evita arrepentirse.
- **Borrar los archivos conserva el texto**, y el chat muestra el archivo como no disponible. A veces puedes descargarlo otra vez y a veces no, según si el archivo sigue disponible para ti. Supón que tu copia puede ser la única.
- **No es una copia de seguridad de WhatsApp.** La copia del historial de chats es la de la propia app (Google Drive). DogNAS guarda los archivos multimedia que copies y no restaura conversaciones.
- **Una sola copia no es seguridad.** DogNAS guarda en el disco que elijas. Para fotos irreemplazables, ten una segunda copia en otro lugar.
- **Solo en tu red.** El envío es por el Wi-Fi de casa, con el servidor encendido y conectado.
- **Espacio en el servidor.** El plan Gratis gestiona hasta 64 GB; los vídeos de grupos suman rápido, así que calcula cuánto necesitas.

## Evita que se vuelva a llenar

- En WhatsApp, en Almacenamiento y datos, deja la descarga automática solo con Wi-Fi o desactívala para vídeos y documentos.
- Silencia la descarga de archivos en grupos grandes.
- Repite la copia de vez en cuando, por ejemplo una vez al mes. Hoy el envío es manual; una copia automática todavía no forma parte de DogNAS.

## Preguntas frecuentes

?? ¿Puedo borrar los archivos sin perder los chats?
Sí. El texto se queda; los archivos borrados aparecen como no disponibles. Por eso se copia y se comprueba antes.

?? ¿DogNAS hace copia de seguridad de WhatsApp?
No. Guarda los archivos multimedia que copies al servidor. La copia del historial de chats sigue siendo la de WhatsApp.

?? ¿Y si el selector no muestra la carpeta de WhatsApp?
En Android nuevos, copia la carpeta a Descargas con un administrador de archivos y envíala desde ahí.

## Resumen

Mira qué ocupa WhatsApp, copia las carpetas de archivos a un servidor tuyo, comprueba y solo entonces borra del celular. Si aún no tienes dónde guardar, empieza por [cómo liberar espacio en el celular Android](/es/blog/como-liberar-espacio-en-el-celular-android/) y [usa un Android viejo como servidor](/es/blog/convertir-android-viejo-en-servidor-de-archivos/).

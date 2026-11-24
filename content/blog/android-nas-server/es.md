---
slug: servidor-nas-android-guia-completa
title: "Servidor NAS en Android: guía completa para tener un NAS en casa con un móvil"
summary: Qué es un servidor NAS en Android, qué necesitas, cómo funciona, qué velocidad tiene de verdad y dónde se queda corto. El mapa de todas las demás guías del sitio.
meta_title: Servidor NAS en Android: guía completa | DogNAS
meta_description: Qué es un servidor NAS en Android, qué necesitas, cómo viajan los archivos, velocidades reales, seguridad y límites. Guía completa para un NAS casero en un móvil, tableta o TV box.
pillar: reuse
tags: [servidor nas, android nas, nas casero, servidor de archivos, sftp, android viejo, tv box]
cta: server
related: [old-android-server, home-nas, nas-vs-android, tv-box-server]
status: review
translation_review: pending
created: 2026-11-24
published: 2026-11-24
updated: 2026-11-24
---
Un servidor NAS en Android es un móvil, una tableta o una TV box Android que se queda en casa, enchufada, guardando tus archivos para que todos los demás dispositivos del Wi-Fi puedan acceder a ellos. NAS son las siglas de almacenamiento conectado a la red: un pequeño servidor en tu red local que solo guarda y entrega archivos. La diferencia es que el equipo es el que ya tienes.

Esta guía es el mapa. Explica qué es un servidor NAS en Android, qué necesitas, cómo viajan los archivos, qué velocidad tiene de verdad, qué lo protege y dónde se queda corto, y señala la guía paso a paso de cada caso. Todo aquí trata de **DogNAS**, la app que convierte el dispositivo en servidor.

> [!takeaways]
> - Un servidor NAS en Android guarda tus archivos **en casa y en tu Wi-Fi**: sin nube y sin cuota mensual por el almacenamiento en sí.
> - Necesitas un dispositivo con **Android 7.0 o posterior**, un cargador, el Wi-Fi de casa y espacio para los archivos: almacenamiento interno, tarjeta SD o unidad USB.
> - Los móviles acceden con la app **DogNAS Client**, por código QR y PIN; los ordenadores, con cualquier programa **SFTP**. No es una carpeta de red de Windows (SMB).
> - La velocidad depende del Wi-Fi y del dispositivo. En una TV box modesta medimos unos **3 MB/s desde un ordenador y de 1 a 1,5 MB/s desde un móvil**, en una red de 5 GHz.
> - **No** sustituye a un NAS completo: no tiene RAID, no ejecuta contenedores y un disco puede fallar. Guarda una copia independiente de lo que importa.

## Qué es un servidor NAS en Android (y qué no es)

Un NAS hace una cosa bien: guarda los archivos en un solo lugar de la casa y los entrega a cualquier dispositivo. Un servidor NAS en Android hace ese trabajo con una app, en lugar de una caja dedicada. Instala DogNAS en el dispositivo, elige dónde se guardan los archivos y pulsa Iniciar. Desde ese momento el dispositivo responde en tu red doméstica.

Es un **servidor de archivos**, no un mini centro de datos. No hay contenedores, apps de contenido multimedia ni conjuntos de discos. Para fotos, vídeos, documentos, trabajos del colegio y «pásame esto a mi ordenador», basta. Para datos irreemplazables en un solo sitio, o mucha gente viendo vídeo a la vez, no basta.

| | NAS en Android con DogNAS | NAS comprado ya hecho |
|---|---|---|
| Equipo | El Android que ya tienes | Una caja nueva, normalmente con discos |
| Varios discos como uno solo (RAID) | No: cada disco es un almacenamiento aparte | Sí, en muchos modelos |
| Cómo se conectan los dispositivos | DogNAS Client en los móviles; programas SFTP en los ordenadores | Normalmente una carpeta de red (SMB) y la app del fabricante |
| Configuración | Instalar la app, elegir una carpeta y pulsar Iniciar | Instalar los discos y configurar el sistema |
| Servicios extra | Solo servidor de archivos | A menudo apps, contenedores y servidores multimedia |
| Energía | Un cargador, como cualquier móvil | Una fuente de alimentación dedicada |

Si aún dudas entre los dos, lee [NAS tradicional o servidor Android](/es/blog/nas-tradicional-o-servidor-android/) y [NAS casero sin comprar un NAS](/es/blog/nas-casero-sin-comprar-un-nas/).

## Qué necesitas

- **Un dispositivo con Android 7.0 o posterior** que se quedará en casa como servidor: un móvil viejo, una tableta o una TV box Android.
- **El Wi-Fi de casa.** El servidor y los dispositivos que lo usan deben estar en la misma red. El servidor no necesita internet para mover archivos; solo la necesitas para instalar las apps.
- **Espacio para los archivos.** El almacenamiento interno del dispositivo, una tarjeta SD, o una unidad USB o disco duro. Las unidades USB necesitan un dispositivo con USB OTG.
- **Un cargador.** El servidor funciona mejor enchufado y lejos del sol directo.
- **Un móvil desde el que usarlo.** DogNAS Client está en Google Play para Android; la versión para iPhone aún no ha salido.

¿Móvil, tableta o TV box? El móvil es la opción más común. La tableta ofrece una pantalla que muestra el panel del servidor de un vistazo: mira [tableta vieja como almacenamiento del hogar](/es/blog/tablet-viejo-como-almacenamiento-del-hogar/). La TV box está encendida todo el día y tiene puertos USB: mira [TV box Android como NAS casero](/es/blog/tv-box-android-como-servidor-de-archivos/), escrita a partir de una prueba en una caja real.

## Cómo funciona

Tres partes se hablan entre sí:

1. **La app servidor (DogNAS)** se ejecuta en el Android de casa. Guarda los archivos en el almacenamiento que elegiste y responde por tu red.
2. **Los perfiles.** Cada persona de la casa recibe un perfil con su PIN y sus carpetas, y nadie ve los archivos de los demás.
3. **Los clientes.** En el móvil, **DogNAS Client** permite navegar, subir y descargar. En el ordenador, un programa SFTP corriente, como FileZilla, WinSCP o Cyberduck, hace lo mismo.

Los archivos viajan por **SFTP**, que funciona dentro de una conexión SSH cifrada. Por eso el ordenador necesita un programa SFTP en lugar de «Red» en el explorador de archivos: DogNAS no es una carpeta de red de Windows (SMB). Si el término es nuevo, [qué es SFTP](/es/blog/que-es-sftp-acceder-servidor-android/) lo explica con palabras sencillas, y [cómo acceder a DogNAS con FileZilla, WinSCP y Cyberduck](/es/blog/acceder-a-dognas-con-filezilla-winscp-cyberduck-rclone/) muestra cada programa.

![Un servidor DogNAS con un disco duro externo en una base USB, al que se accede desde el móvil.](assets/photos/usb-drive.webp)

## Configúralo en cinco pasos

1. **Instala DogNAS en el dispositivo que será el servidor.**
2. **Elige dónde se guardan los archivos** y pulsa Iniciar. El servidor ya funciona en tu red.
3. **Crea un perfil y un PIN de 4 dígitos** para cada persona.
4. **Muestra el código QR del perfil.** La app servidor también tiene un botón con un segundo código QR que lleva el otro móvil a la página de DogNAS Client, y la app queda a un escaneo de distancia.
5. **En el móvil, abre DogNAS Client**, apunta la cámara al código QR del perfil y escribe el PIN.

El recorrido completo, con pantallas, está en [cómo convertir un Android viejo en servidor NAS](/es/blog/convertir-android-viejo-en-servidor-de-archivos/).

![Servidor DogNAS en línea, con una transferencia en curso](assets/shots/es/server-status.webp)
![Código QR del perfil para conectar el móvil](assets/shots/es/server-qr.webp)
![Archivos en DogNAS Client](assets/shots/es/client-files.webp)

## ¿Qué velocidad tiene de verdad?

Depende de dos cosas que puedes comprobar antes de empezar: tu Wi-Fi y el dispositivo.

La velocidad la limitan la **red Wi-Fi y el procesador del dispositivo**, no el disco. En una TV box con un procesador débil, en una red de 5 GHz, medimos unos **3 MB/s desde un ordenador y de 1 a 1,5 MB/s desde un móvil**. Eso sirve para documentos, fotos y copias de seguridad corrientes; es lento si piensas mover una biblioteca grande de vídeos cada día. Un móvil más nuevo, con un procesador más fuerte y buena señal de 5 GHz, irá mejor, así que revisa las especificaciones de tu dispositivo.

Para sacar más de una transferencia: deja el servidor cerca del router, prefiere la red de 5 GHz y mantén el servidor enchufado. La pestaña Monitor del servidor muestra la velocidad y los clientes conectados en tiempo real.

![Monitor del servidor: clientes y velocidad en tiempo real](assets/shots/es/server-monitor.webp)

## Seguridad y privacidad

- **Sin nube.** Los archivos se quedan en el dispositivo, y DogNAS no los envía a ningún servidor de DogNAS.
- **Transferencia cifrada.** Los archivos viajan por SSH/SFTP a través de tu red.
- **Un PIN por perfil.** Tras varios PIN incorrectos, los intentos se bloquean durante unos minutos.
- **El cliente recuerda la identidad del servidor.** Si la identidad cambia, DogNAS Client te avisa y te pide emparejar de nuevo.

DogNAS está pensado para tu **red local**. No está pensado para abrirse a internet. Mantén en privado la contraseña del Wi-Fi y trata el PIN como cualquier otra contraseña. Ninguna herramienta lo protege todo, así que guarda una copia independiente de lo que importa.

## Lo que no hace

- **Sin RAID.** Cada disco es un almacenamiento aparte. DogNAS no une varios discos en un solo volumen, y un disco puede fallar.
- **Sin copias de seguridad por su cuenta.** Almacenamiento no es copia de seguridad. Para los archivos que no puedes perder, guarda una copia en otro sitio.
- **Sin carpeta de red para Windows o Mac.** Los ordenadores usan un programa SFTP.
- **Depende del dispositivo.** Algunos fabricantes limitan las apps en segundo plano para ahorrar batería, y las unidades USB necesitan USB OTG. Si el servidor se detiene solo, revisa los ajustes de batería del dispositivo.
- **No es un centro multimedia.** Guarda y entrega archivos; no ejecuta otras apps por ti.

## Plan Gratis y Pro

En el plan Gratis DogNAS gestiona hasta **64 GB**, con el perfil Casa más dos perfiles y hasta tres dispositivos emparejados. **DogNAS Pro** es una compra única, sin suscripción, y desbloquea todo el almacenamiento del dispositivo, entre otras cosas. Si necesitas más espacio antes, conecta una tarjeta SD o una unidad USB.

## Adónde ir ahora

- Decidir: [NAS tradicional o servidor Android](/es/blog/nas-tradicional-o-servidor-android/).
- Montar: [Android viejo como servidor NAS](/es/blog/convertir-android-viejo-en-servidor-de-archivos/), [tableta vieja](/es/blog/tablet-viejo-como-almacenamiento-del-hogar/), [TV box](/es/blog/tv-box-android-como-servidor-de-archivos/), [disco de portátil como almacenamiento](/es/blog/reutilizar-disco-de-laptop-como-almacenamiento/).
- Usar: [pasar archivos entre PC y móvil por Wi-Fi](/es/blog/transferir-archivos-entre-pc-y-celular-por-wifi/).

?? ¿Necesito internet para usar un servidor NAS en Android?
No. El servidor y tus dispositivos solo necesitan estar en el mismo Wi-Fi. Necesitas internet para instalar las apps y, si quieres, para comprar Pro.

?? ¿Puedo verlo como una unidad de red en Windows o en Mac?
No. A DogNAS se accede por SFTP, no como carpeta de red (SMB). Usa un programa SFTP corriente, como FileZilla, WinSCP o Cyberduck, o la app DogNAS Client en Android.

?? ¿Qué versiones de Android funcionan?
Android 7.0 o posterior, en un móvil, una tableta o una TV box. Algunos fabricantes limitan las apps en segundo plano, así que revisa los ajustes de batería del dispositivo si el servidor se detiene.

?? ¿Puedo usar una tableta o una TV box en lugar de un móvil?
Sí. Mira las guías de la [tableta vieja](/es/blog/tablet-viejo-como-almacenamiento-del-hogar/) y de la [TV box Android](/es/blog/tv-box-android-como-servidor-de-archivos/).

?? ¿Puedo guardar los archivos en una tarjeta SD o en una unidad USB?
Sí. Puedes elegir el almacenamiento interno, una tarjeta SD o una unidad USB o disco duro. Las unidades USB necesitan un dispositivo con USB OTG.

?? ¿Un servidor NAS en Android es una copia de seguridad?
No. Almacenamiento no es copia de seguridad, y DogNAS no hace copias por su cuenta. Guarda una copia independiente de lo que no puedes perder.

?? ¿Es gratis?
El plan Gratis gestiona hasta 64 GB, con el perfil Casa más dos y hasta tres dispositivos emparejados. DogNAS Pro es una compra única, sin suscripción, y elimina esos límites.

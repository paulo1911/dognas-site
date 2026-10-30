---
slug: nas-casero-sin-comprar-un-nas
title: Un NAS casero sin comprar un NAS: usa el Android que ya tienes
summary: Para guardar en casa las fotos, los videos y los documentos de la familia no siempre hace falta comprar un NAS. Mira cuándo basta un Android viejo y cuándo no.
meta_title: NAS casero sin comprar un NAS: usa un Android | DogNAS
meta_description: Arma un NAS casero con un Android viejo, sin comprar equipo y sin mensualidad. Mira qué hace bien, sus límites y cuándo conviene comprar un NAS.
pillar: compare
tags: [nas casero, android viejo, servidor de archivos, almacenamiento]
cover: assets/blog/home-nas/cover-es.webp
cover_alt: Ilustración de una casa con una caja de almacenamiento junto a la pantalla del DogNAS Client Lite
social_image: assets/blog/home-nas/social-es.jpg
cta: server
related: [old-android-server, old-phone-ideas]
status: published
translation_review: reviewed
created: 2026-10-28
published: 2026-10-28
updated: 2026-10-28
---
Un NAS (almacenamiento conectado a la red) es un pequeño servidor que guarda tus archivos y se los entrega a cualquier dispositivo de la casa por Wi-Fi. Es la idea correcta para quien se cansó de los pendrives, del celular sin espacio y de las mensualidades de la nube. El problema es que un NAS comercial con disco cuesta dinero y requiere algo de configuración.

Si lo que necesitas es guardar y acceder a las fotos, los videos y los documentos de la familia, hay un camino más simple: usar un celular o tablet Android que ya te sobra.

## Qué hace un NAS en casa

En la práctica, la mayoría de las personas usa un NAS para cuatro cosas:

- guardar fotos y videos en un solo lugar, dentro de casa;
- abrir los mismos archivos en el celular, en la tablet y en la computadora;
- pasar archivos entre dispositivos sin cables y sin enviarte correos a ti mismo;
- liberar espacio en el celular sin depender de una nube de pago.

Para esas tareas, un servidor de archivos simple es suficiente. No necesitas RAID, contenedores ni un equipo dedicado.

## Tres formas de tener un NAS casero

- **Comprar un NAS ya armado.** Es la opción más completa: varios discos, más funciones y soporte del fabricante. También es la más cara y la que más configuración pide.
- **Armarlo con una computadora vieja o una placa como Raspberry Pi.** Da más control, pero hay que instalar y mantener un sistema.
- **Usar un Android viejo con DogNAS.** Instalas una app, eliges dónde guardar los archivos, tocas Iniciar y conectas los demás dispositivos con un código QR y un PIN. Sin tocar el router.

## Cómo queda con DogNAS

DogNAS convierte un celular o tablet con Android 7.0 o más reciente en un servidor de archivos en tu red Wi-Fi. Cada persona de la casa tiene un perfil con PIN y carpetas propias. Los archivos quedan en la memoria del dispositivo, en una tarjeta SD o en un disco/pendrive USB, y viajan cifrados (SSH/SFTP) por tu red, sin pasar por una nube.

En la computadora, usa programas comunes como FileZilla, WinSCP y Cyberduck. En el celular, usa DogNAS Client Lite para ver, subir y descargar archivos.

![Servidor DogNAS con un disco duro externo en un dock USB, al que se accede desde el celular.](assets/photos/usb-drive.webp)
![Monitor del servidor: clientes y velocidad en tiempo real](assets/shots/es/server-monitor.webp)
![Archivos de DogNAS en Client Lite](assets/shots/es/lite-files.webp)

## Lo que un Android no hace (y cuándo comprar un NAS)

Un celular no reemplaza a un NAS completo, y conviene ser honestos al respecto:

- **No tiene RAID.** Cada disco es un almacenamiento independiente. DogNAS no junta varios discos en un único volumen, y un disco puede fallar. Mantén una copia independiente de lo importante.
- **No ejecuta contenedores ni servicios avanzados.** Es un servidor de archivos, no un mini centro de datos.
- **Depende del dispositivo.** Algunos fabricantes limitan las apps en segundo plano para ahorrar batería, y los discos USB requieren USB OTG. Revisa los requisitos antes de empezar.
- **Límites de espacio en el plan Gratis:** hasta 64 GB administrados. DogNAS Pro, una compra única y sin suscripción, libera todo el almacenamiento del dispositivo.

Si en tu casa muchas personas transmiten video a la vez, necesitas redundancia de discos o vas a guardar datos irremplazables en un solo lugar, un NAS dedicado es la elección correcta.

## Para quién basta un Android viejo

Para la mayoría de los hogares, que solo quieren fotos, videos y documentos en un lugar seguro, el Android que ya está en el cajón resuelve, sin costo extra de equipo.

Saca el dispositivo, instala el servidor y conecta tu celular. En pocos minutos, tienes un NAS casero.

---
slug: convertir-android-viejo-en-servidor-de-archivos
title: Cómo convertir un Android viejo en un servidor de archivos
summary: Ese celular o tablet guardado en un cajón puede almacenar las fotos, los videos y los documentos de la casa por Wi-Fi, sin nube y sin mensualidad.
meta_title: Convierte un Android viejo en servidor de archivos | DogNAS
meta_description: Guía paso a paso para usar un celular o tablet Android viejo como servidor de archivos en el Wi-Fi de casa, sin nube y sin mensualidad, con DogNAS.
pillar: reuse
tags: [android viejo, servidor de archivos, nas casero, sftp]
cover: assets/blog/old-android-server/cover-es.webp
cover_alt: Ilustración de un celular con Wi-Fi junto a la pantalla del servidor DogNAS
social_image: assets/blog/old-android-server/social-es.jpg
cta: server
related: [home-nas, old-phone-ideas]
status: published
translation_review: reviewed
created: 2026-10-28
published: 2026-10-28
updated: 2026-10-28
---
Casi todos tenemos un celular o una tablet Android guardado en un cajón. Todavía enciende, se conecta al Wi-Fi y tiene espacio de sobra. En lugar de dejarlo parado, puedes convertirlo en un pequeño servidor de archivos para tu casa: un lugar para guardar y acceder a fotos, videos y documentos por la red, sin nube y sin mensualidad.

Esta guía muestra el camino completo con **DogNAS**, una app gratuita que hace que el dispositivo funcione como servidor de archivos en tu red Wi-Fi local.

![Un Android viejo, conectado a la corriente, funcionando como servidor DogNAS en casa.](assets/photos/always-on.webp)
![Un servidor DogNAS con un disco duro externo en un dock USB, al que se accede desde el celular.](assets/photos/usb-drive.webp)

## Qué necesitas

- Un celular o tablet con **Android 7.0 o más reciente**, que se quedará en casa como servidor.
- El Wi-Fi de tu casa. El servidor y los dispositivos que accederán a los archivos deben estar en la misma red.
- Espacio para los archivos: la memoria interna del dispositivo, una tarjeta SD o un disco/pendrive USB (los discos USB requieren un dispositivo con USB OTG).
- Un cargador, porque el servidor funciona mejor conectado a la corriente.

## Paso a paso

1. **Instala DogNAS en el Android viejo.** Es el dispositivo que guardará los archivos. La app está en Google Play.
2. **Elige dónde guardar los archivos** y toca Iniciar. El servidor empieza a funcionar en la red de tu casa.
3. **Crea un perfil para cada persona.** Cada perfil tiene su PIN y sus carpetas, y nadie ve los archivos de los demás.
4. **Conecta tu celular.** En el servidor, genera el código QR del perfil. En el celular que usará los archivos, abre DogNAS Client Lite, apunta la cámara al código QR e ingresa el PIN.
5. **Úsalo día a día.** Navega por las carpetas, sube fotos y videos y descarga lo que necesites por el Wi-Fi de casa.

Para acceder desde la computadora no necesitas una app especial: DogNAS habla SFTP, así que programas como FileZilla, WinSCP, Cyberduck y el `sftp` de OpenSSH funcionan.

## Sigue todo sin complicaciones

El servidor muestra en tiempo real los clientes conectados y la velocidad de las transferencias. En el celular, Client Lite mantiene la cola de envíos y descargas, y reutilizas el dispositivo viejo en pocos minutos.

## Cuánto espacio tienes

En el plan Gratis, DogNAS administra hasta 64 GB, con el perfil Casa y 2 perfiles más, y hasta 3 dispositivos vinculados. DogNAS Pro es una compra única, sin suscripción, y libera todo el almacenamiento del dispositivo. Si necesitas más espacio, conecta una tarjeta SD o un disco USB.

## Qué considerar antes de empezar

- **Depende del dispositivo.** Algunos fabricantes limitan las apps en segundo plano para ahorrar batería. Si el servidor se detiene solo, revisa la configuración de batería del dispositivo y los requisitos de compatibilidad.
- **Un disco puede fallar.** DogNAS guarda los archivos en el almacenamiento que elegiste y no hace copias de seguridad por su cuenta. Para archivos importantes, mantén una copia independiente.
- **Varios discos no se vuelven uno.** Cada disco es un almacenamiento separado; DogNAS no junta varios discos en un único volumen.
- **Red local.** El acceso depende de la configuración de tu red y de las credenciales de DogNAS. Los archivos viajan cifrados (SSH/SFTP) por tu red, sin pasar por una nube.

## Mira lo simple que es

Capturas de pantalla reales de la app: el servidor encendido, el código QR del perfil y los archivos en el celular.

![Servidor DogNAS en línea, con una transferencia en curso](assets/shots/es/server-status.webp)
![Código QR del perfil para conectar el celular](assets/shots/es/server-qr.webp)
![Archivos de DogNAS en Client Lite](assets/shots/es/lite-files.webp)
![Monitor del servidor: clientes y velocidad en tiempo real](assets/shots/es/server-monitor.webp)
![Cola de transferencias en el celular](assets/shots/es/lite-transfers.webp)

## Próximo paso

Saca el Android viejo, instala el servidor y conecta tu celular. En pocos minutos, ese cajón se convierte en el almacenamiento de la casa.

---
slug: transferir-archivos-entre-pc-y-celular-por-wifi
title: Cómo transferir archivos entre la PC y el celular por Wi-Fi, sin cable
summary: Cable, nube, apps o un servidor propio en casa: las formas de pasar archivos de la PC al celular y viceversa, y cuándo conviene cada una.
meta_title: Transferir archivos entre PC y celular por Wi-Fi | DogNAS
meta_description: Cómo pasar archivos de la PC al celular y del celular a la PC por Wi-Fi, sin cable y sin nube: comparación de métodos y paso a paso con DogNAS.
pillar: storage
tags: [transferir archivos, pc y celular, wi-fi, sftp]
cover: assets/blog/pc-phone-transfer/cover-es.webp
cover_alt: Ilustración de una computadora y un celular intercambiando archivos junto a la pantalla del DogNAS Client Lite
social_image: assets/blog/pc-phone-transfer/social-es.jpg
cta: both
related: [old-android-server, home-nas, free-phone-space]
status: published
translation_review: reviewed
created: 2026-10-28
published: 2026-10-28
updated: 2026-10-28
---
Pasar un archivo de la computadora al celular, o del celular a la computadora, parece simple hasta que tienes que hacerlo cada semana. Un cable que nunca está a mano, enviarte correos a ti mismo, una nube llena. Hay una forma de hacerlo por el Wi-Fi de casa, directamente, sin cable y sin depender de una cuenta.

## Las formas más comunes

- **Cable USB.** Funciona sin red y es rápido, pero necesitas el cable, el permiso en el celular y el dispositivo junto a la computadora.
- **Servicios en la nube.** Subes a la nube y descargas en el otro dispositivo. Es práctico, pero usa internet, ocupa espacio de tu cuenta y el archivo pasa por servidores de terceros.
- **Apps que abren el celular en el navegador de la PC.** Sin cable, pero tienes que abrir la app cada vez, y la conexión suele caerse cuando la pantalla se apaga.
- **Bluetooth y Wi-Fi Direct.** Sirven para archivos pequeños y sueltos, y varían mucho de un dispositivo a otro.
- **Un servidor de archivos propio en casa.** Un dispositivo queda encendido en la red y todos los demás acceden a las mismas carpetas. Es el único que configuras una vez y usas siempre.

## Cómo hacerlo con DogNAS

DogNAS convierte un celular o tablet Android (7.0 o más reciente) en un servidor de archivos en el Wi-Fi de tu casa. La PC y el celular acceden a las mismas carpetas, y los archivos viajan cifrados (SSH/SFTP) por tu red, sin pasar por una nube.

1. **Instala el servidor** en el Android que guardará los archivos y toca Iniciar.
2. **Crea un perfil** para ti, con PIN y carpetas propias.
3. **En el celular,** abre DogNAS Client Lite, apunta la cámara al código QR del perfil e ingresa el PIN. Sube y descarga archivos desde la cola de transferencias.
4. **En la PC,** abre un cliente SFTP como FileZilla, WinSCP o Cyberduck y usa los datos de conexión que el servidor muestra en la pantalla "Cómo conectar tu PC o iPhone". Arrastra los archivos entre las ventanas.

Listo: lo que pones en el servidor desde la PC aparece en el celular, y lo que el celular sube aparece en la PC. Funciona en los dos sentidos, sin cable y sin abrir una app cada vez.

![Cola de transferencias en el celular](assets/shots/es/lite-transfers.webp)
![Código QR del perfil para conectar el celular](assets/shots/es/server-qr.webp)
![Monitor del servidor: clientes y velocidad en tiempo real](assets/shots/es/server-monitor.webp)

## Qué considerar

- **Misma red.** La PC y el celular deben estar en el Wi-Fi de casa, igual que el servidor.
- **Velocidad.** Depende de la calidad de tu Wi-Fi y del dispositivo que hace de servidor.
- **Servidor encendido.** El dispositivo debe quedar encendido y conectado; algunos fabricantes limitan las apps en segundo plano, así que revisa los requisitos.
- **Copia de seguridad.** DogNAS guarda los archivos en el almacenamiento que elegiste y no hace copias por su cuenta. Mantén una copia independiente de lo importante.

## Cuándo conviene

Si pasas archivos entre dispositivos de vez en cuando, el cable resuelve. Si lo haces siempre, o quieres que toda la familia acceda a las mismas carpetas, un servidor propio en casa ahorra tiempo y espacio de nube. Para ver qué más hace, lee [cómo convertir un Android viejo en un servidor de archivos](/es/blog/convertir-android-viejo-en-servidor-de-archivos/).

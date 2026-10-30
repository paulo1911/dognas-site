---
slug: acceder-a-dognas-con-filezilla-winscp-cyberduck-rclone
title: Cómo acceder a DogNAS con FileZilla, WinSCP, Cyberduck y rclone
summary: Paso a paso para conectar tu servidor DogNAS a cuatro programas SFTP populares y elegir el mejor para tu uso.
meta_title: Acceder a DogNAS con FileZilla, WinSCP, Cyberduck | DogNAS
meta_description: Cómo conectar el servidor DogNAS a FileZilla, WinSCP, Cyberduck y rclone por SFTP, qué completar en cada uno y cuál elegir.
pillar: sftp
tags: [filezilla, winscp, cyberduck, rclone, sftp]
cover: assets/blog/sftp-clients/cover-es.webp
cover_alt: Ilustración de una ventana de terminal junto a la pantalla del DogNAS Client Lite
social_image: assets/blog/sftp-clients/social-es.jpg
cta: both
related: [sftp-explained, pc-phone-transfer, old-android-server]
status: published
translation_review: reviewed
created: 2026-10-28
published: 2026-10-28
updated: 2026-10-28
---
DogNAS habla SFTP, así que cualquier programa que entienda ese protocolo puede acceder a los archivos de tu servidor. Esta guía muestra cómo conectar cuatro de los más usados y te ayuda a elegir. Si todavía no sabes qué es SFTP, empieza por [qué es SFTP](/es/blog/que-es-sftp-acceder-servidor-android/).

## Antes de nada: los datos de conexión

En cualquier programa necesitarás el mismo conjunto de datos: **dirección del servidor (host), puerto, usuario y contraseña**. El servidor DogNAS los muestra en la pantalla "Cómo conectar tu PC o iPhone". La computadora debe estar en la misma red Wi-Fi que el servidor, y el servidor debe estar encendido.

En la primera conexión, el programa muestra la **huella digital (fingerprint)** de la clave del servidor y te pide que confíes en ella. Acepta cuando el dispositivo sea tuyo. Si después cambia sin motivo, desconfía.

## FileZilla (Windows, Mac y Linux)

El más conocido, y funciona en los tres sistemas.

1. Abre el Gestor de Sitios y crea un sitio nuevo.
2. En Protocolo, elige **SFTP**.
3. Completa host, puerto, usuario y contraseña con los datos del servidor.
4. Conecta y arrastra archivos entre el lado de la computadora y el del servidor.

## WinSCP (Windows)

Tiene una interfaz parecida al Explorador de archivos y es bueno si solo usas Windows.

1. En la pantalla de inicio de sesión, elige **SFTP** como protocolo de archivo.
2. Completa nombre de host, puerto, usuario y contraseña.
3. Guarda la sesión y conecta.

## Cyberduck (Windows y Mac)

Simple y visual, popular entre quienes usan Mac.

1. Haz clic en Abrir conexión y elige **SFTP** en la lista.
2. Completa servidor, puerto, usuario y contraseña.
3. Conecta y navega por las carpetas como en un explorador de archivos.

## rclone (línea de comandos)

Para quien le gusta la automatización y los scripts.

1. Ejecuta `rclone config`, crea un remoto nuevo y elige el tipo **sftp**.
2. Indica host, puerto, usuario y contraseña.
3. Usa comandos como `rclone ls` y `rclone copy` para listar y copiar archivos entre la computadora y el servidor.

## Cuál elegir

- **Quieres lo más simple en Mac:** Cyberduck.
- **Usas Windows y quieres algo parecido al Explorador:** WinSCP.
- **Usas más de un sistema:** FileZilla.
- **Quieres automatizar copias:** rclone.

![Pantalla de inicio de DogNAS Client Lite](assets/shots/es/lite-home.webp)
![Archivos de DogNAS en Client Lite](assets/shots/es/lite-files.webp)
![Cola de transferencias en el celular](assets/shots/es/lite-transfers.webp)

## Precauciones

- **Contraseña y PIN.** No compartas los datos de conexión. Puedes revocar la credencial de un dispositivo cuando quieras.
- **No es una copia de seguridad.** Copiar al servidor guarda los archivos en otro lugar, pero DogNAS no hace copias por sí solo. Mantén una copia independiente de lo importante.
- **En el celular,** usa DogNAS Client Lite, con código QR y PIN, en lugar de un cliente SFTP genérico.

Para armar el servidor, mira [cómo convertir un Android viejo en un servidor de archivos](/es/blog/convertir-android-viejo-en-servidor-de-archivos/).

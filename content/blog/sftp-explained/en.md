---
slug: what-is-sftp-access-android-server
title: What is SFTP, and how to access a file server on Android
summary: SFTP is a secure way to send and fetch files over a network. Learn what it is, what it is for and how to reach your DogNAS server from a PC and a phone.
meta_title: What is SFTP and how to access an Android server | DogNAS
meta_description: What SFTP is, why it is secure and how to access a file server on Android with FileZilla, WinSCP, Cyberduck and other clients.
pillar: sftp
tags: [sftp, ssh, filezilla, winscp, file server]
cover: assets/blog/sftp-explained/cover-en.webp
cover_alt: Illustration of a padlock next to the DogNAS server screen
social_image: assets/blog/sftp-explained/social-en.jpg
cta: server
related: [old-android-server, pc-phone-transfer, nas-vs-android]
status: published
translation_review: reviewed
created: 2026-10-28
published: 2026-10-28
updated: 2026-10-28
---
If you have seen "SFTP" somewhere and scrolled past, this guide is for you. The acronym looks scary, but the idea is simple: a secure way to send and fetch files on another computer over the network. It is what DogNAS uses to hand the files on your server to the other devices at home.

## What SFTP is

SFTP stands for *SSH File Transfer Protocol*: file transfer over SSH. SSH is the protocol that creates an **encrypted** connection between two devices. SFTP uses that connection to list folders, upload, download, rename and delete files.

In practice, this means that what travels over the network cannot be read by other devices on the same Wi-Fi.

## SFTP, FTP and SMB: what is the difference?

- **FTP** is old and, by default, sends everything unencrypted, including the password. It is not the best choice on any network.
- **SFTP** looks like FTP to the user, but it runs over SSH and is encrypted. It has no technical relation to FTP, despite the similar name.
- **SMB** is Windows folder sharing. It is handy on a local network, but is often more annoying to set up outside Windows.

## What it is for at home

- keeping and reaching photos, videos and documents on a home server;
- sending files from the PC to the phone and back;
- receiving files from cameras, NVRs and automations that send over SFTP;
- copying files from other computers with scripts and tools such as rclone.

## How to access an Android server with DogNAS

DogNAS turns an Android phone or tablet (7.0 or newer) into an SFTP server on your Wi-Fi network. Each device gets its own credential, which you can revoke at any time, and the server's key is pinned at pairing, so you know you are talking to the right server.

1. **Install and start the server** on the Android that will keep the files.
2. **On the phone,** use DogNAS Client Lite: point the camera at the profile's QR Code and type the PIN.
3. **On the computer,** open an SFTP client such as FileZilla, WinSCP or Cyberduck and use the connection details the server shows on its "how to connect your PC or iPhone" screen.
4. Browse, drag and drop files. For automations, tools such as rclone and OpenSSH's `sftp` also work.

![Profile QR Code to connect the phone](assets/shots/en/server-qr.webp)
![Server monitor: clients and speed in real time](assets/shots/en/server-monitor.webp)
![DogNAS files in Client Lite](assets/shots/en/lite-files.webp)

## What SFTP doesn't do

- **It is not a backup.** It only carries files. Keep an independent copy of what matters.
- **It only works if the network allows it.** The server and your device must be on the same network, and the server must be on.
- **Encrypting the path doesn't protect the server.** Use a PIN and strong passwords, and revoke credentials of devices you no longer use.

## In short

SFTP is a secure, universal way to reach files over the network, and almost every transfer program understands it. With DogNAS you get an SFTP server on Android without touching the router. For the complete walkthrough, read [how to turn an old Android into a file server](/en/blog/turn-old-android-into-file-server/).

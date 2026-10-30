---
slug: access-dognas-with-filezilla-winscp-cyberduck-rclone
title: How to access DogNAS with FileZilla, WinSCP, Cyberduck and rclone
summary: Step-by-step to connect your DogNAS server to four popular SFTP programs and choose the best one for how you work.
meta_title: Access DogNAS with FileZilla, WinSCP, Cyberduck | DogNAS
meta_description: How to connect the DogNAS server to FileZilla, WinSCP, Cyberduck and rclone over SFTP, what to fill in on each one and which to choose.
category: Guides
tags: [filezilla, winscp, cyberduck, rclone, sftp]
cover: assets/blog/sftp-clients/cover-en.webp
cover_alt: DogNAS Client Lite home screen on an Android, next to the DogNAS mascot
social_image: assets/blog/sftp-clients/social-en.jpg
cta: both
related: [sftp-explained, pc-phone-transfer, old-android-server]
status: published
translation_review: reviewed
created: 2026-10-28
published: 2026-10-28
updated: 2026-10-28
---
DogNAS speaks SFTP, so any program that understands that protocol can reach the files on your server. This guide shows how to connect four of the most used ones and helps you choose. If you don't yet know what SFTP is, start with [what SFTP is](/en/blog/what-is-sftp-access-android-server/).

## First: the connection details

In any program you will need the same set of information: **server address (host), port, username and password**. The DogNAS server shows these on its "how to connect your PC or iPhone" screen. The computer must be on the same Wi-Fi network as the server, and the server must be on.

On the first connection, the program shows the **fingerprint** of the server's key and asks you to trust it. Accept when the device is yours. If it changes later for no reason, be suspicious.

## FileZilla (Windows, Mac and Linux)

The best known, and it works on all three systems.

1. Open the Site Manager and create a new site.
2. Under Protocol, choose **SFTP**.
3. Fill in host, port, username and password with the server's details.
4. Connect and drag files between the computer side and the server side.

## WinSCP (Windows)

It has an interface similar to File Explorer and is good if you only use Windows.

1. On the login screen, choose **SFTP** as the file protocol.
2. Fill in host name, port, username and password.
3. Save the session and connect.

## Cyberduck (Windows and Mac)

Simple and visual, popular among Mac users.

1. Click Open Connection and choose **SFTP** from the list.
2. Fill in server, port, username and password.
3. Connect and browse the folders like a file browser.

## rclone (command line)

For people who like automation and scripts.

1. Run `rclone config`, create a new remote and choose the **sftp** type.
2. Enter host, port, username and password.
3. Use commands such as `rclone ls` and `rclone copy` to list and copy files between the computer and the server.

## Which to choose

- **Want the simplest on a Mac:** Cyberduck.
- **Use Windows and want something like File Explorer:** WinSCP.
- **Use more than one system:** FileZilla.
- **Want to automate copies:** rclone.

![DogNAS Client Lite home screen](assets/shots/en/lite-home.webp)
![DogNAS files in Client Lite](assets/shots/en/lite-files.webp)
![Transfer queue on the phone](assets/shots/en/lite-transfers.webp)

## Precautions

- **Password and PIN.** Don't share the connection details. You can revoke a device's credential whenever you want.
- **Not a backup.** Copying to the server keeps the files somewhere else, but DogNAS does not back up on its own. Keep an independent copy of what matters.
- **On the phone,** use DogNAS Client Lite, with a QR Code and a PIN, instead of a generic SFTP client.

To set up the server, see [how to turn an old Android into a file server](/en/blog/turn-old-android-into-file-server/).

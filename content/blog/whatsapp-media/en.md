---
slug: whatsapp-filling-your-phone-free-up-space
title: WhatsApp filling your phone: how to move photos and videos out without losing your chats
summary: WhatsApp is often the biggest space hog on Android. Where its media lives, how to copy it to a server of your own at home, and only then delete it from the phone.
meta_title: WhatsApp filling your phone: free up space | DogNAS
meta_description: WhatsApp filled your Android? See where its media lives, how to copy it to your own home server with DogNAS and free up space without deleting your chats.
pillar: storage
tags: [whatsapp, free up space, storage, android, photos and videos]
cover: assets/blog/free-phone-space/cover-en.webp
cover_alt: Illustration of a phone with an arrow taking files out, next to the DogNAS Client Lite screen
social_image: assets/blog/free-phone-space/social-en.jpg
cta: client
related: [free-phone-space, old-android-server, pc-phone-transfer]
status: review
translation_review: pending
created: 2026-11-01
updated: 2026-11-01
---
**WhatsApp fills your phone because it keeps every photo, video, voice note and document that passes through your groups on the device**, even the ones you never opened. The way out that keeps what matters is to copy that media to a place of your own, check it, and only then delete it from the phone. Your text conversations stay in the app.

> [!takeaways]
> - The media sits in ordinary folders on the phone that you can copy. Android 11 or newer: `Android/media/com.whatsapp/WhatsApp/Media`. Android 10 or older: `WhatsApp/Media`.
> - You can copy those folders to a server of your own at home with DogNAS, with no cloud and no monthly fee, and then delete them from the phone.
> - Deleting media **keeps the chat text**, but the file may not come back. If the sender deleted it too, you cannot download it again. Check your copy first.
> - This copies **media files**. It is not a backup or restore of your chat history, and DogNAS does not promise that.

## Why WhatsApp takes so much space

By default WhatsApp downloads photos automatically and, depending on your settings, videos and documents too. Family, work and neighbourhood groups send dozens of files a day, and all of it stays on the phone. Over time the app grows to gigabytes without you noticing.

Start by seeing the size of the problem: in WhatsApp open Settings, Storage and data, then Manage storage. It lists the chats that use the most space and the large files or those forwarded many times. Menu names change a little between versions.

## Where the media lives

The paths depend on your Android version:

| | Android 11 or newer | Android 10 or older |
|---|---|---|
| WhatsApp | `Android/media/com.whatsapp/WhatsApp/Media` | `WhatsApp/Media` |
| WhatsApp Business | `Android/media/com.whatsapp.w4b/WhatsApp Business/Media` | `WhatsApp Business/Media` |

Inside `Media` there is one folder per type: `WhatsApp Images`, `WhatsApp Video`, `WhatsApp Audio`, `WhatsApp Voice Notes`, `WhatsApp Documents`, and a `Sent` subfolder with what you sent. Names can vary with the app language and version.

> [!note]
> On recent Android versions the system file picker may not show `Android/media`. If so, use a file manager to copy it to an ordinary folder such as Downloads and send it from there. We have not tested every manufacturer.

## Step by step with DogNAS

You need a DogNAS server at home. An [old Android works as a file server](/en/blog/turn-old-android-into-file-server/) and, with a hard drive or USB stick, you get more room. On the full phone use DogNAS Client (or the lighter DogNAS Client Lite), which is free.

1. **See what is heavy.** In WhatsApp open Manage storage and note the biggest chats.
2. **Create a folder on the server**, for example `WhatsApp-2026`, and pair the phone with the profile's QR Code and PIN.
3. **Send the media folders** with the upload button, choosing `WhatsApp Images`, `WhatsApp Video` and, if you like, `Documents` and `Voice Notes`. The transfer queue shows progress and resumes if the Wi-Fi drops.
4. **Check on the server.** Open a few photos and videos and compare the file count and size with the phone.
5. **Only then delete from the phone**, either in WhatsApp (Manage storage) or by deleting the folders you copied.

## Things to keep in mind

- **Check before you delete.** This is the step that prevents regret.
- **Deleting media keeps the text**, and the chat shows the file as unavailable. If it is still on the sender's WhatsApp you can sometimes download it again; if not, your copy is the only one.
- **This is not a WhatsApp backup.** The chat history backup is WhatsApp's own (Google Drive). DogNAS stores the media files you copy and does not restore chats.
- **One copy is not safety.** DogNAS stores on the disk you choose. For irreplaceable photos, keep a second copy somewhere else.
- **Your network only.** Sending happens over home Wi-Fi, with the server on and connected.

## Keep it from filling up again

- In WhatsApp, under Storage and data, set automatic download to Wi-Fi only, or turn it off for videos and documents.
- Mute media download in big groups.
- Repeat the copy now and then, for example monthly. Sending is manual today; an automatic copy is not part of DogNAS yet.

## Frequently asked questions

?? Can I delete the media without losing my chats?
Yes. The text stays; deleted files show as unavailable. That is why you copy and check first.

?? Does DogNAS back up WhatsApp?
No. It stores the media files you copy to the server. The chat history backup remains WhatsApp's own.

?? What if the picker does not show the WhatsApp folder?
On newer Android, copy the folder to Downloads with a file manager and send it from there.

## Summary

See what WhatsApp takes, copy the media folders to a server of your own, check them, and only then delete from the phone. If you have nowhere to store it yet, start with [how to free up space on Android](/en/blog/how-to-free-up-space-on-android/) and [use an old Android as a server](/en/blog/turn-old-android-into-file-server/).

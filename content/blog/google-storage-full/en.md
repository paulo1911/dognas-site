---
slug: google-drive-photos-full-store-files-at-home
title: Google Drive or Google Photos full? How to move everything out and keep it at home
summary: How to export your photos and files from Google, keep them on a server of your own at home, and only then free up space in your account, without paying more every month.
meta_title: Google Photos full: keep your photos at home | DogNAS
meta_description: Google Drive or Photos full? Export with Google Takeout, keep everything on a server of your own at home, and free up space in your account without paying more.
pillar: storage
tags: [google photos full, google drive full, google takeout, cloud storage, home server]
cover: assets/blog/google-storage-full/cover-en.webp
cover_alt: A phone running the DogNAS server, connected by cable, next to a hard drive in a stand, on a desk
social_image: assets/blog/google-storage-full/social-en.jpg
cta: server
related: [android-nas-server, cloud-subscription-savings, free-phone-space, pc-phone-transfer, sftp-clients]
status: review
translation_review: pending
created: 2026-11-26
published: 2026-11-26
updated: 2026-11-26
---
The warning shows up: "your storage is almost full." Gmail can stop receiving mail, and Google Photos stops saving what you shoot. The quickest way out is to pay for a bigger plan. But the bill never ends, and the space in an account always fills up again.

There is another way: take the heavy stuff out, keep it at home, and leave the account clean. It's some work at the start, but you only do it once. Here is an order that makes sense, along with the things people tend to forget.

> [!takeaways]
> - Exporting with **Google Takeout** makes a copy. Nothing leaves your account until you delete it.
> - Keep that copy on a server of your own (an old Android sitting in a drawer will do) and **check it** before deleting anything at Google.
> - A server at home is not a backup. For things you can't replace, keep a second copy somewhere else.

## First: what is actually taking the space

The free space (15 GB today, a number Google can change) is shared between Gmail, Drive and Photos. Open your account's storage page and see which of the three is heaviest. It's usually Photos, and sometimes a forgotten folder in Drive or old attachments in Gmail.

This matters because it changes what you export. If the problem is one 4 GB video in Drive, you don't need Takeout at all: download the file and you're done.

## Step 1: have somewhere to put it

Before you download anything, decide where it's going. It can be a hard drive, but if you already have an Android phone or tablet in a drawer, you can turn it into a file server on your Wi-Fi. We explain that in [how to turn an old Android into a file server](/blog/turn-old-android-into-file-server/) and in the [complete guide to an Android NAS server](/blog/android-nas-server-guide/).

Do a quick size check. The free DogNAS plan manages up to 64 GB. If your Google library is 150 GB, you'll need Pro (one-time purchase, no subscription), which uses the device's whole storage, including an SD card or a USB drive.

## Step 2: export with Google Takeout

Takeout is Google's own tool for downloading your data (takeout.google.com).

1. Sign in with the account that is full and tick only what you want: **Google Photos**, **Drive**, or both. Unticking the rest makes the export much lighter.
2. In Drive and Photos you can pick just some albums or folders. If the library is huge, it's worth doing it in stages.
3. Choose the file format and the size of the parts. Smaller parts (2 GB, for example) are easier to download and to repeat if one fails.
4. Request the export and wait. For big libraries it can take anywhere from hours to a few days. Google emails you when it's ready.
5. Download every part. The link only works for a limited time, so don't put it off.

> [!note]
> Photos usually come with `.json` files holding the original date and location. If you open the folder and wonder what they are, that's it. Don't delete them before you see how your photo app handles dates.

## Step 3: move it to your server

Once downloaded, unzip it and copy it to your server. Two simple ways:

- **From a computer:** connect to the server with a program like FileZilla or WinSCP and drag the folders over. It's all in [how to access DogNAS with FileZilla, WinSCP, Cyberduck and rclone](/blog/access-dognas-with-filezilla-winscp-cyberduck-rclone/). Another route is [PC to phone over Wi-Fi](/blog/transfer-files-between-pc-and-phone-over-wifi/).
- **From your phone:** if you downloaded the Takeout straight to the phone, send the folders with the DogNAS Client.

A big transfer over Wi-Fi really is slow. Leave the computer on and the server plugged in, and don't touch it while it copies.

## Step 4: check before you delete

Nobody wants to do this step and everybody should. Before removing anything from Google:

- Compare counts: how many files Google said you had, and how many arrived.
- Open a few photos and videos from different years, preferably the biggest ones. Do they play?
- Look for a folder you know exists, from a specific event.
- If you can, copy everything to a second place too (an external drive). A server at home stores your files but doesn't back itself up, and disks fail.

## Step 5: free up space in the account

Only now, delete, and a little at a time. In Google Photos, what goes to the trash still counts until you empty it. Drive works the same way. And "free up space" in the phone app usually removes only the local copy, without touching what's in the cloud. Read what the button does before you tap it.

Deleting gradually has one advantage: if you notice something missing, you can still go back.

## What if I keep using Google Photos?

Plenty of people do, and that's fine. Photos is great for looking at pictures from anywhere and sharing an album. A server at home is good for volume and privacy, but you only reach it from inside your home network. A common middle ground: keep the last few months in the cloud and send the rest home every so often.

If the goal is to pay less, also read [how to save money on cloud storage subscriptions](/blog/save-money-on-cloud-storage-subscriptions/) and [how to free up space on Android](/blog/how-to-free-up-space-on-android/).

## Quick questions

?? Does exporting with Takeout delete my files at Google?
No. Takeout only creates a copy for you to download. Your photos and files stay in the account until you delete them.

?? Can I do this from my phone alone?
You can, but the export is big and copying from a phone is slower. For large libraries, a computer makes it easier.

?? Can my server be a phone I no longer use?
Yes. An Android 7.0 or newer, plugged in and on your Wi-Fi, is enough. The [Android NAS server guide](/blog/android-nas-server-guide/) shows what works and where it stops.

?? Is this a backup?
Not by itself. It's a copy at home, which depends on the device and the disk. For anything irreplaceable, keep a second copy somewhere else.

## Where to start

Open your Google account's storage page, see what's heavy, and start with a small export just to see how it works. When the first batch lands safely on the server, the rest is just repeating it.

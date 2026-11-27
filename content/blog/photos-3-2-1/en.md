---
slug: keep-photos-without-relying-only-on-the-cloud
title: "Photos without relying only on the cloud: the 3-2-1 rule at home"
summary: The cloud is one copy, not a safe. See how to keep your family photos in more than one place with the 3-2-1 rule, using a server at home and a drive you already own.
meta_title: Photos beyond the cloud: the 3-2-1 rule at home | DogNAS
meta_description: Photos only in the cloud or only on your phone? The 3-2-1 rule explained simply: three copies, two kinds of media, one outside the house, using a server at home.
pillar: storage
tags: [photo backup, 3-2-1 rule, cloud storage, family photos, home server]
cover: assets/blog/google-storage-full/cover-en.webp
cover_alt: A phone running the DogNAS server, connected by cable, next to a hard drive in a stand, on a desk
social_image: assets/blog/google-storage-full/social-en.jpg
cta: server
related: [google-storage-full, cloud-subscription-savings, android-nas-server, free-phone-space, pc-phone-transfer]
status: published
translation_review: reviewed
reviewed_by: Paulo Leite
created: 2026-11-27
published: 2026-11-27
updated: 2026-11-27
---
Most people's photos live in two places: the phone and an app that syncs to the cloud. It feels safe, but it's less than it looks. If the phone is lost and the account gets locked, or the sync quietly stops, there's nothing left to go back to.

The cloud is great, and nobody needs to quit it. The point is to stop it being the only place. There's an old, simple rule for that, and it fits in an ordinary home.

> [!takeaways]
> - The **3-2-1 rule**: 3 copies of what matters, on 2 different kinds of media, with 1 of them outside the house.
> - The phone, the cloud and a server at home count as copies, but a cloud that mirrors your phone can delete in the cloud whatever you delete on the phone.
> - A server at home is a copy, not a backup on its own. Add a second drive and one copy somewhere else.

## Why "synced" is not "backed up"

Many photo apps *sync*: what you do on one side happens on the other. Delete a photo by mistake on the phone and it can disappear from the cloud too (usually it sits in the trash for a while, then goes). A real second copy is one that a mistake on the first can't touch.

Also remember that the account is a single point: a forgotten password, a blocked account, a plan that expired and a library that no longer fits. That's why the rule asks for copies that don't depend on each other.

## The 3-2-1 rule, translated for a home

- **3 copies.** The original (the one on your phone counts) plus two more.
- **2 kinds of media.** Don't put every copy on the same type of thing. A phone and a cloud account are already two. Add a drive and you have three.
- **1 outside the house.** Fire, flood, theft or a power surge hit everything at home at once. One copy has to live elsewhere: the cloud usually plays that role well.

None of this makes a loss impossible. It just makes losing everything at once much less likely.

## A realistic setup with what you already have

You don't have to buy equipment. One arrangement that uses what's probably in your drawer:

1. **Copy 1: the phone** where you shoot. Fine while it's alive.
2. **Copy 2: a server at home.** An old Android phone or tablet running DogNAS, plugged in and on your Wi-Fi, keeps the photos on your network. See [how to turn an old Android into a file server](/blog/turn-old-android-into-file-server/).
3. **Copy 3: outside the house.** The cloud you already use, even on the free plan, or an external drive that lives at a relative's home.

That makes 3 copies, on 3 kinds of media, with 1 outside the house. If you're already stuck with a full cloud account, the order in [Google Drive or Photos full](/blog/google-drive-photos-full-store-files-at-home/) helps you take the heavy part home without losing anything.

> [!warning]
> A server at home is a copy of your files, not a backup that looks after itself. DogNAS doesn't mirror, repeat or restore anything on its own, it doesn't join disks into one volume, and the device can fail like any other. That's why the rule asks for more than one copy.

## How to get photos onto the server today

There are a few simple ways, and none of them needs an account in the cloud:

- **From the phone:** open the DogNAS Client and send the camera folders to the server, as in a normal upload.
- **From a computer:** connect with FileZilla or WinSCP and drag the folders over. The steps are in [how to access DogNAS with FileZilla, WinSCP, Cyberduck and rclone](/blog/access-dognas-with-filezilla-winscp-cyberduck-rclone/).
- **A one-off cable-free copy:** [PC to phone over Wi-Fi](/blog/transfer-files-between-pc-and-phone-over-wifi/).

Today it's a manual routine: you choose what to send and when. A good habit is to send the month's photos on the first weekend of the next one, and check that they opened before you free anything on the phone.

## Habits that make it work

- **Name by date.** Folders like `2026/11-November` are easy to compare and to find years from now.
- **Check, don't assume.** Once in a while open a few old photos from the copy. A backup you've never opened is a hope.
- **Don't delete from the phone until two copies exist.** See [how to free up space on Android](/blog/how-to-free-up-space-on-android/).
- **Keep the outside-the-house copy up to date**, or at least remember when it was last refreshed.
- **Mind the device.** It needs power, ventilation and a Wi-Fi it can reach. An Android that is too old may stop receiving updates, so be wary of exposing it beyond your home network.

## Does this replace the cloud?

Not necessarily. The cloud is convenient for browsing from anywhere and for sharing, and it plays the "outside the house" role well. What changes is that it stops being the only copy and the only reason you're paying a bigger plan each month. If cost is the concern, see [how to save money on cloud storage subscriptions](/blog/save-money-on-cloud-storage-subscriptions/).

## Quick questions

?? Is a cloud account a backup?
It's a copy, and a useful one, but a sync can spread a mistake or a deletion. Treat it as one copy among several, not the only one.

?? Do I need two servers at home?
No. One server at home plus a copy outside the house already meets the rule. A second drive just adds a layer.

?? Can the server be a phone I no longer use?
Yes, an Android 7.0 or newer, plugged in and on your Wi-Fi. The [Android NAS server guide](/blog/android-nas-server-guide/) shows what works and where it stops.

?? Will DogNAS back up my photos automatically?
Not today. Sending is manual, through the Client or a computer. An automatic option is something we're working on, but we only count it once it's in the store.

## Where to start

Count how many copies of your photos exist right now and where. If the answer is "the phone and the cloud", add one at home this weekend, and write down when you'll next refresh it.

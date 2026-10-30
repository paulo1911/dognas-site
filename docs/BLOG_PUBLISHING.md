# Publishing a blog article

Files: `content/blog/<group>/<lang>.md` (en, pt, es; same `group`), syntax and front matter in `content/blog/_template/README.md`.
Build: `python3 tools/build_blog.py` runs `tools/check_blog.py` first (errors stop the build; warnings are counted).

## Flow
1. Topic and intent, keywords **in each language** (not translated keywords). 2. One page = one question; answer it in the first paragraph.
3. First-hand evidence: our own screenshots, measured numbers, a real test (fill `tested:` only after one). **No article without it.**
4. Draft with `status: draft`/`review`; preview with `python3 tools/build_blog.py --preview` (drafts only in `_preview/`).
5. Review each language (`translation_review: reviewed`, and `reviewed_by: <name>` once a person checked it).
6. Publish: `status: published`, real `published`/`updated` dates; build in the documented order (home, client, privacy, blog, seo, redirects).
7. After the deploy: sitemap/canonical/hreflang, URL inspection, then follow Search Console (`BLOG_KPI.md` in the workspace). IndexNow only when asked.

## Quality rules (checked by `check_blog.py` where marked ✔)
- ✔ No absolute security/backup claims ("100 % safe", "never lose", "risk-free"…). Say what DogNAS does and its limits.
- ✔ Never say several servers/disks form one volume or redundant backup (DogNAS has no RAID/pooling). Negations ("does not join disks…") are fine.
- ✔ No WhatsApp backup/restore promises without proof.
- State dependencies on Android version, maker and hardware (background limits, USB OTG, SD cards).
- ✔ Links to other articles must exist in the same language; ✔ images need alt text; ✔ every published group exists in en, pt and es (hreflang pairs); ✔ H1 only from the title.
- ⚠ Warnings: fewer than 2 internal links in the text, step guides without a `tested` line, no `reviewed_by`, no update for 90 days, intent pieces under 1,200 words (BLOG-15), any article under 400 words is an error.

## Cadence and upkeep
1–2 articles a week with the real date (no batches). Review every article every 90 days; change `updated` only when the content really changed.
A native speaker reviews es/en before the volume grows.

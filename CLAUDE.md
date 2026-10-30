# dognas-site — https://dognas.app

Public static site (GitHub Pages, custom domain `dognas.app` at GoDaddy, HTTPS enforced). Public repo:
never put app code, keys or personal data here. Workspace context: `../CLAUDE.md`.

- Pages are **generated** — edit the generators, not the HTML:
  `python3 tools/build_home.py` (landing: **English is the default language and lives at `/`**; Portuguese at `/pt/`, Spanish at `/es/`) and `python3 tools/build_privacy.py` (`/privacy/`), `python3 tools/build_client.py` (`/client/`, `/pt/client/`, `/es/client/`; store links in `STORE`, empty = "Coming soon").
  Texts live inside the scripts; screenshots in `assets/shots/<lang>/` (WebP, 540 px wide).
- SEO / AI-agent files: `python3 tools/build_seo.py` writes `robots.txt` (AI crawlers named), `sitemap.xml` (hreflang), `llms.txt`, `llms-full.txt`, `agents.txt`, `.well-known/security.txt`, `404.html` and the IndexNow key file; `tools/seo.py` holds the shared canonical/hreflang/OG meta and JSON-LD used by every generator. Keep their facts in sync with the product (no prices, no device list). After a deploy, `python3 tools/indexnow.py --send` pings IndexNow (outward-facing, ask first).
- Blog (publishing rules and checks: `docs/BLOG_PUBLISHING.md`, `tools/check_blog.py` runs on every build): `content/blog/<group>/<lang>.md`, `python3 tools/build_blog.py` (`/blog/`, `/pt/blog/`, `/es/blog/`; drafts only with `--preview`). It also writes an Atom feed per language (`<blog>/feed.xml`, auto-discovery `<link>` on every blog page, RSS link in the footer) and the `Blog`/`BlogPosting` JSON-LD (image array, wordCount, keywords from the tags, articleSection). Moved URLs get stub pages from `python3 tools/build_redirects.py`, which **must run last** (order: home, client, privacy, blog, seo, redirects). After a deploy, `python3 tools/indexnow.py --send` (ask first).
- Performance (PageSpeed/Lighthouse 96–100 on all four categories): CSS is inlined by the generators (`inline_css`, no render-blocking request); images get width variants via `python3 tools/optimize_images.py` (needs Pillow; rerun when adding screenshots/photos/covers; icons are `icon-80/128/240.webp`, favicon `icon-96.png`); `<meta charset>` stays first in `<head>`; buttons use `--btn` (4.5:1 with white text). GitHub Pages sends `max-age=600` and cannot change it: the only remaining PSI hint ("efficient cache lifetimes") would need a CDN in front.
- CTA analytics (events, parameters, GA4 setup, how to rank the CTAs): `docs/analytics.md`. New CTAs need a unique `data-loc` (= `cta_id`).
- Real photos: `tools/build_photos.py` (needs Pillow) crops/grades the originals in `../store-assets/real-images`
  into `assets/photos/`, blurring the framed family photo and dropping EXIF. Never publish people or EXIF.
- `/privacy/` is the URL in both Play listings — change it only together with `../dognas-server/docs/PRIVACY_POLICY.md`.
- The stylesheet URL carries a content hash (`style.css?v=…`) because Pages caches files for 10 min.
- Preview: `python3 -m http.server 8765`. Check mobile at 390 px (headless Chrome has a ~500 px minimum
  window — render inside a 390 px iframe).
- Deploy = merge to `main`; build status: `gh api repos/paulo1911/dognas-site/pages/builds/latest -q .status`.

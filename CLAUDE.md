# dognas-site — https://dognas.app

Public static site (GitHub Pages, custom domain `dognas.app` at GoDaddy, HTTPS enforced). Public repo:
never put app code, keys or personal data here. Workspace context: `../CLAUDE.md`.

- Pages are **generated** — edit the generators, not the HTML:
  `python3 tools/build_home.py` (landing `/`, `/en/`, `/es/`) and `python3 tools/build_privacy.py` (`/privacy/`), `python3 tools/build_client.py` (`/client/`, `/en/client/`, `/es/client/`; store links in `STORE`, empty = "Coming soon").
  Texts live inside the scripts; screenshots in `assets/shots/<lang>/` (WebP, 540 px wide).
- Real photos: `tools/build_photos.py` (needs Pillow) crops/grades the originals in `../store-assets/real-images`
  into `assets/photos/`, blurring the framed family photo and dropping EXIF. Never publish people or EXIF.
- `/privacy/` is the URL in both Play listings — change it only together with `../dognas-server/docs/PRIVACY_POLICY.md`.
- The stylesheet URL carries a content hash (`style.css?v=…`) because Pages caches files for 10 min.
- Preview: `python3 -m http.server 8765`. Check mobile at 390 px (headless Chrome has a ~500 px minimum
  window — render inside a 390 px iframe).
- Deploy = merge to `main`; build status: `gh api repos/paulo1911/dognas-site/pages/builds/latest -q .status`.

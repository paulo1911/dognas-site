# Site analytics — comparing the calls to action

GA4 (`G-HJDFSS9D15`) loads only after the visitor accepts the cookie notice. The apps collect nothing. No file names,
PINs, credentials or personal data are ever sent.

## Total pageviews: GoatCounter (cookieless)
GA4 only sees visitors who accept the cookie notice, so its numbers are a floor. `GC` in `GA_TAG` (`tools/build_home.py`) holds the GoatCounter site code; the script
loads on every page, sets no cookie and stores no personal data, so it counts every visit, including decliners and Instagram's in-app browser. Use it as the
source of truth for traffic; use GA4 for the CTA funnel. Accept rate ≈ GA4 visitors ÷ GoatCounter visitors. Tag links from Instagram with
`?utm_source=instagram&utm_medium=social&utm_campaign=<post>` (in-app browsers often drop the referrer).

### GoatCounter events (store clicks only)
Clicks on elements whose `data-ev` is `server|lite|client_store_click` or `blog_server|client_download_click` also send a GoatCounter **event**
(`event: true`, delivered with `sendBeacon`, so it survives the navigation to Google Play): path `store/<app>/<cta_id>/<lang>`, e.g.
`store/server/hero_primary/pt`, `store/server/blog_reuse-old-android_end/en`; title = `Store click: <app> · <cta_id> · <lang>` (English, independent of the page language or button text). Views (`cta_view`), FAQ and navigation clicks are
GA4-only on purpose (events share the pageview quota). GoatCounter has no funnel: click-through of a page = event visits ÷ page visits (`/pt/`). Real installs: Play Console
(the Play links carry `utm_campaign=<cta_id>`).

### Cookie banner (variant C won the A/B/C test, 2026-11; now 100 %)
One short notice, in the style of large Brazilian shops: "Cookies: a gente guarda estatísticas de visitas para melhorar sua experiência de navegação. Ao continuar, você concorda com nossa política de privacidade." + a single button *Concordar e Fechar* (en: *Agree and Close*, es: *Aceptar y cerrar*; the privacy-policy words are the link).
Test result (GoatCounter, accept ÷ shown): first read 04–09/11 had c at ~33 % of only 12 views (partly the owner's own tests); **the 07–09/11 read corrects it: c ≈ 16 % (4 of 25; pt only 1 of 19 ≈ 5 %), a ≈ 14 % (3 of 21), b 0 % (0 accepts, 2 declines)**. So c is **not proven better than a**; it was kept because it is shorter, has one button and the store-click event does not depend on consent (GoatCounter is cookieless). a/b also overlapped with the Instagram traffic that produced no store click (confounded with audience). Re-read with a few hundred views per variant before drawing conclusions.
**Re-ask (one time):** a visitor whose browser has `dognas_banner_v` = a or b **and** `dognas_consent` = denied has the choice cleared once and sees the current notice again; accepted choices are kept. The migration marks `dognas_consent_v2` so it runs once per browser and then drops `dognas_banner_v`.
**It still needs the click:** GA4 and AdSense load only after *Concordar e Fechar*; "continuing" to browse is not consent (the privacy policy promises "only if you accept"). There is no decline button, so a visitor who ignores it stays without cookies; the footer's "Cookie preferences" link opens the two-button text (*Aceitar / Não, obrigado*), so anyone can decline or withdraw consent.
GoatCounter events (anonymous, no cookie): `consent/shown/c/<lang>` (once per browser session) and `consent/accept/c/<lang>`; the constant `c` keeps the series of the experiment. Choices made from the footer link are not counted.

### Experiment SITE-PLAY: red button (A) × official Google Play badge (B)
The three server CTAs of the home pages (`hero_primary`, `final`, `float`) render both variants; `html[data-pv]` (set before paint from `localStorage.dognas_play_v`, 50/50, no cookie; no storage = A) shows one. B links use `cta_id` `<id>_b` (e.g. `hero_primary_b`) and the same suffix in the Play `utm_campaign`, so GoatCounter (`store/server/hero_primary_b/pt`), GA4 and Play Console separate the variants without extra code. Every GA4 event also carries `variant` (`a`/`b`, from `html[data-pv]`; register it as an event-scoped custom dimension to use it in reports — `cta_id` already tells them apart), and `cta_text` falls back to the badge's `alt` text. Click rate = store events ÷ visits of `/`, `/pt/`, `/es/` per variant (`<id>` = A, `<id>_b` = B); read it only with ≥ 300 visits (or ≥ 30 clicks) per variant and ≥ 2 weeks. Badges: official files in `assets/badges/` (unmodified, from the Google Play brand kit), trademark note in the footer. To end the test, keep the winner and delete the other markup, the `PV_SCRIPT` and the `.pv-*` CSS.

## Events (all send the same parameters)
| Event | When |
|---|---|
| `cta_view` | a CTA was on screen (≥ 60 %) — once per `cta_id` per page view (the floating button counts when it first appears) |
| `server_store_click` | click on a link to the server app on Google Play |
| `lite_store_click` | click on a link to the DogNAS Client Lite on Google Play |
| `client_store_click` / `client_page_click` | DogNAS Client (Play when published / the `/client/` page) |
| `support_click` | contact / privacy buttons in the support block |
| `requirements_click`, `faq_open`, `pro_view`, `lang_switch` | engagement signals |
| `blog_read_50` | the reader scrolled past half of the article text (once per page view; params `article`, `category` = pillar id, `lang`); consent-gated like the rest |
| `blog_article_view` | an article page was opened (params: `article` = group id, `category` = pillar id (`reuse`/`storage`/`sftp`/`compare`, language-neutral), `cta`, `lang`); sent only when consent was already granted at load |
| `blog_server_download_click` / `blog_client_download_click` | the article's Play CTA (`cta: server` → server app, `cta: client` → Client Lite); `cta_id` = `blog_<group>_<cta>`, Play `utm_campaign` = `blog_<group>` |
| CTA positions in an article | Three placements per article, same events (`blog_server_download_click` / `blog_client_download_click`), told apart by `cta_id` (and by the Play `utm_campaign`, which equals it): **end** = `blog_<group>_<server\|client>` (no suffix, unchanged), **mid** = `blog_<group>_mid` (band before the middle section, articles with ≥4 sections), **sticky** = `blog_<group>_sticky` (floating button after ~40 % of the scroll; hidden while the cookie banner or another in-page CTA is on screen). Impressions of each come from the generic `cta_view` with the same `cta_id`. The article's `cta` front matter is `server`, `client` or `both` (end box with both buttons; the Client link replaces the Lite as soon as `CLIENT_PLAY` is set) |
| `blog_product_cta_click` | "About DogNAS" link in the article CTA box (to the home page); `cta_id` = `blog_<group>_product` |
| `blog_related_article_click` | link in the article's "Keep reading" list; `cta_id` = `blog_<group>_related_<other group>` |
| `blog_list_article_click` | article card on the blog list (`cta_id` = `blog_list_<group>`; the featured card `blog_list_featured_<group>`, the "Start here" strip `blog_list_start_<group>`) or on a pillar hub (`blog_hub_<pillar>_<group>`) |
| `blog_pillar_click` | pillar chip on the list/hub (`cta_id` = `blog_chip_<pillar|all>`) or the pillar label in an article (`blog_article_<group>_pillar`) |
| `blog_nav_click` | "Blog" link in the header of the home, client and privacy pages; `cta_id` = `nav_blog_<page>` |
| `blog_home_teaser_click` / `blog_home_all_click` | the three "From the blog" cards on the home / its "All guides" link; `cta_id` = `home_blog_<group>` / `home_blog_all` |
| `blog_home_context_click` | "Read the guide" link under a FAQ answer on the home; `cta_id` = `home_faq_<group>` |
| `blog_next_step_click` | the "Next step" card at the end of an article (funnel order in `NEXT`, `build_blog.py`); `cta_id` = `blog_<group>_next_<next group>` |
| `blog_*_download_click` (side) | the desktop side card; `cta_id` = `blog_<group>_side` (Play campaign the same); the floating bar is hidden on desktop |
| `blog_server_download_click` (`blog_list`) | the CTA band under the blog list; `cta_id` = `blog_list_server` |
| `blog_server_download_click` (`blog_header`) | the "Get DogNAS" button in the blog header; `cta_id` = `blog_header` |

Blog funnel: article → download click is measured here; `server_started`, `client_paired`, `first_transfer_success` happen inside the apps (no telemetry by design) — read them from Play Console acquisition and from tester reports. Mark `blog_server_download_click` / `blog_client_download_click` as key events once the first article is live.

Parameters: `cta_id`, `cta_text` (≤ 60 chars), `cta_target` (server / lite / client / client_page / support), `lang`, `page_depth` (% of the page scrolled at the time).

`cta_id` values: `hero_primary`, `hero_secondary` (Lite) / `hero_client` + `hero_lite` (when `CLIENT_PLAY` is set), `mid_how`, `mid_plans`, `mid_faq`, `final`, `float`, `apps_server`, `apps_lite`, `apps_client`, `support_0`, `support_1`.
The Play links also carry `referrer=utm_source=dognas.app&utm_medium=website&utm_campaign=<cta_id>` so Play Console's acquisition report can attribute store visits per CTA.

## One-time GA4 setup (Admin → Data display)
1. **Custom definitions → Create custom dimension** (scope *Event*): `cta_id`, `cta_text`, `cta_target`, `lang`; a custom metric (*Event*, standard) for `page_depth` is optional.
2. **Events → Mark as key event**: `server_store_click` (the install intent), optionally `lite_store_click`.
3. Parameters only appear in reports after the dimension exists and new events arrive (up to 24 h).

## Ranking the CTAs (Explore → Free form)
- Rows: `cta_id`; Columns/values: **Event count** filtered by `cta_view` and by `server_store_click` (two tabs or a segment per event).
- Click rate per CTA = `server_store_click` ÷ `cta_view` for the same `cta_id`. Compare by `lang` and by first-touch channel.
- A CTA with many views and a low rate needs a new text or position; one with a high rate but few views needs more visibility. Low traffic: do not read small differences as proof — keep dates and traffic sources noted (see the strategy doc, §11).

# Site analytics — comparing the calls to action

GA4 (`G-HJDFSS9D15`) loads only after the visitor accepts the cookie notice. The apps collect nothing. No file names,
PINs, credentials or personal data are ever sent.

## Events (all send the same parameters)
| Event | When |
|---|---|
| `cta_view` | a CTA was on screen (≥ 60 %) — once per `cta_id` per page view (the floating button counts when it first appears) |
| `server_store_click` | click on a link to the server app on Google Play |
| `lite_store_click` | click on a link to the DogNAS Client Lite on Google Play |
| `client_store_click` / `client_page_click` | DogNAS Client (Play when published / the `/client/` page) |
| `support_click` | contact / privacy buttons in the support block |
| `requirements_click`, `faq_open`, `pro_view`, `lang_switch` | engagement signals |
| `blog_article_view` | an article page was opened (params: `article` = group id, `category`, `cta`, `lang`); sent only when consent was already granted at load |
| `blog_server_download_click` / `blog_client_download_click` | the article's Play CTA (`cta: server` → server app, `cta: client` → Client Lite); `cta_id` = `blog_<group>_<cta>`, Play `utm_campaign` = `blog_<group>` |
| CTA positions in an article | Three placements per article, same events (`blog_server_download_click` / `blog_client_download_click`), told apart by `cta_id` (and by the Play `utm_campaign`, which equals it): **end** = `blog_<group>_<server\|client>` (no suffix, unchanged), **mid** = `blog_<group>_mid` (band before the middle section, articles with ≥4 sections), **sticky** = `blog_<group>_sticky` (floating button after ~40 % of the scroll; hidden while the cookie banner or another in-page CTA is on screen). Impressions of each come from the generic `cta_view` with the same `cta_id`. The article's `cta` front matter is `server`, `client` or `both` (end box with both buttons; the Client link replaces the Lite as soon as `CLIENT_PLAY` is set) |
| `blog_product_cta_click` | "About DogNAS" link in the article CTA box (to the home page); `cta_id` = `blog_<group>_product` |
| `blog_related_article_click` | link in the article's "Keep reading" list; `cta_id` = `blog_<group>_related_<other group>` |
| `blog_list_article_click` | article card on the blog list |

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

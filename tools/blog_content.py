"""Blog content model: loads and validates content/blog/<group>/<lang>.md (front matter + Markdown subset).
No dependency on the page generators, so build_home/build_client/build_privacy can ask `has_blog(lang)` for the
nav/footer link without a circular import. Only `published` articles are ever emitted."""
import os, re, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, 'content', 'blog')
LANG_PREFIX = {'en': '', 'pt': 'pt/', 'es': 'es/'}  # English is the default language
STATUSES = ('draft', 'review', 'published', 'archived')
CTAS = ('server', 'client')
REVIEWS = ('pending', 'reviewed')
REQUIRED = ('slug', 'title', 'summary', 'meta_title', 'meta_description', 'category', 'cta', 'status', 'translation_review', 'created')
PER_PAGE = 12


def blog_dir(lang): return LANG_PREFIX[lang] + 'blog/'
def article_path(a): return blog_dir(a['lang']) + a['slug'] + '/'
def list_path(lang, page=1): return blog_dir(lang) + ('' if page == 1 else f'page/{page}/')


def _value(v):
    v = v.strip()
    if v.startswith('[') and v.endswith(']'):
        return [x.strip().strip('"\'') for x in v[1:-1].split(',') if x.strip()]
    return v.strip('"\'')


def parse(text):
    m = re.match(r'---\n(.*?)\n---\n(.*)\Z', text, re.S)
    if not m: raise ValueError('missing front matter')
    meta = {}
    for line in m.group(1).splitlines():
        if line.strip() and not line.lstrip().startswith('#'):
            k, _, v = line.partition(':')
            meta[k.strip()] = _value(v)
    return meta, m.group(2).strip()


def load(include_drafts=False):
    """Returns (articles, errors). Errors block the build; drafts/review/archived are skipped unless `include_drafts`."""
    arts, errors = [], []
    if not os.path.isdir(CONTENT): return arts, errors
    for group in sorted(os.listdir(CONTENT)):
        gdir = os.path.join(CONTENT, group)
        if not os.path.isdir(gdir) or group.startswith('_'): continue
        for fn in sorted(os.listdir(gdir)):
            if not fn.endswith('.md'): continue
            lang, where = fn[:-3], f'{group}/{fn}'
            try: meta, body = parse(open(os.path.join(gdir, fn)).read())
            except ValueError as e: errors.append(f'{where}: {e}'); continue
            if lang not in LANG_PREFIX: errors.append(f'{where}: unknown language'); continue
            a = dict(meta, group=group, lang=lang, body=body, where=where)
            errors += [f'{where}: {e}' for e in validate(a)]
            if a.get('status') == 'published' or include_drafts: arts.append(a)
    seen = {}
    for a in arts:
        k = (a['lang'], a.get('slug'))
        if k in seen: errors.append(f'{a["where"]}: slug "{a.get("slug")}" already used by {seen[k]}')
        seen[k] = a['where']
    groups = {g for g in os.listdir(CONTENT) if os.path.isdir(os.path.join(CONTENT, g)) and not g.startswith('_')}  # a related article may still be a draft: it is just not linked until published
    for a in arts:
        for r in a.get('related', []) if isinstance(a.get('related'), list) else []:
            if r not in groups: errors.append(f'{a["where"]}: related "{r}" is not a known article group')
    return arts, errors


def validate(a):
    e = [f'missing "{k}"' for k in REQUIRED if not a.get(k)]
    if a.get('status') not in STATUSES: e.append(f'status must be one of {STATUSES}')
    if a.get('cta') not in CTAS: e.append(f'cta must be one of {CTAS}')
    if a.get('translation_review') not in REVIEWS: e.append(f'translation_review must be one of {REVIEWS}')
    if a.get('slug') and not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', a['slug']): e.append('slug must be lowercase ascii with hyphens')
    if a.get('status') == 'published':
        for k in ('published', 'updated', 'cover', 'cover_alt'):
            if not a.get(k): e.append(f'published article needs "{k}"')
        if a.get('translation_review') != 'reviewed' and a['lang'] != 'pt': e.append('published translation must have translation_review: reviewed')
        if len(a.get('meta_description', '')) > 170: e.append('meta_description over 170 characters')
        if len(re.findall(r'^# ', a['body'], re.M)): e.append('body must not contain an H1 (the title is the H1)')
    for k in ('created', 'published', 'updated'):
        if a.get(k):
            try: datetime.date.fromisoformat(a[k])
            except ValueError: e.append(f'"{k}" must be YYYY-MM-DD')
    return e


def has_blog(lang):
    """True when `lang` has at least one published article (then nav/footer link to its list)."""
    try: return any(a['lang'] == lang for a in load()[0])
    except Exception: return False


def slugify(s):
    s = re.sub(r'[^a-z0-9]+', '-', re.sub(r'[̀-ͯ]', '', __import__('unicodedata').normalize('NFD', s.lower()))).strip('-')
    return s or 'section'


def _url(u, base, lang=None):
    if u.startswith('assets/'): return base + u  # site-relative asset paths work at any depth
    m = re.match(r'/(?:(?:pt|en|es)/)?blog/(.*)', u)
    if m and lang: return '/' + LANG_PREFIX[lang] + 'blog/' + m.group(1)  # article links name the blog, not the language
    return u


PHOTO_DIMS = {'always-on': (900, 1129), 'usb-drive': (900, 1347)}  # assets/photos/<name>.webp
def _srcset(u, base):
    """srcset from the variants made by tools/optimize_images.py (assets/shots: 300/460, assets/photos: 450)."""
    stem = u[:-5]
    if '/shots/' in u: return f' srcset="{base}{stem}-300.webp 300w, {base}{stem}-460.webp 460w, {base}{u} 540w" sizes="190px"'
    if '/photos/' in u:
        w = PHOTO_DIMS.get(os.path.splitext(os.path.basename(u))[0], (900, 1))[0]
        return f' srcset="{base}{stem}-450.webp 450w, {base}{u} {w}w" sizes="300px"'
    return ''


def _dims(u):
    w, h = PHOTO_DIMS.get(os.path.splitext(os.path.basename(u))[0], (540, 1080)) if '/photos/' in u else (540, 1080)
    return f'width="{w}" height="{h}"'


def _inline(s, base='', lang=None):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'!\[([^\]]*)\]\(([^)\s]+)\)', lambda m: f'<img src="{_url(m.group(2), base)}" alt="{m.group(1)}" loading="lazy">', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lambda m: f'<a href="{_url(m.group(2), base, lang)}"' + (' rel="noopener"' if m.group(2).startswith('http') else '') + f'>{m.group(1)}</a>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    return re.sub(r'(?<![*\w])\*([^*]+)\*(?!\w)', r'<em>\1</em>', s)


def render(body, base='', lang=None):
    """Markdown subset: ## / ### headings, paragraphs, - / 1. lists, > quotes, images, links, bold, italic, code. Returns (html, toc)."""
    out, toc, used = [], [], set()
    for block in re.split(r'\n\s*\n', body):
        lines = block.strip().splitlines()
        if not lines: continue
        h = re.match(r'(#{2,3}) (.+)', lines[0])
        if h and len(lines) == 1:
            n, text = len(h.group(1)), h.group(2).strip()
            sid, i = slugify(text), 2
            while sid in used: sid, i = f'{slugify(text)}-{i}', i + 1
            used.add(sid); toc.append((n, sid, text))
            out.append(f'<h{n} id="{sid}">{_inline(text, base, lang)}</h{n}>')
        elif all(re.match(r'[-*] ', l) for l in lines):
            out.append('<ul>' + ''.join(f'<li>{_inline(l[2:], base, lang)}</li>' for l in lines) + '</ul>')
        elif all(re.match(r'\d+\. ', l) for l in lines):
            out.append('<ol>' + ''.join(f'<li>{_inline(re.sub(r"^\d+\. ", "", l), base, lang)}</li>' for l in lines) + '</ol>')
        elif all(l.startswith('>') for l in lines):
            out.append('<blockquote><p>' + _inline(' '.join(l.lstrip('> ') for l in lines), base, lang) + '</p></blockquote>')
        elif all(re.fullmatch(r'!\[[^\]]*\]\([^)\s]+\)', l) for l in lines):
            figs = ''.join(f'<figure><a href="{_url(m.group(2), base)}" target="_blank" rel="noopener"><img src="{_url(m.group(2), base)}"{_srcset(m.group(2), base)} alt="{html.escape(m.group(1))}" {_dims(m.group(2))} loading="lazy"></a><figcaption>{html.escape(m.group(1))}</figcaption></figure>'
                           for m in (re.match(r'!\[([^\]]*)\]\(([^)\s]+)\)', l) for l in lines))
            out.append(f'<div class="carousel"><div class="track">{figs}</div></div>')
        else:
            out.append('<p>' + _inline(' '.join(lines), base, lang) + '</p>')
    return '\n'.join(out), toc

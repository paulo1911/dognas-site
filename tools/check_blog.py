"""Pre-publish checks for blog articles (BLOG-21); build_blog.py runs them on every build. Errors stop the build, warnings are printed.
Rules come from the blog spec (quality section): no absolute security/backup claims, no pooled disks / redundant volume across servers,
no WhatsApp backup promises, links that resolve, alt text, hreflang pairs, internal links, first-hand evidence ("Tested on" for step guides).
Run alone: python3 tools/check_blog.py"""
import re, sys, datetime
import blog_content as bc

LANGS = ('en', 'pt', 'es')
INTENT = ('old-android-server', 'home-nas', 'free-phone-space', 'pc-phone-transfer', 'cloud-subscription-savings')  # BLOG-15: 1,200+ words expected
WORD_FLOOR, INTENT_FLOOR, REFRESH_DAYS = 400, 1200, 90
ABSOLUTE = [r'100\s?%\s?(seguro|safe|seguro)', r'(totally|completely|absolutely|totalmente|completamente|absolutamente)\s+(safe|secure|seguro|seguros)', r'\b(unhackable|inviolable|inviolável|à prova de (hackers?|falhas))\b',
            r'\b(never|nunca|jamás)\s+(lose|loses|perde|perdem|pierdes|pierde)\b', r'\b(risk[- ]free|sem (nenhum )?risco|sin riesgo)\b', r'\b(guaranteed|garantido|garantizado)\s+(backup|copia|safety|segurança)']
POOLING = [r'(combin\w+|join\w*|pool\w*|jun(ta|tar|te)\w*|une?\w*|unir\w*)\s+(several |multiple |vários |varios |todos os |all )?(disks|drives|discos|hds)\s+(in|into|em|como|en)\s+(a |one |um |uma |un )?(single|only|único|unico|volume)',
           r'redundan\w+\s+(across|between|entre)\s+(servers|servidores)']
WHATSAPP = [r'(whatsapp)[^.\n]{0,40}(back ?up|restor|restaur|copia de seguridad)', r'(back ?up|restor|restaur|copia de seguridad)[^.\n]{0,40}whatsapp']
NEGATORS = r'(\bnot\b|n[’\']t\b|\bno\b|\bnão\b|\bnunca\b|\bnunca\b|\bsin\b|\bni\b|\bnem\b|\bnenhum|\bsem\b|n[ãa]o precisa|without|cannot|can not|does not|doesn’t)'


def _negated(text, pos):
    return bool(re.search(NEGATORS, text[max(0, pos - 45):pos], re.I))


def check(arts):
    errors, warns = [], []
    slugs = {(a['lang'], a['slug']) for a in arts}
    by_group = {}
    for a in arts: by_group.setdefault(a['group'], {})[a['lang']] = a
    today = datetime.date.today()
    for a in arts:
        w, body, words = a['where'], a['body'], len(a['body'].split())
        flat = ' '.join(body.split())
        for kind, pats, neg in (('absolute claim', ABSOLUTE, True), ('disk-pooling / redundancy claim', POOLING, True), ('WhatsApp backup claim', WHATSAPP, True)):
            for p in pats:
                for m in re.finditer(p, flat, re.I):
                    if not (neg and _negated(flat, m.start())): errors.append(f'{w}: {kind}: "{flat[max(0, m.start() - 20):m.end() + 20]}"')
        for m in re.finditer(r'!\[\]\(', body): errors.append(f'{w}: image without alt text')
        if len(a.get('cover_alt', '')) < 8: errors.append(f'{w}: cover_alt too short')
        internal = re.findall(r'\]\((/[^)\s]*)\)', body)
        for u in internal:
            m = re.match(r'/(?:(?:pt|en|es)/)?blog/([^/]+)/?$', u)
            if m and (a['lang'], m.group(1)) not in slugs: errors.append(f'{w}: link to unknown article {u}')
        if len(internal) < 2: warns.append(f'{w}: only {len(internal)} internal link(s) in the text (aim for 3+; related links come on top)')
        floor = INTENT_FLOOR if a['group'] in INTENT else WORD_FLOOR
        (warns if a['group'] in INTENT else errors).append(f'{w}: {words} words, below {floor}') if words < floor else None
        if re.search(r'^\d+\. ', body, re.M) and not a.get('tested'): warns.append(f'{w}: has steps but no "tested" line (add one only after a real test)')
        if not a.get('reviewed_by'): warns.append(f'{w}: no reviewed_by')
        try:
            if (today - datetime.date.fromisoformat(a.get('updated') or a['created'])).days > REFRESH_DAYS: warns.append(f'{w}: not updated for {REFRESH_DAYS}+ days (review it)')
        except ValueError: pass
    for g, langs in by_group.items():
        miss = [l for l in LANGS if l not in langs]
        if miss: errors.append(f'{g}: published without {", ".join(miss)} (hreflang pair incomplete)')
    return errors, warns


if __name__ == '__main__':
    arts, errs = bc.load()
    e, w = check(arts)
    print('\n'.join('WARN  ' + x for x in w)); print('\n'.join('ERROR ' + x for x in errs + e))
    print(f'{len(errs) + len(e)} error(s), {len(w)} warning(s)'); sys.exit(1 if errs or e else 0)

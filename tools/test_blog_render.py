"""Checks of the blog Markdown components (tables, callouts, FAQ, video). Run: python3 tools/test_blog_render.py"""
import blog_content as bc

def r(md, lang='en'): return bc.render(md, '../../', lang)[0]

h = r('> [!takeaways]\n> - one **a**\n> - two')
assert '<aside class="callout callout-takeaways"><strong class="callout-title">In short</strong><ul><li>one <strong>a</strong></li><li>two</li></ul></aside>' == h, h
assert 'Em resumo' in r('> [!takeaways]\n> - a', 'pt') and 'En resumen' in r('> [!takeaways]\n> - a', 'es')
assert 'callout-warning' in r('> [!warning]\n> careful') and 'Atenção' in r('> [!warning]\n> x', 'pt')
p = r('> [!tip]\n> first\n>\n> second'); assert p.count('<p>') == 2, p

t = r('| | A | B |\n|---|---|---|\n| row | x | [l](/blog/z/) |')
assert '>A</th>' in t and 'scope="row" role="rowheader">row</th>' in t and 'class="table-wrap"' in t, t
assert '<span class="sr">Aspect</span>' in t and 'data-label="A">x</td>' in t, 'empty corner cell is labelled; cells carry their column name'
assert '<th scope="col" role="columnheader"></th>' not in t
assert 'href="/pt/blog/z/"' in r('| | A |\n|---|---|\n| r | [l](/blog/z/) |', 'pt')
assert '<table' not in r('| not | a table |\n| just | lines |'), 'a pipe line without a separator row is text'

f = r('?? Why?\nBecause.\n\n?? And?\nYes.\n\nAfter.')
assert f.count('<details>') == 2 and f.count('<div class="faq">') == 1 and f.endswith('<p>After.</p>'), f
assert r('?? Only?\nOne.').endswith('</div>'), 'a FAQ at the end of the article is closed'

v = r('@video(assets/v.mp4, assets/p.webp, A demo)')
assert 'poster="../../assets/p.webp"' in v and 'preload="none"' in v and '<figcaption>A demo</figcaption>' in v, v

h2, toc = bc.render('## One\n\ntext\n\n> [!tip]\n> note\n\n### Two')
assert [x[2] for x in toc] == ['One', 'Two'], toc
print('ok')

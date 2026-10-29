# Template de artigo

Copie para `content/blog/<grupo-de-traducao>/<pt|en|es>.md`. Pastas que começam com `_` são ignoradas pelo build.
Só `status: published` é gerado. Regras completas: `docs/BLOG_PUBLISHING.md` (BLOG-4).

```
---
slug: slug-do-artigo
title: Título (H1)
summary: Uma frase para a lista.
meta_title: Título para o Google (até ~60 caracteres)
meta_description: Descrição para o Google (até 170 caracteres)
category: Guias
tags: [android, nas]
cover: assets/blog/<grupo>/cover.webp
cover_alt: Descrição da imagem
social_image: assets/blog/<grupo>/social.jpg
cta: server            # server | client
related: [outro-grupo]
status: draft          # draft | review | published | archived
translation_review: pending   # pending | reviewed (traduções publicadas exigem reviewed)
created: 2026-10-28
published: 2026-10-28
updated: 2026-10-28
---
Corpo em Markdown (## e ### para seções; sem H1).
```

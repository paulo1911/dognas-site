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
pillar: reuse   # reuse | storage | sftp | compare (names and hub pages: tools/blog_pillars.py)
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

## Componentes (BLOG-12) — tudo vira HTML estático, sem JS

Linhas em branco separam os blocos; cada componente é um bloco.

**Resumo no topo** ("Em resumo"; coloque logo depois da introdução — também serve a snippets e respostas de IA):
```
> [!takeaways]
> - Primeiro ponto.
> - Segundo ponto.
```
**Destaques** (`tip` = dica, `warning` = limites/atenção, `note` = nota; o título é traduzido pelo build):
```
> [!warning]
> Texto do destaque (pode ter vários parágrafos separados por uma linha `>` vazia).
```
**Tabela** (a primeira coluna vira o título de cada linha para leitores de tela; role na horizontal no celular):
```
| | Opção A | Opção B |
|---|---|---|
| Custo | ... | ... |
```
**FAQ** (cada pergunta é um bloco; blocos seguidos viram uma lista; a resposta é o resto do bloco):
```
?? A pergunta?
A resposta em uma ou duas frases.
```
**Vídeo** (arquivo mp4 no site + imagem de capa; só carrega ao tocar):
```
@video(assets/blog/<grupo>/demo.mp4, assets/blog/<grupo>/demo-poster.webp, Legenda)
```
Listas numeradas (`1.`) viram passos em cartões numerados. Teste do renderizador: `python3 tools/test_blog_render.py`.

## Optional: `tested`
`tested: Moto G100 · Android 12 · 2026-10-20` shows a "Tested on" line under the title. Fill it only with a real test (device, Android version, date);
leave it out otherwise. Devices and the "How we test" page: `tools/blog_about.py`.

## Optional: `reviewed_by`
`reviewed_by: <name>` records who checked the language version (`check_blog.py` warns when it is missing).

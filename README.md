# dognas-site

Site público do DogNAS (página inicial e política de privacidade), servido pelo GitHub Pages.
O código dos apps fica em repositórios privados; este repositório só tem o site estático.

- `/` (pt-BR), `/en/`, `/es/` — página inicial
- `/privacy/` — política de privacidade (PT, EN, ES), usada nas fichas da Google Play

## Regenerar as páginas

    python3 tools/build_home.py      # páginas iniciais (pt, en, es)
    python3 tools/build_privacy.py   # política de privacidade

Os textos ficam nos próprios scripts; as capturas em `assets/shots/<idioma>/` (WebP, 540 px).

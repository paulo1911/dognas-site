# Fotos reais para o blog — para validar (branch `exp/blog-real-photos`)

Abra `preview.html` (`python3 -m http.server 8765` e `/assets/photos/blog/preview.html`) e aprove ou reprove cada foto.
Nada disso está ligado a nenhum artigo ainda. Todas saem sem EXIF, em 900 px e 450 px (WebP).

| Arquivo | O que mostra | Observação |
|---|---|---|
| `s20fe-dark` | Galaxy S20 FE com o DogNAS, luz azul | tela em português; sem pessoas |
| `s20fe-closeup` | mesmo, de perto (Wi-Fi, disco, CPU, memória) | a barra de status mostra a hora |
| `s20fe-side` | mesmo, ângulo mais baixo | quase igual à primeira: escolha uma |
| `tv-box-g100` | TV box + Moto G100 com o Client Lite | o app mostra "Home · STV-3000 Plus" |
| `tv-launcher` | tela da TV (Aquário) com o DogNAS nos favoritos | sem pessoas |
| `old-tablet` | tablet de 7" como servidor, ao lado de um roteador | sem pessoas |

## Ficaram de fora de propósito
- **3 fotos de catálogo de terceiros** (Vivensis, Trendoca/Aquário, XSmart): imagens de outras marcas e de loja, com direitos próprios. Se quiser mostrar uma TV box no artigo, use a sua (`tv-box-g100`, `tv-launcher`).
- **4 fotos com a foto de família emoldurada na mesa** (`1FD46A93`, `50A0F0E5`, `6BFBDF00`, `AB2E3A51`): aparecem pessoas. As que o site já usa (`always-on`, `usb-drive`) têm a moldura borrada pelo `build_photos.py`. `50A0F0E5` ainda mostra seu nome ("Paulo") e arquivos de teste no Moto G. Para incluí-las, é preciso definir a área a borrar em cada uma.

## Antes de publicar
1. Textos alternativos acima estão em inglês; falta pt e es.
2. Conferir que nenhuma tela mostra IP, QR ou nome de rede (as seis atuais não mostram).
3. Ligar as fotos aos artigos (BLOG-23 TV box, o do tablet e o do servidor no S20 FE) numa mudança separada.

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
| `usb-dock-s20fe` | S20 FE com um dock com HDD de 500 GB reaproveitado de notebook, alimentação externa de 20 W (confirmado pelo dono do projeto) | 2º lote; moldura de família borrada; combina com o artigo `old-laptop-hdd` |
| `tv-box-client` | Moto G100 com o Client Lite conectado à TV box ("My files") | 2º lote; sem pessoas |
| `tablet-transfers` | tablet servidor + celular recebendo arquivos | 2º lote; moldura borrada; mostra nomes de arquivos de teste |
| `tablet-server-online` | tablet "Server ONLINE" + celular na frente | 2º lote; moldura borrada; mostra o nome "Paulo" na tela do celular (decisão do dono do projeto, 2026-11-01: manter, dá realismo) |
| `old-tablet` | tablet de 7" como servidor, ao lado de um roteador | sem pessoas |

## Segundo lote (10 fotos novas, 2026-11-01)
Usadas 4 das 10. As outras 6 repetem enquadramentos (tablet + celular + moldura de família) ou são muito escuras (`3FD07428`); `62E0FA42`, `17D7EE1A`, `57D97CBB` e `A90B5F73` são variações do mesmo cenário e podem entrar se você quiser mais (a moldura precisa ser borrada em cada uma). `65054EA3` é quase igual a `065464F3`.

## Hardware nas fotos (informado pelo dono do projeto)
- **S20 FE:** dock com HDD de 500 GB reaproveitado de notebook, alimentação externa de 20 W.
- **Tablet de 7" (E13):** usa o mesmo tipo de dock, com um HDD de 320 GB. O dock com o cabo vermelho aparece atrás do tablet nas fotos `62E0FA42` e `57D97CBB` (não usadas ainda); entram no artigo `old-laptop-hdd` se você quiser, com a moldura de família borrada.

## Ficaram de fora de propósito
- **3 fotos de catálogo de terceiros** (Vivensis, Trendoca/Aquário, XSmart): imagens de outras marcas e de loja, com direitos próprios. Se quiser mostrar uma TV box no artigo, use a sua (`tv-box-g100`, `tv-launcher`).
- **4 fotos com a foto de família emoldurada na mesa** (`1FD46A93`, `50A0F0E5`, `6BFBDF00`, `AB2E3A51`): aparecem pessoas. As que o site já usa (`always-on`, `usb-drive`) têm a moldura borrada pelo `build_photos.py`. `50A0F0E5` ainda mostra seu nome ("Paulo") e arquivos de teste no Moto G. Para incluí-las, é preciso definir a área a borrar em cada uma.

## Antes de publicar
1. Textos alternativos acima estão em inglês; falta pt e es.
2. Conferir que nenhuma tela mostra IP, QR ou nome de rede (as seis atuais não mostram).
3. Ligar as fotos aos artigos (BLOG-23 TV box, o do tablet e o do servidor no S20 FE) numa mudança separada.

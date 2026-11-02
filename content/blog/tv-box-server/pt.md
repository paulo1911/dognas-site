---
slug: tv-box-android-como-servidor-de-arquivos
title: TV box Android como servidor de arquivos da casa: o que funciona e o que esperar
summary: Uma TV box Android barata também pode guardar seus arquivos em casa. O que testamos numa box real, o que você precisa, qual a velocidade e onde ela deixa a desejar.
meta_title: TV box Android como servidor de arquivos com o DogNAS | DogNAS
meta_description: Use uma TV box Android como servidor de arquivos particular no Wi-Fi de casa com o DogNAS: testado numa box real, com passo a passo, velocidades medidas, limites e o que conferir antes.
pillar: reuse
tags: [tv box android, servidor de arquivos, nas caseiro, sftp, hd externo]
cover: assets/blog/tv-box-server/cover-pt.webp
cover_alt: A tela inicial de uma TV box Android com o app DogNAS entre os apps favoritos
social_image: assets/blog/tv-box-server/social-pt.jpg
cta: server
related: [old-android-server, home-nas, old-tablet]
tested: Aquário STV-3000 Plus (TV box) · Android 11 · 2026-11-01
status: review
translation_review: pending
created: 2026-11-01
updated: 2026-11-01
---
Uma TV box Android é um pequeno computador sempre ligado que já fica ao lado da TV e do roteador. Tem Wi-Fi (muitas têm também porta de rede), porta USB e nenhuma tela própria para manter acesa. Isso a torna uma candidata natural a servidor de arquivos de casa, e desde o **DogNAS 1.1.6** o app servidor foi preparado para rodar numa delas.

Este guia vem de um teste real, não da ficha técnica: rodamos o DogNAS numa Aquário STV-3000 Plus (Android 11, 2 GB de memória) e a usamos de dois celulares e de um computador. Ele diz o que funcionou, o que não funcionou e o que não conseguimos testar.

> [!takeaways]
> - O DogNAS 1.1.6 ou mais novo roda numa TV box Android: aparece no menu da TV e pode ser usado com o controle remoto.
> - A box precisa de **Android 7.0 ou mais novo**. A nossa tinha Google Play, que também importa para o plano Pro.
> - Os arquivos podem ficar na memória interna da box ou num **HD ou pendrive USB** ligado a ela. Os dois funcionaram igual no nosso teste.
> - A velocidade é limitada pelo Wi-Fi e pelo processador fraco da box, não pelo disco: cerca de 3 MB/s de um computador e de 1 a 1,5 MB/s de um celular, na nossa rede de 5 GHz.
> - Serve bem para backup e para acessar documentos e fotos, não para passar vídeo 4K direto da box.

## O que você precisa

- Uma TV box Android com **Android 7.0 ou mais novo** e algum espaço livre, ou um disco USB (HD ou SSD num dock, ou um pendrive).
- A box ligada à rede de casa. O Wi-Fi funciona; se a sua box tem porta de rede, o cabo é a opção mais estável (não testamos com cabo).
- Um celular para parear, para ler o QR Code mostrado na TV.
- O app DogNAS na box. Ele vem do Google Play, então a box precisa ter a Play Store. Boxes sem ela podem ser um problema: não testamos instalar o app por outros meios.

> [!warning]
> Muitas boxes baratas cortam a rede quando entram em espera, e o Wi-Fi delas pode ser lento. Veja como a sua se comporta antes de contar com ela para backup, e deixe-a ligada na tomada.

## Configure em poucos passos

1. **Instale o DogNAS** pela Play Store na box e abra-o na linha de "Apps" do menu da TV.
2. **Escolha onde guardar os arquivos.** O assistente do primeiro uso pergunta onde a pasta "DogNAS" deve ficar. Muitas TV boxes não têm seletor de pastas do sistema, então o DogNAS mostra uma escolha própria: a memória interna da box ou, se houver um ligado, o disco USB.
3. **Inicie o servidor** e escolha um PIN de 4 dígitos para o perfil Home. O teclado na tela da TV funciona para o PIN.
4. **Pareie um celular.** A TV mostra um QR Code. No celular, abra o DogNAS Client Lite ou o DogNAS Client, toque em "Adicionar DogNAS", aponte a câmera para a TV e digite o mesmo PIN.
5. **Dê um endereço fixo à box** no roteador ou nas configurações de Wi-Fi dela, para o endereço não mudar depois de reiniciar. No nosso teste a box ganhou outro endereço depois de reiniciar: um app a encontrou sozinho, o outro precisou de atualização (corrigido no DogNAS Client Lite 1.0.6). Um endereço fixo evita o problema.

![A tela inicial da TV com o DogNAS entre os apps favoritos.](assets/photos/blog/tv-launcher.webp)
![A TV box sobre a mesa com um Moto G100 na frente, mostrando o DogNAS Client Lite conectado a ela.](assets/photos/blog/tv-box-g100.webp)

## O que medimos

| | Resultado no nosso teste |
|---|---|
| Box | Aquário STV-3000 Plus, Android 11, 2 GB de RAM |
| Rede | Wi-Fi 5 GHz, link de cerca de 200 a 290 Mbps |
| Computador para a box (SFTP, 200 MB) | cerca de 3,3 MB/s para enviar e 3,1 MB/s para baixar |
| Celular para a box (200 MB) | cerca de 1,2 a 1,4 MB/s para enviar |
| Memória interna x disco USB | mesma velocidade (o disco não era o limite) |
| Arquivos depois da cópia | conferidos byte a byte: idênticos |

Para comparar, um celular moderno num bom roteador pode ser várias vezes mais rápido. O processador da box precisa criptografar cada transferência, por isso uma box barata chega a poucos MB/s. Se a ideia é guardar cópias e abrir documentos, tudo bem; copiar um vídeo grande leva minutos, não segundos.

## O que saber antes de depender dela

- **Depois de reiniciar, o servidor não liga sozinho no plano Grátis.** Abra o DogNAS e toque em Iniciar. O plano Pro pode ligar o servidor sozinho quando a box é ligada.
- **O plano Pro é comprado pelo Google Play.** Uma box sem Google Play não consegue comprar e fica no plano Grátis.
- **O controle remoto basta, mas não é rápido.** O app mostra um contorno de foco e se move com as setas; testamos as setas, mas não todos os modelos de controle. Digitar no teclado da tela é mais lento que no celular, e o botão Voltar sai do app, como em qualquer app de TV.
- **Trate-a como um canto quieto da sua rede.** O DogNAS é para o Wi-Fi de casa: nada sai da sua rede e não há nuvem.

?? Funciona em qualquer TV box Android?
Precisa de Android 7.0 ou mais novo e, na prática, de Google Play. Testamos uma box; outros modelos podem ser diferentes, principalmente no comportamento em espera e na velocidade do Wi-Fi.

?? Posso usar um HD USB com ela?
Pode. No nosso teste, um disco USB ligado à box apareceu no assistente do primeiro uso e funcionou na mesma velocidade da memória interna. Um disco que pede mais energia do que a porta USB da box entrega pode não girar, então um dock com fonte própria é mais seguro.

?? É rápida o bastante para ver vídeos a partir dela?
Não de forma confiável. A poucos MB/s um vídeo comum pode tocar, mas arquivos grandes demoram para copiar e um vídeo de alta qualidade pode travar. Use-a para guardar e acessar arquivos, e copie os vídeos para o aparelho em que você os assiste.

?? Preciso pagar?
Não. O plano Grátis guarda até 64 GB de arquivos, com o perfil Home e mais dois perfis. O Pro tira esse limite e acrescenta as opções listadas no app.

## Vale a pena

Se você já tem uma TV box parada numa gaveta, é um jeito sem custo de guardar os arquivos de casa num só lugar, sem nuvem. Se vai comprar um aparelho para isso, um celular ou tablet antigo com processador melhor costuma ser mais rápido. Compare com as outras opções em [reaproveitar um Android antigo](old-android-server) e em [um tablet antigo como armazenamento da casa](old-tablet).

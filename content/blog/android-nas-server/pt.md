---
slug: servidor-nas-android-guia-completo
title: "Servidor NAS no Android: guia completo para ter um NAS em casa com um celular"
summary: O que é um servidor NAS no Android, o que você precisa, como funciona, qual a velocidade real e onde ele para. O mapa de todos os outros guias do site.
meta_title: Servidor NAS no Android: guia completo | DogNAS
meta_description: O que é um servidor NAS no Android, o que você precisa, como os arquivos trafegam, velocidades reais, segurança e limites. Guia completo para um NAS caseiro num celular, tablet ou TV box.
pillar: reuse
tags: [servidor nas, android nas, nas caseiro, servidor de arquivos, sftp, android antigo, tv box]
cta: server
related: [old-android-server, home-nas, nas-vs-android, tv-box-server]
cover: assets/blog/android-nas-server/cover-pt.webp
cover_alt: Um tablet com o servidor DogNAS ao lado de um dock de HD USB, com um celular conectado
social_image: assets/blog/android-nas-server/social-pt.jpg
status: review
translation_review: pending
created: 2026-11-24
published: 2026-11-24
updated: 2026-11-24
---
Um servidor NAS no Android é um celular, tablet ou TV box Android que fica em casa, ligado na tomada, guardando os seus arquivos para que todos os outros aparelhos do Wi-Fi consigam acessá-los. NAS é a sigla de armazenamento conectado à rede: um pequeno servidor na sua rede local que só guarda e entrega arquivos. A diferença é que o equipamento é o que você já tem.

Este guia é o mapa. Ele explica o que é um servidor NAS no Android, o que você precisa, como os arquivos trafegam, qual a velocidade real, o que o protege e onde ele para, e aponta o passo a passo de cada caso. Tudo aqui é sobre o **DogNAS**, o app que transforma o aparelho em servidor.

> [!takeaways]
> - Um servidor NAS no Android guarda os seus arquivos **em casa e no seu Wi-Fi**: sem nuvem e sem mensalidade pelo armazenamento em si.
> - Você precisa de um aparelho com **Android 7.0 ou mais novo**, um carregador, o Wi-Fi de casa e espaço para os arquivos: memória interna, cartão SD ou unidade USB.
> - Os celulares acessam com o app **DogNAS Client**, por QR Code e PIN; os computadores, com qualquer programa de **SFTP**. Não é uma pasta de rede do Windows (SMB).
> - A velocidade depende do Wi-Fi e do aparelho. Numa TV box modesta medimos cerca de **3 MB/s a partir de um computador e de 1 a 1,5 MB/s a partir de um celular**, numa rede de 5 GHz.
> - Ele **não** substitui um NAS completo: não tem RAID, não roda contêineres e um disco pode falhar. Mantenha uma cópia independente do que importa.

## O que é um servidor NAS no Android (e o que não é)

Um NAS faz uma coisa bem: guarda os arquivos num só lugar da casa e os entrega a qualquer aparelho. Um servidor NAS no Android faz esse trabalho com um app, em vez de uma caixa dedicada. Instale o DogNAS no aparelho, escolha onde ficam os arquivos e toque em Iniciar. A partir daí o aparelho responde na sua rede doméstica.

É um **servidor de arquivos**, não um mini data center. Não há contêineres, apps de mídia nem conjuntos de discos. Para fotos, vídeos, documentos, trabalhos da escola e "mandar isso para o meu computador", basta. Para dados insubstituíveis num único lugar, ou muita gente assistindo vídeo ao mesmo tempo, não basta.

| | NAS no Android com DogNAS | NAS comprado pronto |
|---|---|---|
| Equipamento | O Android que você já tem | Uma caixa nova, geralmente com discos |
| Vários discos como um só (RAID) | Não: cada disco é um armazenamento separado | Sim, em muitos modelos |
| Como os aparelhos se conectam | DogNAS Client nos celulares; programas SFTP nos computadores | Em geral uma pasta de rede (SMB) e o app do fabricante |
| Configuração | Instalar o app, escolher uma pasta e tocar em Iniciar | Instalar os discos e configurar o sistema |
| Serviços extras | Só servidor de arquivos | Muitas vezes apps, contêineres e servidores de mídia |
| Energia | Um carregador, como qualquer celular | Uma fonte dedicada |

Se você ainda está decidindo entre os dois, leia [NAS tradicional ou servidor Android](/blog/nas-tradicional-ou-servidor-android/) e [NAS caseiro sem comprar um NAS](/blog/nas-caseiro-sem-comprar-nas/).

## O que você precisa

- **Um aparelho com Android 7.0 ou mais novo** que ficará em casa como servidor: um celular antigo, um tablet ou uma TV box Android.
- **O Wi-Fi de casa.** O servidor e os aparelhos que o usam precisam estar na mesma rede. O servidor não precisa de internet para mover arquivos; você só precisa dela para instalar os apps.
- **Espaço para os arquivos.** A memória interna do aparelho, um cartão SD, ou uma unidade USB ou HD. Unidades USB exigem um aparelho com USB OTG.
- **Um carregador.** O servidor funciona melhor ligado na tomada e longe do sol direto.
- **Um celular para usar.** O DogNAS Client está no Google Play para Android; a versão para iPhone ainda não saiu.

Celular, tablet ou TV box? O celular é a opção mais comum. O tablet dá uma tela que mostra o painel do servidor num relance: veja [tablet antigo como armazenamento da casa](/blog/tablet-antigo-como-armazenamento-da-casa/). A TV box fica ligada o dia todo e tem portas USB: veja [TV box Android como NAS caseiro](/blog/tv-box-android-como-servidor-de-arquivos/), escrito a partir de um teste numa caixa real.

## Como funciona

Três partes conversam entre si:

1. **O app servidor (DogNAS)** roda no Android em casa. Guarda os arquivos no armazenamento que você escolheu e responde pela sua rede.
2. **Os perfis.** Cada pessoa da casa recebe um perfil com PIN e pastas próprios, e ninguém vê os arquivos dos outros.
3. **Os clientes.** No celular, o **DogNAS Client** permite navegar, enviar e baixar. No computador, um programa SFTP comum, como FileZilla, WinSCP ou Cyberduck, faz o mesmo.

Os arquivos trafegam por **SFTP**, que roda dentro de uma conexão SSH criptografada. Por isso o computador precisa de um programa SFTP em vez de "Rede" no explorador de arquivos: o DogNAS não é uma pasta de rede do Windows (SMB). Se o termo é novo, [o que é SFTP](/blog/o-que-e-sftp-como-acessar-servidor-android/) explica em palavras simples, e [como acessar o DogNAS pelo FileZilla, WinSCP e Cyberduck](/blog/acessar-dognas-pelo-filezilla-winscp-cyberduck-rclone/) mostra cada programa.

![Um servidor DogNAS com um HD externo numa base USB, acessado pelo celular.](assets/photos/usb-drive.webp)

## Configure em cinco passos

1. **Instale o DogNAS no aparelho que será o servidor.**
2. **Escolha onde ficam os arquivos** e toque em Iniciar. O servidor já está rodando na sua rede.
3. **Crie um perfil e um PIN de 4 dígitos** para cada pessoa.
4. **Mostre o QR Code do perfil.** O app servidor também tem um botão com um segundo QR Code que leva o outro celular à página do DogNAS Client, e o app fica a um escaneamento de distância.
5. **No celular, abra o DogNAS Client**, aponte a câmera para o QR Code do perfil e digite o PIN.

O passo a passo completo, com telas, está em [como transformar um Android antigo em servidor NAS](/blog/transformar-android-antigo-em-servidor-de-arquivos/).

![Servidor DogNAS online, com uma transferência em andamento](assets/shots/pt/server-status.webp)
![QR Code do perfil para conectar o celular](assets/shots/pt/server-qr.webp)
![Arquivos no DogNAS Client](assets/shots/pt/client-files.webp)

## Qual é a velocidade, de verdade?

Depende de duas coisas que você pode conferir antes de começar: o seu Wi-Fi e o aparelho.

A velocidade é limitada pela **rede Wi-Fi e pelo processador do aparelho**, não pelo disco. Numa TV box com processador fraco, numa rede de 5 GHz, medimos cerca de **3 MB/s a partir de um computador e de 1 a 1,5 MB/s a partir de um celular**. Isso serve para documentos, fotos e backups comuns; é lento se você pretende mover uma biblioteca grande de vídeos todo dia. Um celular mais novo, com processador mais forte e bom sinal de 5 GHz, vai melhor, então confira as especificações do seu aparelho.

Para tirar mais de uma transferência: deixe o servidor perto do roteador, prefira a rede de 5 GHz e mantenha o servidor na tomada. A aba Monitor do servidor mostra a velocidade e os clientes conectados em tempo real.

![Monitor do servidor: clientes e velocidade em tempo real](assets/shots/pt/server-monitor.webp)

## Segurança e privacidade

- **Sem nuvem.** Os arquivos ficam no aparelho, e o DogNAS não os envia a nenhum servidor do DogNAS.
- **Transferência criptografada.** Os arquivos trafegam por SSH/SFTP pela sua rede.
- **Um PIN por perfil.** Depois de vários PINs errados, as tentativas ficam bloqueadas por alguns minutos.
- **O cliente lembra a identidade do servidor.** Se a identidade mudar, o DogNAS Client avisa e pede para parear de novo.

O DogNAS foi pensado para a sua **rede local**. Ele não deve ser aberto para a internet. Mantenha a senha do Wi-Fi em segredo e trate o PIN como qualquer outra senha. Nenhuma ferramenta protege tudo, então mantenha uma cópia independente do que importa.

## O que ele não faz

- **Sem RAID.** Cada disco é um armazenamento separado. O DogNAS não une vários discos num só volume, e um disco pode falhar.
- **Sem backup por conta própria.** Armazenamento não é backup. Para arquivos que você não pode perder, guarde uma cópia em outro lugar.
- **Sem pasta de rede para Windows ou Mac.** Os computadores usam um programa SFTP.
- **Depende do aparelho.** Alguns fabricantes limitam apps em segundo plano para poupar bateria, e unidades USB exigem USB OTG. Se o servidor parar sozinho, confira as configurações de bateria do aparelho.
- **Não é uma central de mídia.** Ele guarda e entrega arquivos; não roda outros apps para você.

## Plano Grátis e Pro

No plano Grátis o DogNAS gerencia até **64 GB**, com o perfil Casa mais dois perfis e até três aparelhos pareados. O **DogNAS Pro** é uma compra única, sem assinatura, e libera todo o armazenamento do aparelho, entre outras coisas. Se você precisar de mais espaço antes disso, ligue um cartão SD ou uma unidade USB.

## Para onde ir agora

- Decidir: [NAS tradicional ou servidor Android](/blog/nas-tradicional-ou-servidor-android/).
- Montar: [Android antigo como servidor NAS](/blog/transformar-android-antigo-em-servidor-de-arquivos/), [tablet antigo](/blog/tablet-antigo-como-armazenamento-da-casa/), [TV box](/blog/tv-box-android-como-servidor-de-arquivos/), [HD de notebook como armazenamento](/blog/reaproveitar-hd-de-notebook-como-armazenamento/).
- Usar: [passar arquivos entre PC e celular pelo Wi-Fi](/blog/transferir-arquivos-entre-pc-e-celular-pelo-wifi/).

?? Preciso de internet para usar um servidor NAS no Android?
Não. O servidor e os seus aparelhos só precisam estar no mesmo Wi-Fi. Você precisa de internet para instalar os apps e, se quiser, para comprar o Pro.

?? Consigo ver como uma unidade de rede no Windows ou no Mac?
Não. O DogNAS é acessado por SFTP, não como pasta de rede (SMB). Use um programa SFTP comum, como FileZilla, WinSCP ou Cyberduck, ou o app DogNAS Client no Android.

?? Quais versões do Android funcionam?
Android 7.0 ou mais novo, num celular, tablet ou TV box. Alguns fabricantes limitam apps em segundo plano, então confira as configurações de bateria do aparelho se o servidor parar.

?? Posso usar um tablet ou uma TV box em vez de um celular?
Sim. Veja os guias do [tablet antigo](/blog/tablet-antigo-como-armazenamento-da-casa/) e da [TV box Android](/blog/tv-box-android-como-servidor-de-arquivos/).

?? Posso guardar os arquivos num cartão SD ou numa unidade USB?
Sim. Você pode escolher a memória interna, um cartão SD ou uma unidade USB ou HD. Unidades USB exigem um aparelho com USB OTG.

?? Um servidor NAS no Android é um backup?
Não. Armazenamento não é backup, e o DogNAS não faz backups por conta própria. Mantenha uma cópia independente do que você não pode perder.

?? É grátis?
O plano Grátis gerencia até 64 GB, com o perfil Casa mais dois e até três aparelhos pareados. O DogNAS Pro é uma compra única, sem assinatura, e remove esses limites.

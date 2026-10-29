---
slug: reaproveitar-hd-de-notebook-como-armazenamento
title: Como reaproveitar o HD de um notebook antigo como armazenamento da casa
summary: Aquele HD ou SSD que sobrou de um notebook pode virar espaço extra para o seu servidor Android. Veja o que você precisa e o que observar.
meta_title: Reaproveitar HD de notebook como armazenamento | DogNAS
meta_description: Como usar o HD ou SSD de um notebook antigo, numa case USB, como armazenamento de um servidor de arquivos Android, com os cuidados de energia e backup.
category: Guias
tags: [hd de notebook, case usb, usb otg, armazenamento]
cover: assets/blog/old-laptop-hdd/cover-pt.webp
cover_alt: Monitor do servidor DogNAS em um Android, ao lado do mascote do DogNAS
social_image: assets/blog/old-laptop-hdd/social-pt.jpg
cta: server
related: [old-android-server, nas-vs-android, home-nas]
status: review
translation_review: reviewed
created: 2026-10-28
---
Quando você troca o HD de um notebook por um SSD, o disco antigo costuma ir para a gaveta. Ele ainda funciona e pode ter centenas de gigabytes. Com uma case USB e um Android que sirva de servidor, esse disco ganha uma nova função: espaço extra para as fotos, os vídeos e os documentos da casa.

![Servidor DogNAS com um HD externo em um dock USB, acessado pelo celular.](assets/photos/usb-drive.webp)

## O que você precisa

- Um **HD ou SSD de notebook** que ainda funcione. Antes de usar, copie para outro lugar qualquer coisa que ainda esteja nele.
- Uma **case ou dock USB** compatível com o formato do disco.
- Um **celular ou tablet Android com USB OTG**, que é o que permite ligar discos USB ao aparelho, e o cabo ou adaptador certo.
- O **DogNAS** instalado nesse Android, que será o servidor.

## Passo a passo

1. Coloque o disco na case USB e confirme que ele aparece normalmente.
2. Ligue a case ao Android pelo cabo OTG.
3. No DogNAS, escolha o disco USB como o lugar onde os arquivos serão guardados e toque em Iniciar.
4. Crie os perfis e conecte os outros aparelhos por QR Code e PIN.

A partir daí, o disco é o armazenamento do seu servidor, acessado pelo Wi-Fi da casa.

## Cuidados importantes

- **Energia.** HDs mecânicos podem pedir mais energia do que o celular fornece. Se o disco não ligar ou desconectar, use um hub USB com fonte própria. SSDs costumam gastar menos.
- **Compatibilidade.** O resultado depende do aparelho, da case e do disco. Teste antes de depender dele.
- **Um disco, sem redundância.** O DogNAS não junta vários discos num único volume e não faz backup por conta própria. Um disco pode falhar, e um disco antigo, mais ainda. Mantenha uma cópia independente do que é importante.
- **Espaço.** No plano Grátis, o DogNAS gerencia até 64 GB, mesmo que o disco seja maior. O Pro, compra única e sem assinatura, usa o disco inteiro.

## Vale a pena?

Se você já tem o disco e a case, o custo é quase zero, e o resultado é um servidor com bastante espaço para a família. Se for comprar tudo do zero, compare com um NAS ou com um SSD externo, e veja [NAS tradicional ou servidor Android](/blog/nas-tradicional-ou-servidor-android/) para decidir.

Para montar o servidor, comece por [como transformar um Android antigo em servidor de arquivos](/blog/transformar-android-antigo-em-servidor-de-arquivos/).

---
slug: fotos-sem-depender-so-da-nuvem-regra-3-2-1
title: "Fotos sem depender só da nuvem: a regra 3-2-1 em casa"
summary: A nuvem é uma cópia, não um cofre. Veja como guardar as fotos da família em mais de um lugar com a regra 3-2-1, usando um servidor em casa e um HD que você já tem.
meta_title: Fotos além da nuvem: a regra 3-2-1 em casa | DogNAS
meta_description: Fotos só na nuvem ou só no celular? A regra 3-2-1 explicada de forma simples: três cópias, duas mídias, uma fora de casa, com um servidor em casa.
pillar: storage
tags: [backup de fotos, regra 3-2-1, armazenamento em nuvem, fotos da família, servidor em casa]
cover: assets/blog/google-storage-full/cover-pt.webp
cover_alt: Celular com o servidor DogNAS ligado por cabo, ao lado de um HD em uma caixa de apoio, sobre uma mesa
social_image: assets/blog/google-storage-full/social-pt.jpg
cta: server
related: [google-storage-full, cloud-subscription-savings, android-nas-server, free-phone-space, pc-phone-transfer]
status: published
translation_review: reviewed
reviewed_by: Paulo Leite
created: 2026-11-27
published: 2026-11-27
updated: 2026-11-27
---
As fotos da maioria das pessoas vivem em dois lugares: o celular e um aplicativo que sincroniza com a nuvem. Parece seguro, mas é menos do que parece. Se o celular for perdido e a conta for bloqueada, ou se a sincronização parar sem avisar, não sobra nada para onde voltar.

A nuvem é ótima, e ninguém precisa abandoná-la. O ponto é deixar de ser o único lugar. Existe uma regra antiga e simples para isso, e ela cabe numa casa comum.

> [!takeaways]
> - A **regra 3-2-1**: 3 cópias do que importa, em 2 tipos diferentes de mídia, com 1 delas fora de casa.
> - O celular, a nuvem e um servidor em casa contam como cópias, mas uma nuvem que espelha o celular pode apagar lá o que você apagar aqui.
> - Um servidor em casa é uma cópia, não um backup por si só. Some um segundo HD e uma cópia em outro lugar.

## Por que "sincronizado" não é "com backup"

Muitos aplicativos de fotos *sincronizam*: o que acontece de um lado acontece no outro. Apague uma foto sem querer no celular e ela pode sumir da nuvem também (em geral fica um tempo na lixeira, depois vai embora). Uma segunda cópia de verdade é aquela que um erro na primeira não alcança.

Lembre também que a conta é um ponto único: senha esquecida, conta bloqueada, plano vencido e biblioteca que não cabe mais. Por isso a regra pede cópias que não dependam umas das outras.

## A regra 3-2-1, traduzida para uma casa

- **3 cópias.** O original (o que está no celular conta) mais outras duas.
- **2 tipos de mídia.** Não ponha todas as cópias no mesmo tipo de coisa. Celular e conta na nuvem já são dois. Some um HD e você tem três.
- **1 fora de casa.** Incêndio, enchente, roubo ou uma descarga elétrica atingem tudo em casa de uma vez. Uma cópia precisa morar em outro lugar: a nuvem costuma cumprir bem esse papel.

Nada disso torna uma perda impossível. Só torna muito menos provável perder tudo ao mesmo tempo.

## Um arranjo realista com o que você já tem

Não é preciso comprar equipamento. Um arranjo que usa o que provavelmente está na sua gaveta:

1. **Cópia 1: o celular** em que você fotografa. Serve enquanto ele estiver vivo.
2. **Cópia 2: um servidor em casa.** Um celular ou tablet Android antigo com o DogNAS, na tomada e no seu Wi-Fi, guarda as fotos na sua rede. Veja [como transformar um Android antigo em servidor de arquivos](/pt/blog/transformar-android-antigo-em-servidor-de-arquivos/).
3. **Cópia 3: fora de casa.** A nuvem que você já usa, mesmo no plano grátis, ou um HD externo que fique na casa de um parente.

São 3 cópias, em 3 tipos de mídia, com 1 fora de casa. Se a conta na nuvem já está lotada, a ordem de [Google Drive ou Fotos cheio](/pt/blog/google-drive-fotos-cheio-guardar-em-casa/) ajuda a trazer a parte pesada para casa sem perder nada.

> [!warning]
> Um servidor em casa é uma cópia dos seus arquivos, não um backup que se cuida sozinho. O DogNAS não espelha, não repete nem restaura nada por conta própria, não une discos em um volume só, e o aparelho pode falhar como qualquer outro. Por isso a regra pede mais de uma cópia.

## Como levar as fotos para o servidor hoje

Há algumas formas simples, e nenhuma exige conta na nuvem:

- **Pelo celular:** abra o DogNAS Client e envie as pastas da câmera para o servidor, como num envio normal.
- **Pelo computador:** conecte com FileZilla ou WinSCP e arraste as pastas. Os passos estão em [como acessar o DogNAS pelo FileZilla, WinSCP, Cyberduck e rclone](/pt/blog/acessar-dognas-pelo-filezilla-winscp-cyberduck-rclone/).
- **Uma cópia avulsa sem cabo:** [PC e celular pelo Wi-Fi](/pt/blog/transferir-arquivos-entre-pc-e-celular-pelo-wifi/).

Hoje é uma rotina manual: você escolhe o que enviar e quando. Um bom hábito é mandar as fotos do mês no primeiro fim de semana do seguinte e conferir que abriram antes de liberar espaço no celular.

## Hábitos que fazem funcionar

- **Nomeie por data.** Pastas como `2026/11-novembro` são fáceis de comparar e de achar daqui a anos.
- **Confira, não presuma.** De vez em quando abra algumas fotos antigas da cópia. Um backup que você nunca abriu é uma esperança.
- **Não apague do celular antes de existirem duas cópias.** Veja [como liberar espaço no Android](/pt/blog/como-liberar-espaco-no-celular-android/).
- **Mantenha a cópia fora de casa em dia**, ou ao menos lembre quando foi a última atualização.
- **Cuide do aparelho.** Ele precisa de energia, ventilação e um Wi-Fi ao alcance. Um Android muito antigo pode ficar sem atualizações, então evite expô-lo além da sua rede de casa.

## Isso substitui a nuvem?

Não necessariamente. A nuvem é cômoda para ver de qualquer lugar e para compartilhar, e cumpre bem o papel de "fora de casa". O que muda é que ela deixa de ser a única cópia e a única razão de pagar um plano maior todo mês. Se o custo é a preocupação, veja [como economizar nas assinaturas de armazenamento em nuvem](/pt/blog/como-economizar-assinaturas-de-armazenamento-em-nuvem/).

## Perguntas rápidas

?? Uma conta na nuvem é um backup?
É uma cópia, e útil, mas a sincronização pode espalhar um erro ou uma exclusão. Trate-a como uma cópia entre várias, não como a única.

?? Preciso de dois servidores em casa?
Não. Um servidor em casa mais uma cópia fora de casa já cumpre a regra. Um segundo HD só acrescenta uma camada.

?? O servidor pode ser um celular que eu não uso mais?
Pode, um Android 7.0 ou mais novo, na tomada e no seu Wi-Fi. O [guia de servidor NAS no Android](/pt/blog/servidor-nas-android-guia-completo/) mostra o que funciona e onde para.

?? O DogNAS faz backup automático das minhas fotos?
Hoje não. O envio é manual, pelo Client ou pelo computador. Uma opção automática é algo em que estamos trabalhando, mas só contamos com ela quando estiver na loja.

## Por onde começar

Conte quantas cópias das suas fotos existem agora e onde estão. Se a resposta é "o celular e a nuvem", acrescente uma em casa neste fim de semana e anote quando vai atualizá-la de novo.

---
slug: google-drive-fotos-cheio-guardar-em-casa
title: Google Drive ou Google Fotos cheio? Como tirar tudo de lá e guardar em casa
summary: Passo a passo para exportar suas fotos e arquivos do Google, guardar em um servidor seu em casa e só então liberar espaço na conta, sem pagar mais por mês.
meta_title: Google Fotos cheio: como guardar suas fotos em casa | DogNAS
meta_description: Google Drive ou Fotos lotado? Veja como exportar com o Google Takeout, guardar tudo em um servidor seu em casa e liberar espaço na conta sem pagar mais.
pillar: storage
tags: [google fotos cheio, google drive cheio, google takeout, armazenamento em nuvem, servidor em casa]
cta: server
related: [android-nas-server, cloud-subscription-savings, free-phone-space, pc-phone-transfer, sftp-clients]
status: review
translation_review: pending
created: 2026-11-26
published: 2026-11-26
updated: 2026-11-26
---
Chega o aviso: "seu armazenamento está quase cheio". O e-mail pode parar de chegar, e o Google Fotos deixa de guardar o que você tira. A saída mais rápida é pagar um plano. Só que a mensalidade não acaba mais, e o espaço de uma conta sempre enche de novo.

Existe outro caminho: tirar o que é pesado de lá, guardar em casa e ficar com a conta limpa. Dá trabalho no começo, mas é feito uma vez só. Abaixo vai a ordem que faz sentido, com os cuidados que as pessoas costumam esquecer.

> [!takeaways]
> - Exportar pelo **Google Takeout** gera uma cópia. Nada some da sua conta até você apagar.
> - Guarde a cópia em um servidor seu (um Android parado em casa serve) e **confira** antes de apagar qualquer coisa no Google.
> - Um servidor em casa não é backup. Para o que não tem volta, mantenha uma segunda cópia em outro lugar.

## Antes de tudo: o que está ocupando espaço

O espaço grátis (hoje 15 GB, valor que o Google pode mudar) é dividido entre Gmail, Drive e Fotos. Abra a tela de armazenamento da conta e veja qual dos três pesa mais. Quase sempre é o Fotos, e às vezes uma pasta esquecida no Drive ou anexos antigos no Gmail.

Isso importa porque muda o que você vai exportar. Se o problema é um vídeo de 4 GB no Drive, você nem precisa de Takeout: baixa o arquivo e pronto.

## Passo 1: tenha onde guardar

Antes de baixar qualquer coisa, decida para onde ela vai. Pode ser um HD, mas se você já tem um celular ou tablet Android na gaveta, dá para transformá-lo em um servidor de arquivos na sua rede Wi-Fi. A gente explica isso em [como transformar um Android antigo em servidor de arquivos](/blog/transformar-android-antigo-em-servidor-de-arquivos/) e no [guia completo do servidor NAS no Android](/blog/servidor-nas-android-guia-completo/).

Faça uma conta rápida de tamanho. O plano Grátis do DogNAS gerencia até 64 GB. Se a sua biblioteca do Google tem 150 GB, vai precisar do Pro (compra única, sem assinatura), que usa o armazenamento inteiro do aparelho, inclusive cartão SD ou disco USB.

## Passo 2: exporte com o Google Takeout

O Takeout é a ferramenta do próprio Google para baixar seus dados (takeout.google.com).

1. Entre com a conta que está cheia e deixe marcado só o que você quer: **Google Fotos**, **Drive**, ou os dois. Desmarcar o resto deixa a exportação bem mais leve.
2. No Drive e no Fotos dá para escolher só alguns álbuns ou pastas. Se a biblioteca é enorme, vale fazer em etapas.
3. Escolha o formato do arquivo e o tamanho das partes. Partes menores (2 GB, por exemplo) são mais fáceis de baixar e de repetir se uma falhar.
4. Peça a exportação e espere. Para bibliotecas grandes pode levar de horas a alguns dias. O Google avisa por e-mail.
5. Baixe todas as partes. O link fica disponível por tempo limitado, então não deixe para depois.

> [!note]
> As fotos costumam vir acompanhadas de arquivos `.json` com a data e o local originais. Se você abrir a pasta e achar estranho, é isso. Não apague esses arquivos antes de ver como o seu programa de fotos trata as datas.

## Passo 3: leve para o servidor

Depois de baixar, descompacte e copie para o seu servidor. Duas formas simples:

- **Pelo computador:** abra o servidor com um programa como o FileZilla ou o WinSCP e arraste as pastas. Está tudo em [como acessar o DogNAS pelo FileZilla, WinSCP, Cyberduck e rclone](/blog/acessar-dognas-pelo-filezilla-winscp-cyberduck-rclone/). Outro caminho é o [Wi-Fi entre PC e celular](/blog/transferir-arquivos-entre-pc-e-celular-pelo-wifi/).
- **Pelo celular:** se você baixou o Takeout direto no celular, envie as pastas pelo DogNAS Client.

Transferência grande pelo Wi-Fi é lenta de verdade. Deixe o computador ligado e o servidor na tomada, e não mexa nele durante a cópia.

## Passo 4: confira antes de apagar

Esse é o passo que ninguém quer fazer e todo mundo devia. Antes de tirar qualquer coisa do Google:

- Compare a quantidade: quantos arquivos o Google dizia que havia e quantos chegaram.
- Abra algumas fotos e vídeos de épocas diferentes, de preferência os mais pesados. Veja se tocam.
- Procure uma pasta que você sabe que existe, de um evento específico.
- Se possível, copie também para um segundo lugar (um HD externo). O servidor em casa guarda os arquivos, mas não faz backup sozinho, e discos falham.

## Passo 5: libere espaço na conta

Só agora apague, e aos poucos. No Google Fotos, o que vai para a lixeira continua ocupando espaço até ser esvaziada. No Drive é igual. E "liberar espaço" no app do celular costuma tirar só a cópia local, sem mexer no que está na nuvem. Leia o que o botão faz antes de tocar.

Apagar aos poucos tem uma vantagem: se você notar que faltou algo, ainda dá para voltar.

## E se eu continuar usando o Google Fotos?

Muita gente faz isso, e tudo bem. O Fotos é ótimo para ver as fotos de qualquer lugar e compartilhar um álbum. O servidor em casa é bom para o volume e para a privacidade, mas só se acessa de dentro da rede da casa. Um meio-termo comum: manter os últimos meses na nuvem e mandar o resto para casa de tempos em tempos.

Se o objetivo é pagar menos, vale ler também [como economizar nas assinaturas de armazenamento em nuvem](/blog/como-economizar-assinaturas-de-armazenamento-em-nuvem/) e [como liberar espaço no celular Android](/blog/como-liberar-espaco-no-celular-android/).

## Perguntas rápidas

?? Exportar pelo Takeout apaga meus arquivos do Google?
Não. O Takeout só gera uma cópia para você baixar. As fotos e arquivos continuam na conta até você apagá-los.

?? Posso fazer isso só pelo celular?
Pode, mas a exportação é grande e a cópia pelo celular é mais lenta. Para bibliotecas grandes, o computador facilita.

?? Meu servidor pode ser um celular que não uso mais?
Pode. Um Android 7.0 ou mais novo, ligado na tomada e no seu Wi-Fi, já resolve. O [guia do servidor NAS no Android](/blog/servidor-nas-android-guia-completo/) mostra o que funciona e onde ele para.

?? Isso é um backup?
Não por si só. É uma cópia em casa, que depende do aparelho e do disco. Para o que é insubstituível, mantenha uma segunda cópia em outro lugar.

## Por onde começar

Abra a tela de armazenamento da sua conta Google, veja o que pesa e comece por uma exportação pequena, só para ver como funciona. Quando o primeiro lote chegar bem ao servidor, o resto é repetir.

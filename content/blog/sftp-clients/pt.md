---
slug: acessar-dognas-pelo-filezilla-winscp-cyberduck-rclone
title: Como acessar o DogNAS pelo FileZilla, WinSCP, Cyberduck e rclone
summary: Passo a passo para conectar o seu servidor DogNAS a quatro programas SFTP populares e escolher o melhor para o seu uso.
meta_title: Acessar o DogNAS pelo FileZilla, WinSCP, Cyberduck | DogNAS
meta_description: Como conectar o servidor DogNAS ao FileZilla, WinSCP, Cyberduck e rclone por SFTP, com o que preencher em cada um e qual escolher.
category: Guias
tags: [filezilla, winscp, cyberduck, rclone, sftp]
cover: assets/blog/sftp-clients/cover-pt.webp
cover_alt: Tela inicial do DogNAS Client Lite em um Android, ao lado do mascote do DogNAS
social_image: assets/blog/sftp-clients/social-pt.jpg
cta: both
related: [sftp-explained, pc-phone-transfer, old-android-server]
status: published
translation_review: reviewed
created: 2026-10-28
published: 2026-10-28
updated: 2026-10-28
---
O DogNAS fala SFTP, então qualquer programa que entenda esse protocolo consegue acessar os arquivos do seu servidor. Este guia mostra como conectar quatro dos mais usados e ajuda a escolher. Se você ainda não sabe o que é SFTP, comece por [o que é SFTP](/blog/o-que-e-sftp-como-acessar-servidor-android/).

## Antes de tudo: os dados de conexão

Em qualquer programa, você vai precisar do mesmo conjunto de informações: **endereço do servidor (host), porta, usuário e senha**. O servidor DogNAS mostra esses dados na tela "Como conectar seu PC ou iPhone". O computador precisa estar na mesma rede Wi-Fi do servidor, e o servidor precisa estar ligado.

Na primeira conexão, o programa mostra a **impressão digital (fingerprint)** da chave do servidor e pede para você confiar nela. Aceite quando o aparelho for o seu. Se ela mudar depois sem motivo, desconfie.

## FileZilla (Windows, Mac e Linux)

É o mais conhecido e funciona nos três sistemas.

1. Abra o Gerenciador de Sites e crie um novo site.
2. Em Protocolo, escolha **SFTP**.
3. Preencha host, porta, usuário e senha com os dados do servidor.
4. Conecte e arraste os arquivos entre o lado do computador e o lado do servidor.

## WinSCP (Windows)

Tem uma interface parecida com a do Explorador de Arquivos e é bom para quem usa só Windows.

1. Na tela de login, escolha **SFTP** como protocolo de arquivo.
2. Preencha nome do host, porta, usuário e senha.
3. Salve a sessão e conecte.

## Cyberduck (Windows e Mac)

Simples e visual, popular entre quem usa Mac.

1. Clique em Abrir conexão e escolha **SFTP** na lista.
2. Preencha servidor, porta, usuário e senha.
3. Conecte e navegue pelas pastas como em um navegador de arquivos.

## rclone (linha de comando)

Para quem gosta de automação e scripts.

1. Rode `rclone config`, crie um novo remoto e escolha o tipo **sftp**.
2. Informe host, porta, usuário e senha.
3. Use comandos como `rclone ls` e `rclone copy` para listar e copiar arquivos entre o computador e o servidor.

## Qual escolher

- **Quer o mais simples no Mac:** Cyberduck.
- **Usa Windows e quer algo parecido com o Explorador:** WinSCP.
- **Usa mais de um sistema:** FileZilla.
- **Quer automatizar cópias:** rclone.

![Tela inicial do DogNAS Client Lite](assets/shots/pt/lite-home.webp)
![Arquivos do DogNAS no Client Lite](assets/shots/pt/lite-files.webp)
![Fila de transferências no celular](assets/shots/pt/lite-transfers.webp)

## Cuidados

- **Senha e PIN.** Não compartilhe os dados de conexão. Você pode revogar a credencial de um aparelho quando quiser.
- **Não é backup.** Copiar para o servidor guarda os arquivos em outro lugar, mas o DogNAS não faz backup sozinho. Mantenha uma cópia independente do que é importante.
- **No celular,** use o DogNAS Client Lite, com QR Code e PIN, em vez de um cliente SFTP genérico.

Para montar o servidor, veja [como transformar um Android antigo em servidor de arquivos](/blog/transformar-android-antigo-em-servidor-de-arquivos/).

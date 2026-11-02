---
slug: whatsapp-lotando-o-celular-como-liberar-espaco
title: WhatsApp lotando o celular: como tirar fotos e vídeos sem perder as conversas
summary: O WhatsApp costuma ser o maior consumidor de espaço do Android. Veja onde ficam as mídias, como copiá-las para um servidor seu em casa e só então apagar do celular.
meta_title: WhatsApp lotando o celular: como liberar espaço | DogNAS
meta_description: O WhatsApp encheu o seu Android? Veja onde ficam as mídias, como copiá-las para um servidor seu em casa com o DogNAS e liberar espaço sem apagar as conversas.
pillar: storage
tags: [whatsapp, liberar espaço, armazenamento, android, fotos e vídeos]
cover: assets/blog/free-phone-space/cover-pt.webp
cover_alt: Ilustração de um celular com uma seta tirando arquivos ao lado da tela do DogNAS Client Lite
social_image: assets/blog/free-phone-space/social-pt.jpg
cta: client
related: [free-phone-space, old-android-server, pc-phone-transfer]
status: review
translation_review: pending
created: 2026-11-01
updated: 2026-11-01
---
**O WhatsApp enche o celular porque guarda no aparelho toda foto, vídeo, áudio e documento que passa pelos seus grupos**, mesmo os que você nunca abriu. A saída que preserva o que importa é copiar essas mídias para um lugar seu, conferir, e só então apagar do celular. As conversas em texto continuam no app.

> [!takeaways]
> - As mídias ficam em pastas do próprio celular, que você pode copiar. No Android 11 ou mais novo: `Android/media/com.whatsapp/WhatsApp/Media`. No Android 10 ou mais antigo: `WhatsApp/Media`.
> - Dá para copiar essas pastas para um servidor seu em casa com o DogNAS, sem nuvem e sem mensalidade, e depois apagar do celular.
> - Apagar a mídia **não apaga o texto** da conversa, mas o arquivo pode não voltar. Se a pessoa que enviou também o apagou, não há como baixar de novo. Por isso, confira a cópia antes.
> - Isto copia **mídias**. Não é backup nem restauração do histórico de conversas, e o DogNAS não promete isso.

## Por que o WhatsApp ocupa tanto espaço

Por padrão, o WhatsApp baixa automaticamente as fotos e, conforme a sua configuração, vídeos e documentos. Grupos de família, trabalho e condomínio mandam dezenas de arquivos por dia, e tudo fica no celular. Com o tempo, o app passa dos gigabytes sem você perceber.

O primeiro passo é ver o tamanho do problema: no WhatsApp, abra Configurações, Armazenamento e dados, e Gerenciar armazenamento. Ele lista as conversas que mais ocupam espaço e os arquivos grandes ou encaminhados muitas vezes. Os nomes dos menus mudam um pouco conforme a versão.

## Onde ficam as mídias

Os caminhos dependem da versão do Android:

| | Android 11 ou mais novo | Android 10 ou mais antigo |
|---|---|---|
| WhatsApp | `Android/media/com.whatsapp/WhatsApp/Media` | `WhatsApp/Media` |
| WhatsApp Business | `Android/media/com.whatsapp.w4b/WhatsApp Business/Media` | `WhatsApp Business/Media` |

Dentro de `Media` há uma pasta por tipo: `WhatsApp Images`, `WhatsApp Video`, `WhatsApp Audio`, `WhatsApp Voice Notes`, `WhatsApp Documents`, e uma subpasta `Sent` com o que você enviou. Os nomes podem variar com o idioma e a versão do app.

> [!note]
> Nas versões novas do Android, o seletor de arquivos do sistema pode não mostrar a pasta `Android/media`. Se for o seu caso, use um gerenciador de arquivos para copiá-la para uma pasta comum, como Downloads, e envie de lá. Não testamos todos os fabricantes.

## Passo a passo com o DogNAS

Você precisa de um servidor DogNAS em casa. Um [Android antigo serve de servidor de arquivos](/blog/transformar-android-antigo-em-servidor-de-arquivos/) e, com um HD ou pendrive, o espaço cresce. No celular cheio, use o DogNAS Client (ou o mais leve DogNAS Client Lite), gratuito.

1. **Veja o que pesa.** No WhatsApp, abra Gerenciar armazenamento e anote as conversas maiores.
2. **Crie uma pasta no servidor**, por exemplo `WhatsApp-2026`, e pareie o celular com o QR Code e o PIN do perfil.
3. **Envie as pastas de mídia** pelo botão de enviar, escolhendo `WhatsApp Images`, `WhatsApp Video` e, se quiser, `Documents` e `Voice Notes`. A fila de transferências mostra o progresso e retoma se o Wi-Fi cair.
4. **Confira no servidor.** Abra algumas fotos e vídeos e compare o número e o tamanho dos arquivos com o celular.
5. **Só então apague do celular**, pelo próprio WhatsApp (Gerenciar armazenamento) ou apagando as pastas copiadas.

## Cuidados importantes

- **Confira antes de apagar.** É o passo que evita o arrependimento.
- **Apagar a mídia mantém o texto**, e a conversa mostra o arquivo como indisponível. Se ele ainda estiver no WhatsApp de quem enviou, às vezes dá para baixar de novo; se não estiver, ele só existirá na sua cópia.
- **Não é backup do WhatsApp.** O backup do histórico de conversas é o do próprio app (Google Drive). O DogNAS guarda os arquivos de mídia que você copiar e não restaura conversas.
- **Uma cópia só não é segurança.** O DogNAS guarda no disco que você escolher. Para fotos insubstituíveis, tenha uma segunda cópia em outro lugar.
- **Só na sua rede.** O envio é pelo Wi-Fi de casa, com o servidor ligado e conectado.

## Evite que lote de novo

- No WhatsApp, em Armazenamento e dados, ajuste o download automático para só Wi-Fi ou desligue-o para vídeos e documentos.
- Silencie o download em grupos grandes.
- Repita a cópia de tempos em tempos, por exemplo uma vez por mês. O envio é manual hoje; uma cópia automática ainda não faz parte do DogNAS.

## Perguntas frequentes

?? Posso apagar as mídias sem perder as conversas?
Sim. O texto fica; os arquivos apagados aparecem como indisponíveis. Por isso copie e confira antes.

?? O DogNAS faz backup do WhatsApp?
Não. Ele guarda os arquivos de mídia que você copiar para o servidor. O histórico de conversas continua sendo o backup do próprio WhatsApp.

?? E se o seletor não mostrar a pasta do WhatsApp?
Em Android novos, copie a pasta com um gerenciador de arquivos para Downloads e envie de lá.

## Resumo

Veja o que o WhatsApp ocupa, copie as pastas de mídia para um servidor seu, confira e só então apague do celular. Se ainda não tem onde guardar, comece por [como liberar espaço no celular Android](/blog/como-liberar-espaco-no-celular-android/) e [use um Android antigo como servidor](/blog/transformar-android-antigo-em-servidor-de-arquivos/).

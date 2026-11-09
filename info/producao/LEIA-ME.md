# Info Imobiliária (infoimobiliaria.com, «Info Imobiliária, by OMNI») - método de produção das redes

Repositório público: só media (vídeos e imagens), a fila e o método. Nunca dados pessoais, chaves ou credenciais.

## Cadência (todos os dias, sem dias em branco)
Por dia: 3 vídeos (FB Reels, IG Reels, TikTok, YouTube Shorts), 1 carrossel (5 slides) e 1 imagem (FB+IG), mais stories (FB+IG) de tudo.
Assuntos diferentes entre si no mesmo dia. Horas de Lisboa variadas (vídeos de manhã, ao início da tarde e à noite; carrossel a meio da manhã/tarde; imagem à tarde), diferentes de dia para dia. Calcular UTC com zoneinfo Europe/Lisbon, nunca à mão.
Stories: vídeo +25 min depois do post; imagem +30 min; carrossel: slide 1 a +30 min e os seguintes de 12 em 12 min.

## Regras de conteúdo (do Marco)
- Português de Portugal, «tu». Nunca o travessão «—» (usar «-»). «e-mail» com hífen.
- Uma frase por linha nas legendas.
- Só factos reais: os das páginas do site infoimobiliaria.com (calculadoras, glossário, guias, notícias PUBLICADAS) e fontes oficiais/imprensa lidas na íntegra. Nunca estatísticas, percentagens ou «regras» inventadas. Propostas dizem-se propostas. Exemplos de contas: etiquetados «Exemplo calculado por nós» e verificados com `assert` em Python.
- Cada peça tem imagem/layout próprio; peso baixo (imagens ~120 KB, vídeos ~1,5 a 2 MB).
- Música nos vídeos (já tratada pelo render_semana.py). Capa = fotograma dos 3 s (tratada pelo motor).
- Não repetir assuntos da fila nem das últimas semanas no Planable (mesmo ângulo).

## Ficheiros
- `engine.py`: motor (vídeo 1080x1920, imagem/carrossel 1080x1350). `modelos.py`: V (vídeo), C (carrossel), I (imagem), END, walk (espaços inseparáveis).
- `exemplo_semana.py`: peças da semana 10-16/11/2026 (vê-se o formato dos elementos: h, p, pn, card, chk, num, pair, btn). Copia o estilo; não copies os assuntos.
- `exemplo_plano.py`: como se montam legendas (função cap), horas e plan.json.
- `render_semana.py <modulo> <saida>`: renderiza e dá os nomes finais. Chaves do dicionário D: `AAAAMMDDv1|v2|v3|c|i`.
- `musica/`, `fontes/`, `logo.png`.

## Legenda (FB e IG iguais)
Linhas curtas com os factos, depois `infoimobiliaria.com` + `(Link também na bio.)`, `Fonte: ...`, `Informação geral. Confirma com um advogado ou solicitador.` (quando aplicável), `Info Imobiliária, by OMNI`, hashtags (5, incl. #infoimobiliária). Vídeos têm também youtubeTitle (<=100 caracteres).

## Planable (workspace dMPBLva5aMPaETb9z)
Páginas: Facebook 6Ph4fgFpnPJsbWgxQ, Instagram BcGXHC36eR33sDkZa, TikTok CxTdN62ZyFmBKxoKL, YouTube EcyNkDkGbdkfbB52B.
- Vídeo: create_grouped_post nas 4 páginas, classification «reels», mediaUrls [mp4], youtubeTitle, scheduledAt, publishAtScheduledDate true.
- Carrossel: FB+IG, classification «post», 5 URLs por ordem. Imagem: FB+IG, «post», 1 URL.
- Stories: FB+IG, classification «story», sem texto, 1 media por story (vídeo: o mesmo mp4; imagem/carrossel: os `-story.jpg`).
- publishAtScheduledDate TEM de ser true (com false fica rascunho e não se converte). Não aprovar (approved fica false). Não há ferramenta para apagar: confirmar duplicados antes (list_posts no mesmo instante).
- URLs de media: https://cdn.jsdelivr.net/gh/ernesto978/media-prosta@<SHA>/info/m/<ficheiro> (SHA completo do commit onde o ficheiro entrou). Do shell não se abre este domínio: é normal.
- Os vídeos mostram «Media is still processing» logo após a criação; confirmar mais tarde com get_post.

## Fila (info/fila/fila.json)
Uma entrada por peça: data, hora_lisboa, scheduledAt_utc, tipo (video|carrossel|imagem), assunto, fonte, ficheiros (nomes), commit (SHA completo), titulo_youtube (vídeos), legenda, stories (lista de {ficheiros, scheduledAt_utc}), estado (pronto|agendado|falhou) e planable_ids.
`ultimo_dia_agendado_ate` no topo do ficheiro regista o último dia já tratado.

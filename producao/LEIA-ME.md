# Produção de peças para as redes do prostata.pt

Método para criar imagens (1080x1350), carrosséis (1080x1350, 6 a 8 slides) e vídeos (1080x1920, com capa de 0,6 s e música gerada por código).

## Como se usa
1. Escrever um `spec.json` (formato abaixo) numa pasta de trabalho, com as fotos de fundo ao lado.
2. `python3 render.py spec.json saida/`
3. Copiar os resultados para `m/` do repositório, fazer commit e push.
4. URL público para o Planable: `https://cdn.jsdelivr.net/gh/ernesto978/media-prosta@<SHA_DO_COMMIT>/m/<ficheiro>` (usar o SHA completo do commit; o jsDelivr serve o tipo de ficheiro certo, o raw.githubusercontent.com não serve mp4 como vídeo).

## Formato do spec.json
```json
{"pecas":[
 {"chave":"img-alimentacao-peixe","tipo":"imagem","tema":"alimentacao","fundo":"peixe.jpg",
  "titulo":"...","texto":["parágrafo", {"destaque":"parágrafo a creme"}],"fonte":"Fonte: NHS"},
 {"chave":"car-tratamento-x","tipo":"carrossel","tema":"tratamento","fundo":"x.jpg",
  "slides":[{"titulo":"capa"},{"titulo":"2. ...","texto":"..."},{"titulo":"Faça o teste de sintomas em prostata.pt"}]},
 {"chave":"vid-prevencao-y","tipo":"video","tema":"prevencao","fundo":"y.jpg","capa":"Título da capa","bpm":112,
  "cenas":[{"titulo":"...","sub":"...","seg":5},{"titulo":"Faça o teste em prostata.pt","seg":4}]}
]}
```
- `tema`: `alimentacao` (verde), `tratamento` (azul), `prevencao` (laranja).
- Nomes de ficheiro: `img-<tema>-<assunto>.jpg`, `car-<tema>-<assunto>-NN.jpg`, `vid-<tema>-<assunto>.mp4` (a capa sai como `capa-...jpg`).
- Os vídeos devem ter 25 a 35 s (cenas de 4 a 6 s). O último slide/cena convida a fazer o teste de sintomas em prostata.pt.

## Fotos de fundo
- Geradas com o fal (modelo `fal-ai/flux/schnell`, `image_size` 896x1120, 4 passos, `output_format` jpeg). Sempre «no text».
- Uma foto NOVA e diferente por peça. Nunca reutilizar fotos já usadas (listar `m/` e a pasta `fotos/` do repositório).
- De vez em quando (regra do Marco), uma foto com homens do público-alvo (mais de 50 anos), de aspeto natural e sóbrio. Nunca pessoas tristes ou doentes.
- Guardar as fotos usadas em `fotos/` (jpg, largura 1080 máx., qualidade 80) para memória do que já foi usado.
- As imagens finais devem ficar leves (imagens < 250 KB, slides < 150 KB).

## Regras de conteúdo (do Marco)
- Português de Portugal; tratar o leitor por «você» sem usar a palavra (ex.: «Faça o teste»). Sem «tu» nestas peças.
- Só factos lidos nas páginas publicadas do prostata.pt ou nas fontes citadas lá (NHS, Associação Portuguesa de Urologia, etc.). Nunca inventar números, regras com nome nem histórias. Avisar quando a fonte é britânica.
- Não afirmar que suplementos (serenoa/saw palmetto, etc.) funcionam ou não.
- Cada legenda termina com o fecho: «Faça o teste de sintomas em prostata.pt (link na bio).» e «Informação geral. Não substitui a consulta com um médico.», seguido das hashtags (`#próstata`, uma de tema, `#prostatapt`).
- Em linhas separadas: cada frase na sua linha.
- Escrever «e-mail» com hífen, se aparecer.

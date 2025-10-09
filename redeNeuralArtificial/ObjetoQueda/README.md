# RNAutonomiaPeso — Queda Livre

Este diretório contém material para uma pequena demonstração de queda livre e como treinar uma rede neural para aprender a relação entre tempo e distância.

Conteúdo

- `QuedaLivre_colab.ipynb` — notebook pronto para executar no Google Colab: explica a física, gera dataset (treino/teste), treina um modelo Keras, avalia e salva o modelo, e mostra exemplos de predição.

Como usar

1. Abra `QuedaLivre_colab.ipynb` no Google Colab (ou Jupyter local).
2. No Colab, monte o Google Drive se quiser salvar o modelo: `from google.colab import drive; drive.mount('/content/drive')`.
3. Execute as células na ordem. O notebook gerará dados, treinará e salvará o modelo em `model/` dentro do ambiente (ou em Drive, se você alterar o caminho).

Fórmula básica

Para queda livre sem resistência do ar e com aceleração da gravidade constante `g`, a equação da posição `s(t)` é:

s(t) = s0 + v0 * t + 0.5 * g * t^2

Usamos por padrão `s0 = 0`, `v0 = 0` e `g = 9.81 m/s^2`, então `s(t) = 0.5 * g * t^2`.

Notas

- O notebook inclui opção para adicionar ruído aos dados para simular medições.
- O modelo predito mapeia `t -> s`. Para estimar `t` a partir de `s`, gere um dataset invertido e treine similarmente.

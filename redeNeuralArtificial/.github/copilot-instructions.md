## Objetivo

Este repositório contém exemplos didáticos de redes neurais em notebooks e modelos Keras (.keras). O objetivo deste arquivo é orientar agentes de IA para serem imediatamente produtivos: onde olhar, convenções do projeto e comandos úteis para desenvolvimento e depuração.

## Visão geral (big picture)

- Estrutura principal: exemplos agrupados por domínio em pastas de alto nível como `DodCat/` (cats vs dogs), `fashion/`, `ObjetoQueda/`, `reconhecerNumero/`, `RNAutonomiaPeso/`.
- Cada pasta normalmente contém notebooks (`.ipynb`), modelos treinados (`*.keras`) e imagens de exemplo. Fluxo comum: abrir o notebook correspondente (ex.: `DodCat/catDogo.ipynb`) para reproduzir o treino, ou usar o arquivo de modelo salvo (`model.keras`) para inferência.

## Dependências e ambiente

- Dependências em `requirements.txt`. Versões fixas (TensorFlow 2.16 / Keras 3.3.3) — use um virtualenv/conda compatível com Python 3.10+.
- Observação: notebooks usam Keras/TensorFlow e bibliotecas comuns (Pillow, matplotlib, numpy). Para evitar problemas em Windows, prefira `tensorflow-intel` ou ajuste conforme CPU/GPU.

## Padrões e convenções do projeto

- Notebooks são a fonte canônica: `*.ipynb` contêm o passo-a-passo. Use-os para entender dados de entrada, pré-processamento e chamadas de treino.
- Modelos exportados seguem extensão `.keras` (Keras SavedModel/ HDF5 export). Carregue com `keras.models.load_model('caminho/model.keras')`.
- Estrutura de dados: diretórios de treino/validação seguem o padrão `train/<class>/` e `validation/<class>/` (por exemplo `DodCat/cats_and_dogs_filtered/train/cats`). Veja `DodCat/cats_and_dogs_filtered/vectorize.py` como utilitário simples para listar imagens.

## Arquivos-chave a inspecionar

- `DodCat/catDogo.ipynb` - notebook de exemplo para classificação cats vs dogs.
- `DodCat/cats_and_dogs_filtered/` - pasta com dataset de treinos/validação e utilitários como `vectorize.py`.
- `fashion/model_fashion.keras` e `reconhecerNumero/mnist_model.keras` - modelos treinados para inferência direta.
- `requirements.txt` - lista completa de dependências e versões.

## Fluxos de trabalho do desenvolvedor (comandos)

- Criar e ativar ambiente (exemplo com venv/powershell):

  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  pip install -r requirements.txt

- Executar notebooks: abra no VS Code ou Jupyter; prefira kernel com Python do `.venv`.
- Carregar modelo em Python:

  from keras.models import load_model
  m = load_model('DodCat/model.keras')

## Padrões de código e estilo observáveis

- Código utilitário simples segue estilo direto — funções curtas e scripts executáveis (`if __name__ == '__main__'`). Ex.: `DodCat/cats_and_dogs_filtered/vectorize.py`.
- Evite modificar notebooks diretamente quando possível; prefira extrair trechos para scripts/modulos para testes automatizados.

## Integrações e pontos de atenção

- Azure / AzureML: muitas dependências `azureml-*` estão listadas. Pode haver integrações legadas com Azure ML; procure por scripts adicionais se precisar de pipelines ou deploy.
- Modelos `.keras` podem depender da versão exata do TensorFlow/Keras usada para treinar — mantenha versões do `requirements.txt` para reproduzir inferência.

## Exemplos concretos que agentes podem modificar

- Para adicionar uma rotina de inferência CLI, crie `scripts/infer_catdog.py` que carrega `DodCat/model.keras` e avalia `DodCat/imagec.jpg`.
- Para automatizar pré-processamento, copie o padrão de `vectorize.py` e expanda: usar `keras.preprocessing.image.load_img` seguido por `img_to_array` e `np.expand_dims`.

## Erros comuns e como detectá-los

- Versão de TF incompatível resulta em erros ao carregar `.keras`. Mensagem típica: "No module named 'tensorflow' or version mismatch". Solução: instalar a versão correta do `requirements.txt`.
- Caminhos relativos: notebooks usam paths relativos (ex.: `train/cats`). Execute scripts a partir da pasta que contém esses diretórios (ex.: `DodCat/cats_and_dogs_filtered`), ou use caminhos absolutos.

## O que não documentar aqui

- Não incluir instruções de alto nível (ex.: “escreva testes”). Concentre-se em padrões observáveis e comandos reprodutíveis neste repositório.

---

Se quiser, eu mesclo qualquer conteúdo existente em um arquivo `.github/copilot-instructions.md` que você já tenha — envie o conteúdo ou diga para mesclar automaticamente. Alguma área que você queira que eu detalhe mais (ex.: scripts de inferência, integração Azure, ou instruções para Windows/WSL)?

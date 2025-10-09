Mini-curso rápido: Keras + TensorFlow

Este mini-curso contém um notebook didático (`keras_minicurso.ipynb`) que explica passo a passo como usar Keras (API do TensorFlow) para treinar um modelo simples em MNIST.

Arquivos:
- keras_minicurso.ipynb : notebook didático com explicações por célula
- train_mnist.py : script que treina e salva um modelo MNIST
- requirements.txt : dependências sugeridas

Como usar:
- Para rodar no Colab: carregue o notebook e execute as células. Colab já possui TensorFlow instalado.
- Para rodar localmente:
  1) Crie um ambiente virtual: python -m venv .venv
  2) Ative e instale: pip install -r requirements.txt
  3) Execute o notebook ou `python train_mnist.py`

Se quiser, eu posso também adicionar uma versão curta em `train_mnist_fast.py` que roda apenas algumas épocas para demonstração rápida.

# MiniCursoPalestra

Repositório com materiais das minhas palestras e mini‑cursos sobre Redes Neurais Artificiais. Contém exemplos, notebooks e slides usados em apresentações.

Principais seções
- CNN/ — material e notebooks sobre Redes Neurais Convolucionais (ex.: classificação de dígitos).
- redeNeuralArtificial/ — conteúdo introdutório e avançado sobre redes neurais artificiais.
- LICENSE — licença MIT.

Como usar
1. Recomendado abrir os notebooks no Google Colab (botão "Open in Colab" nos notebooks) ou executar localmente num ambiente Python isolado.
2. Para execução local (Windows PowerShell):
   - python -m venv .venv
   - .venv\Scripts\Activate.ps1
   - pip install -r requirements.txt  (se houver)
3. No Colab: monte o Google Drive se quiser carregar/salvar modelos (drive.mount('/content/drive')).

Observações rápidas
- Notebooks podem assumir caminhos padrão para modelos (por exemplo `simple_cnn_mnist.h5`). Ajuste conforme necessário.
- Dependências relevantes: Python 3.8+ recomendado, numpy, Pillow, matplotlib, tensorflow/keras conforme notebooks.
- Se usar GPU no Colab, selecione Runtime → Change runtime type → GPU.

Contribuições
Pull requests são bem‑vindas. Para alterações grandes (reorganização de material), abra um issue antes.

Licença
Projeto licenciado sob MIT — veja o arquivo `LICENSE`.

Contato
Para dúvidas ou sugestões, abra um issue neste repositório.
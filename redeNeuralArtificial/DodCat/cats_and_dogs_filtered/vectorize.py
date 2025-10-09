from keras.preprocessing.image import array_to_img, img_to_array, load_img

import os


def list_cat_images(train_dir='train/cats'):
  """Lista arquivos de imagem no diretório de treino de gatos.

  Retorna uma lista de nomes de arquivos. Emite uma mensagem se o
  diretório não existir.
  """
  if not os.path.isdir(train_dir):
    print(f"Diretório não encontrado: {train_dir}")
    return []
  return [fname for fname in os.listdir(train_dir) if os.path.isfile(os.path.join(train_dir, fname))]


if __name__ == '__main__':
  images = list_cat_images()
  for fname in images:
    print(fname)

"""Treina um modelo simples em MNIST e salva em model/mnist.keras"""
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

def build_model(input_shape=(28,28,1), num_classes=10):
    model = keras.Sequential([
        keras.layers.Input(shape=input_shape),
        keras.layers.Rescaling(1./255),
        keras.layers.Conv2D(32, 3, activation='relu'),
        keras.layers.MaxPool2D(),
        keras.layers.Conv2D(64, 3, activation='relu'),
        keras.layers.MaxPool2D(),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model


def main():
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    x_train = x_train[..., np.newaxis]
    x_test = x_test[..., np.newaxis]

    model = build_model()
    model.fit(x_train, y_train, epochs=3, validation_split=0.1)

    os.makedirs('model', exist_ok=True)
    model.save('model/mnist.keras')
    print('Modelo salvo em model/mnist.keras')

if __name__ == '__main__':
    main()

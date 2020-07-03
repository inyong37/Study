# -*- coding: utf-8 -*-
# Modified Author : Inyong Hwang (inyong1020@gmail.com)
# Date            : 2020-07-03-Fri
# Title           : 코딩셰프의 분 딥러닝, 케라스맛 Chapter 5. 케라스로 구현하는 RNN(순환신경망)


from __future__ import print_function
from keras.preprocessing import sequence
from keras.datasets import imdb
import keras
from keras import models, layers
from keras import backend
import numpy as np
from keras.utils import np_utils
import matplotlib.pyplot as plt


def plot_loss(history):
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc=0)


def plot_acc(history):
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc=0)


class Data:
    def __init__(self, max_features=20000, maxlen=80):
        (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
        x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
        x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
        self.x_train, self.y_train = x_train, y_train
        self.x_test, self.y_test = x_test, y_test


class RNN_LSTM(models.Model):
    def __init__(self, max_features, maxlen):
        x = layers.Input((maxlen,))
        h = layers.Embedding(max_features, 128)(x)
        h = layers.LSTM(128, dropout=0.2, recurrent_dropout=0.2)(h)
        y = layers.Dense(1, activation='sigmoid')(h)
        super().__init__(x, y)
        self.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


class Machine:
    def __init__(self, max_features=20000, maxlen=80):
        self.data = Data(max_features, maxlen)
        self.model = RNN_LSTM(max_features, maxlen)

    def run(self, epochs=3, batch_size=32):
        data = self.data
        model = self.model
        print('Training stage')
        print('='*10)
        model.fit(data.x_train, data.y_train, batch_size=batch_size, epochs=epochs, validation_data=(data.x_test, data.y_test))

        score, acc = model.evaluate(data.x_test, data.y_test, batch_size=batch_size)
        print('Test performance: accuracy={0}, loss={1]'.format(acc, score))


def main():
    m = Machine()
    m.run()


if __name__ == '__main__':
    main()

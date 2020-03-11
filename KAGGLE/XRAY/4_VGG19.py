# -*- coding:utf-8 -*-
# Author : Inyong Hwang
# 4. VGG19

import numpy as np
import pickle
from keras.models import Model
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense
from keras.optimizers import Adam
import matplotlib.pyplot as plt
import pandas as pd
import os

modelname = 'vgg19'

origin_dir = 'D:/Dataset/KAGGLE/XRAY/PKL_64/'

with open(origin_dir + 'train_image.pkl', 'rb') as f:
    train_image = pickle.load(f)
with open(origin_dir + 'train_label.pkl', 'rb') as f:
    train_label = pickle.load(f)
with open(origin_dir + 'val_image.pkl', 'rb') as f:
    val_image = pickle.load(f)
with open(origin_dir + 'val_label.pkl', 'rb') as f:
    val_label = pickle.load(f)
with open(origin_dir + 'test_image.pkl', 'rb') as f:
    test_image = pickle.load(f)
with open(origin_dir + 'test_label.pkl', 'rb') as f:
    test_label = pickle.load(f)

train_image = np.array(train_image)
train_label = np.array(train_label)
test_image = np.array(test_image)
test_label = np.array(test_label)
val_image = np.array(val_image)
val_label = np.array(val_label)


def vgg19():
    i = Input(shape=train_image.shape[1:], name='Input_Image')

    x = Conv2D(64, (3, 3), activation='relu', padding='same', name='Conv1_1')(i)
    x = Conv2D(64, (3, 3), activation='relu', padding='same', name='Conv1_2')(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='pool1')(x)

    x = Conv2D(128, (3, 3), activation='relu', padding='same', name='Conv2_1')(x)
    x = Conv2D(128, (3, 3), activation='relu', padding='same', name='Conv2_2')(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='pool2')(x)

    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='Conv3_1')(x)
    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='Conv3_2')(x)
    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='Conv3_3')(x)
    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='Conv3_4')(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='pool3')(x)

    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv4_1')(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv4_2')(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv4_3')(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv4_4')(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='pool4')(x)

    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv5_1')(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv5_2')(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv5_3')(x)
    x = Conv2D(512, (3, 3), activation='relu', padding='same', name='Conv5_4')(x)
    x = MaxPooling2D((2, 2), strides=(2, 2), name='pool5')(x)

    x = Flatten(name='flatten')(x)
    # x = Dense(4096, activation='relu', name='fc1')(x)
    # x = Dense(4096, activation='relu', name='fc2')(x)
    # 4096: OOM
    # 4: loss, acc, val_loss, val_acc fixed
    y = Dense(2, activation='softmax', name='predictions')(x)
    model = Model(inputs=i, outputs=y, name='vgg19')
    return model


model = vgg19()
model.summary()
model.compile(loss='binary_crossentropy', metrics=['accuracy'], optimizer=Adam(lr=0.0001, decay=1e-5))
fit = model.fit(x=train_image, y=train_label, epochs=100, batch_size=10, validation_data=(test_image, test_label), verbose=2)
eva = model.evaluate(x=val_image, y=val_label, batch_size=val_image.shape[0])


def plot_loss(history):
    plt.clf()
    plt_loss = plt
    plt_loss.plot(history.history['loss'])
    plt_loss.plot(history.history['val_loss'])
    plt_loss.title('Model Loss')
    plt_loss.xlabel('Epoch')
    plt_loss.ylabel('Loss')
    plt_loss.legend(['Train', 'Test'], loc=0)
    figure = 'D:/Dataset/KAGGLE/XRAY/OUTPUT/' + str(modelname) + '/loss.png'
    plt_loss.savefig(figure, dpi=1080)


def plot_acc(history):
    plt.clf()
    plt_acc = plt
    plt_acc.plot(history.history['acc'])
    plt_acc.plot(history.history['val_acc'])
    plt_acc.title('Model Accuracy')
    plt_acc.xlabel('Epoch')
    plt_acc.ylabel('Accuracy')
    plt_acc.legend(['Train', 'Test'], loc=0)
    figure = 'D:/Dataset/KAGGLE/XRAY/OUTPUT/' + str(modelname) + '/accuracy.png'
    plt_acc.savefig(figure, dpi=1080)


def csv_fit(fit):
    train_result_label = ['loss', 'acc', 'val_loss', 'val_acc']
    loss = fit.history['loss']
    acc = fit.history['acc']
    val_loss = fit.history['val_loss']
    val_acc = fit.history['val_acc']
    train_result = []
    train_result.append(loss)
    train_result.append(acc)
    train_result.append(val_acc)
    train_result.append(val_loss)
    train_result = np.array(train_result)
    train_result = train_result.reshape(train_result.shape[1], train_result.shape[0])
    train_result_file = pd.DataFrame(train_result)
    train_result_file.to_csv('D:/Dataset/KAGGLE/XRAY/OUTPUT/' + str(modelname) + '/csv_fit.csv', header=train_result_label, index=False)


def csv_eva(eva):
    test_result_label = ['test_loss, test_acc']
    test_loss = eva[0]
    test_acc = eva[1]
    test_result = []
    test_result.append(test_loss)
    test_result.append(test_acc)
    test_result = np.array(test_result)
    test_result_file = pd.DataFrame(test_result)
    test_result_file.to_csv('D:/Dataset/KAGGLE/XRAY/OUTPUT/' + str(modelname) + '/csv_eva.csv', header=test_result_label, index=False)


if os.path.isdir('D:/Dataset/KAGGLE/XRAY/OUTPUT/' + str(modelname)):
    pass
else:
    os.mkdir('D:/Dataset/KAGGLE/XRAY/OUTPUT/' + str(modelname))

print('Model', modelname, 'Loss: ', eva[0], ', Accuracy: ', eva[1])
plot_acc(fit)
plot_loss(fit)
csv_fit(fit)
csv_eva(eva)
model.save('D:/Dataset/KAGGLE/XRAY/OUTPUT/' + str(modelname) + '/model.h5')
model.save_weights('D:/Dataset/KAGGLE/XRAY/OUTPUT/' + str(modelname) + '/weights.h5')
print('Done!')

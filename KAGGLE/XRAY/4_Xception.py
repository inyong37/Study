# -*- coding:utf-8 -*-
# Author : Inyong Hwang
# 4. Xception

import numpy as np
import pickle
from keras.models import Model
from keras import layers
from keras.layers import Input, Conv2D, MaxPooling2D, Dense, BatchNormalization, Activation, SeparableConv2D, GlobalAveragePooling2D
from keras.optimizers import Adam
import matplotlib.pyplot as plt
import pandas as pd
import os

modelname = 'xception'

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


def xception(classes=2):
    i = Input(shape=train_image.shape[1:], name='Input_Image')

    x = Conv2D(32, (3, 3), strides=(2, 2), use_bias=False, name='block1_conv1')(i)
    x = BatchNormalization(name='block1_conv1_bn')(x)
    x = Activation('relu', name='block1_conv1_act')(x)
    x = Conv2D(64, (3, 3), use_bias=False, name='block1_conv2')(x)
    x = BatchNormalization(name='block1_conv2_bn')(x)
    x = Activation('relu', name='block1_conv2_act')(x)

    residual = Conv2D(128, (1, 1), strides=(2, 2), padding='same', use_bias=False)(x)
    residual = BatchNormalization()(residual)

    x = SeparableConv2D(128, (3, 3), padding='same', use_bias=False, name='block2_sepconv1')(x)
    x = BatchNormalization(name='block2_sepconv1_bn')(x)
    x = Activation('relu', name='block2_sepconv2_act')(x)
    x = SeparableConv2D(128, (3, 3), padding='same', use_bias=False, name='block2_sepconv2')(x)
    x = BatchNormalization(name='block2_sepconv2_bn')(x)

    x = MaxPooling2D((3, 3), strides=(2, 2), padding='same', name='block2_pool')(x)
    x = layers.add([x, residual])

    residual = Conv2D(256, (1, 1), strides=(2, 2), padding='same', use_bias=False)(x)
    residual = BatchNormalization()(residual)

    x = Activation('relu', name='block3_sepconv1_act')(x)
    x = SeparableConv2D(256, (3, 3), padding='same', use_bias=False, name='block3_sepconv1')(x)
    x = BatchNormalization(name='block3_sepconv1_bn')(x)
    x = Activation('relu', name='block3_sepconv2_act')(x)
    x = SeparableConv2D(256, (3, 3), padding='same', use_bias=False, name='block3_sepconv2')(x)
    x = BatchNormalization(name='block3_sepconv2_bn')(x)

    x = MaxPooling2D((3, 3), strides=(2, 2), padding='same', name='block3_pool')(x)
    x = layers.add([x, residual])

    residual = Conv2D(728, (1, 1), strides=(2, 2), padding='same', use_bias=False)(x)
    residual = BatchNormalization()(residual)

    x = Activation('relu', name='block4_sepconv1_act')(x)
    x = SeparableConv2D(728, (3, 3), padding='same', use_bias=False, name='block4_sepconv1')(x)
    x = BatchNormalization(name='block4_sepconv1_bn')(x)
    x = Activation('relu', name='block4_sepconv2_act')(x)
    x = SeparableConv2D(728, (3, 3), padding='same', use_bias=False, name='block4_sepconv2')(x)
    x = BatchNormalization(name='block4_sepconv2_bn')(x)

    x = MaxPooling2D((3, 3), strides=(2, 2), padding='same', name='block4_pool')(x)
    x = layers.add([x, residual])

    for j in range(8):
        residual = x
        prefix = 'block' + str(j + 5)

        x = Activation('relu', name=prefix + '_sepconv1_act')(x)
        x = SeparableConv2D(728, (3, 3), padding='same', use_bias=False, name=prefix + '_sepconv1')(x)
        x = BatchNormalization(name=prefix + '_sepconv1_bn')(x)
        x = Activation('relu', name=prefix + '_sepconv2_act')(x)
        x = SeparableConv2D(728, (3, 3), padding='same', use_bias=False, name=prefix + '_sepconv2')(x)
        x = BatchNormalization(name=prefix + '_sepconv2_bn')(x)
        x = Activation('relu', name=prefix + '_sepconv3_act')(x)
        x = SeparableConv2D(728, (3, 3), padding='same', use_bias=False, name=prefix + '_sepconv3')(x)
        x = BatchNormalization(name=prefix + '_sepconv3_bn')(x)

        x = layers.add([x, residual])

    residual = Conv2D(1024, (1, 1), strides=(2, 2), padding='same', use_bias=False)(x)
    residual = BatchNormalization()(residual)

    x = Activation('relu', name='block13_sepconv1_act')(x)
    x = SeparableConv2D(728, (3, 3), padding='same', use_bias=False, name='block13_sepconv1')(x)
    x = BatchNormalization(name='block13_sepconv1_bn')(x)
    x = Activation('relu', name='block13_sepconv2_act')(x)
    x = SeparableConv2D(1024, (3, 3), padding='same', use_bias=False, name='block13_sepconv2')(x)
    x = BatchNormalization(name='block13_sepconv2_bn')(x)

    x = MaxPooling2D((3, 3), strides=(2, 2), padding='same', name='block13_pool')(x)
    x = layers.add([x, residual])

    x = SeparableConv2D(1536, (3, 3), padding='same', use_bias=False, name='block14_sepconv1')(x)
    x = BatchNormalization(name='block14_sepconv1_bn')(x)
    x = Activation('relu', name='block14_sepconv1_act')(x)

    x = SeparableConv2D(2048, (3, 3), padding='same', use_bias=False, name='block14_sepconv2')(x)
    x = BatchNormalization(name='block14_sepconv2_bn')(x)
    x = Activation('relu', name='block14_sepconv2_act')(x)

    x = GlobalAveragePooling2D(name='avg_pool')(x)
    y = Dense(classes, activation='softmax', name='predictions')(x)
    model = Model(inputs=i, outputs=y, name='xception')
    return model


model = xception()
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

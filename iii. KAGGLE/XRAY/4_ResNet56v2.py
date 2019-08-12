# -*- coding:utf-8 -*-
# Author : Inyong Hwang
# 4. ResNet 56 v2

import numpy as np
import pickle
from keras.models import Model
from keras import layers
from keras.layers import Input, Conv2D, Dense, BatchNormalization, Activation, AveragePooling2D, Flatten
from keras.optimizers import Adam
from keras.regularizers import l2
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, ReduceLROnPlateau
import matplotlib.pyplot as plt
import pandas as pd
import os

modelname = 'resnet56v2'

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

# Define Model
version = 2
n = 6
depth = n * 9 + 2
model_type = 'ResNet%dv%d' % (depth, version)


def lr_schedule(epoch):
    lr = 1e-3
    if epoch > 180:
        lr *= 0.5e-3
    elif epoch > 160:
        lr *= 1e-3
    elif epoch > 120:
        lr *= 1e-2
    elif epoch > 80:
        lr *= 1e-1
    print('Learning rate: ', lr)
    return lr


def resnet_layer(inputs,
                 filters=16,
                 kernel_size=3,
                 strides=1,
                 activation='relu',
                 batch_normalization=True,
                 conv_first=True):
    conv = Conv2D(filters=filters,
                  kernel_size=kernel_size,
                  strides=strides,
                  padding='same',
                  kernel_initializer='he_normal',
                  kernel_regularizer=l2(1e-4))
    x = inputs
    if conv_first:
        x = conv(x)
        if batch_normalization:
            x = BatchNormalization()(x)
        if activation is not None:
            x = Activation(activation)(x)
    else:
        if batch_normalization:
            x = BatchNormalization()(x)
        if activation is not None:
            x = Activation(activation)(x)
        x = conv(x)
    return x


def resnet_v2(classes=2, depth=depth):
    filters_in = 16
    resnet_blocks = int((depth - 2) / 9)

    i = Input(shape=train_image.shape[1:], name='Input_Image')
    x = resnet_layer(inputs=i, filters=filters_in, conv_first=True)
    for stage in range(3):
        for resnet_block in range(resnet_blocks):
            activation = 'relu'
            batch_normalization = True
            strides = 1
            if stage == 0:
                filters_out = filters_in * 4
                if resnet_block == 0:
                    activation = None
                    batch_normalization = False
            else:
                filters_out = filters_in * 2
                if resnet_block == 0:
                    strides = 2
            y = resnet_layer(inputs=x, filters=filters_in, kernel_size=1, strides=strides, activation=activation, batch_normalization=batch_normalization, conv_first=False)
            y = resnet_layer(inputs=y, filters=filters_in, conv_first=False)
            y = resnet_layer(inputs=y, filters=filters_out, kernel_size=1, conv_first=False)
            if resnet_block == 0:
                x = resnet_layer(inputs=x, filters=filters_out, kernel_size=1, strides=strides, activation=None, batch_normalization=False)
            x = layers.add([x, y])
        filters_in = filters_out

    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = AveragePooling2D(pool_size=8)(x)
    x = Flatten()(x)
    y = Dense(classes, activation='softmax', kernel_initializer='he_normal')(x)
    model = Model(inputs=i, outputs=y)
    return model


model = resnet_v2()
model.summary()
model.compile(loss='binary_crossentropy', metrics=['accuracy'], optimizer=Adam(lr=lr_schedule(0)))
print(model_type)

if os.path.isdir('D:/Dataset/KAGGLE/XRAY/OUTPUT/' + str(modelname)):
    pass
else:
    os.mkdir('D:/Dataset/KAGGLE/XRAY/OUTPUT/' + str(modelname))

checkpoint = ModelCheckpoint(filepath='D:/Dataset/KAGGLE/XRAY/OUTPUT/' + str(modelname) + '/checkpoint.{epoch:03d}.hg',
                             monitor='val_acc',
                             verbose=0,
                             save_best_only=True)
lr_scheduler = LearningRateScheduler(lr_schedule)
lr_reducer = ReduceLROnPlateau(factor=np.sqrt(0.1),
                               cooldown=0,
                               patience=5,
                               min_lr=0.5e-6)
callbacks = [checkpoint, lr_reducer, lr_scheduler]
fit = model.fit(x=train_image, y=train_label, epochs=200, batch_size=20, validation_data=(test_image, test_label), verbose=2, callbacks=callbacks)
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


print('Model', modelname, 'Loss: ', eva[0], ', Accuracy: ', eva[1])
plot_acc(fit)
plot_loss(fit)
csv_fit(fit)
csv_eva(eva)
model.save('D:/Dataset/KAGGLE/XRAY/OUTPUT/' + str(modelname) + '/model.h5')
model.save_weights('D:/Dataset/KAGGLE/XRAY/OUTPUT/' + str(modelname) + '/weights.h5')
print('Done!')

# -*- coding: utf-8 -*-
# Modified Author : Inyong Hwang (inyong1020@gmail.com)
# Date            : 2020-07-08-Wed
# Title           : 코딩셰프의 분 딥러닝, 케라스맛 Chapter 9. 케라스 응용
# Environment     : TensorFlow (1.12.0) Keras (2.2.4) PyTorch (1.1.0) OpenCV (3.4.5)
# tensorflow.python.framework.errors_impl.InternalError: Blas GEMM launch failed : a.shape=(100, 784), b.shape=(784, 100), m=100, n=100, k=784
# 	 [[node dense_1/MatMul (defined at C:\Users\terry\Anaconda3\envs\tensorflow\lib\site-packages\keras\backend\tensorflow_backend.py:1085)  = MatMul[T=DT_FLOAT, transpose_a=false, transpose_b=false, _device="/job:localhost/replica:0/task:0/device:GPU:0"](_arg_Placeholder_0_0/_3, dense_1/kernel/read)]]
# Reference       : https://bryan7.tistory.com/992
# Reference       : ithttp://blog.naver.com/PostView.nhn?blogId=kenshin511&logNo=221013877842&parentCategoryNo=&categoryNo=25&viewDate=&isShowPopularPosts=true&from=search
import tensorflow as tf
from keras import backend as K
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout
from keras.metrics import categorical_accuracy, categorical_crossentropy
import numpy as np
from keras import datasets
from keras.utils import np_utils
import matplotlib.pyplot as plt
import inspect


filename = inspect.getfile(inspect.currentframe())
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
K.set_session(sess)


def plot_loss(history):
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc=0)
    plt.savefig(filename.replace('.py', '') + '_loss.png', dpi=300)


def plot_acc(history):
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc=0)
    plt.savefig(filename.replace('.py', '') + '_acc.png', dpi=300)


class DNN():
    def __init__(self, Nin, Nh_l, Nout):
        self.X_ph = tf.placeholder(tf.float32, shape=(None, Nin))
        self.L_ph = tf.placeholder(tf.float32, shape=(None, Nout))

        H = Dense(Nh_l[0], activation='relu')(self.X_ph)
        H = Dropout(0.5)(H)
        H = Dense(Nh_l[1], activation='relu')(H)
        H = Dropout(0.25)(H)
        self.Y_tf = Dense(Nout, activation='softmax')(H)

        self.Loss_tf = tf.reduce_mean(
            categorical_crossentropy(self.L_ph, self.Y_tf))
        self.Train_tf = tf.train.AdamOptimizer().minimize(self.Loss_tf)
        self.Acc_tf = categorical_accuracy(self.L_ph, self.Y_tf)
        self.Init_tf = tf.global_variables_initializer()


def Data_func():
    (X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()

    Y_train = np_utils.to_categorical(y_train)
    Y_test = np_utils.to_categorical(y_test)

    L, W, H = X_train.shape
    X_train = X_train.reshape(-1, W * H)
    X_test = X_test.reshape(-1, W * H)

    X_train = X_train / 255.0
    X_test = X_test / 255.0

    return (X_train, Y_train), (X_test, Y_test)


def run(model, data, sess, epochs, batch_size=100):
    (X_train, Y_train), (X_test, Y_test) = data
    sess.run(model.Init_tf)
    with sess.as_default():
        N_tr = X_train.shape[0]
        for epoch in range(epochs):
            for b in range(N_tr // batch_size):
                X_tr_b = X_train[batch_size * (b - 1):batch_size * b]
                Y_tr_b = Y_train[batch_size * (b - 1):batch_size * b]

                model.Train_tf.run(feed_dict={model.X_ph: X_tr_b, model.L_ph: Y_tr_b, K.learning_phase(): 1})
            loss = sess.run(model.Loss_tf, feed_dict={model.X_ph: X_test, model.L_ph: Y_test, K.learning_phase(): 0})
            acc = model.Acc_tf.eval(feed_dict={model.X_ph: X_test, model.L_ph: Y_test, K.learning_phase(): 0})
            print("Epoch {0}: loss = {1:.3f}, acc = {2:.3f}".format(epoch, loss, np.mean(acc)))


def main():
    Nin = 784
    Nh_l = [100, 50]
    number_of_class = 10
    Nout = number_of_class

    data = Data_func()
    model = DNN(Nin, Nh_l, Nout)

    run(model, data, sess, 10, 100)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
# Modified Author : Inyong Hwang (inyong1020@gmail.com)
# Date            : 2020-07-08-Wed
# Title           : 코딩셰프의 분 딥러닝, 케라스맛 Chapter 9. 케라스 응용
# Environment     : TensorFlow (1.12.0) Keras (2.2.4) PyTorch (1.1.0) OpenCV (3.4.5)
# Error           : tensorflow.python.framework.errors_impl.InternalError: Blas GEMV launch failed:
# Reference       : https://blog.naver.com/vft1500/221793591386
import keras
from keras import backend as K
from keras.engine.topology import Layer
import numpy as np
from keras import initializers
import tensorflow as tf


gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

igu = initializers.get('glorot_uniform')
iz = initializers.get('zeros')


class SFC(Layer):
    def __init__(self, No, **kwargs):
        self.No = No
        super().__init__(**kwargs)

    def build(self, inshape):
        self.w = self.add_weight("w", (inshape[1], self.No), initializer=igu)
        self.b = self.add_weight("b", (self.No,), initializer=iz)
        super().build(inshape)

    def call(self, x):
        return K.dot(x, self.w) + self.b

    def compute_output_shape(self, inshape):
        return inshape[0], self.No


def main():
    x = np.array([0, 1, 2, 3, 4])
    y = x * 2 + 1

    model = keras.models.Sequential()
    model.add(SFC(1, input_shape=(1,)))
    model.compile('SGD', 'mse')

    model.fit(x[:2], y[:2], epochs=1000, verbose=0)
    print('Targets:',y[2:])
    print('Predictions:', model.predict(x[2:]).flatten())


if __name__ == '__main__':
    main()

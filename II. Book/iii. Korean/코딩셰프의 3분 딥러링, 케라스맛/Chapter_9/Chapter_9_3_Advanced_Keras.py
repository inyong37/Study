# -*- coding: utf-8 -*-
# Modified Author : Inyong Hwang (inyong1020@gmail.com)
# Date            : 2020-07-08-Wed
# Title           : 코딩셰프의 분 딥러닝, 케라스맛 Chapter 9. 케라스 응용
# Environment     : TensorFlow (1.12.0) Keras (2.2.4) PyTorch (1.1.0) OpenCV (3.4.5)
# ValueError: Error when checking model input: the list of Numpy arrays that you are passing to your model is not the size the model expected. Expected to see 1 array(s), but instead got the following list of 2 arrays

def Lambda_with_lambda():
    from keras.layers import Lambda, Input
    from keras.models import Model

    x = Input((1,))
    y = Lambda(lambda x: x + 1)(x)
    m = Model(x, y)

    yp = m.predict_on_batch([1, 2, 3])
    print('np.array([1, 2, 3]) + 1:')
    print(yp)


def Lambda_function():
    from keras.layers import Lambda, Input
    from keras.models import Model

    def kproc(x):
        return x ** 2 + 2 * x + 1

    def kshape(input_shape):
        return input_shape

    x = Input((1,))
    y = Lambda(kproc, kshape)(x)
    m = Model(x, y)

    yp = m.predict_on_batch([1, 2, 3])
    print('np.array([1, 2, 3] + 1:')
    print(yp)


def Backend_for_Lambda():
    from keras.layers import Lambda, Input
    from keras.models import Model
    from keras import backend as K

    def kproc_concat(x):
        m = K.mean(x, axis=1, keepdims=True)
        d1 = K.abs(x - m)
        d2 = K.square(x - m)
        return K.concatenate([x, d1, d2], axis=1)

    def kshape_concat(input_shape):
        output_shape = list(input_shape)
        output_shape[1] *= 3
        return tuple(output_shape)

    x = Input((3,))
    y = Lambda(kproc_concat, kshape_concat)(x)
    m = Model(x, y)

    yp = m.predict_on_batch([[1, 2, 3], [3, 4, 8]])
    print(yp)


def TF_for_Lambda():
    from keras.layers import Lambda, Input
    from keras.models import Model
    import tensorflow as tf

    def kproc_concat(x):
        m = tf.reduce_mean(x, axis=1, keep_dims=True)
        d1 = tf.abs(x - m)
        d2 = tf.square(x - m)
        return tf.concat([x, d1, d2], axis=1)

    def kshape_concat(input_shape):
        output_shape = list(input_shape)
        output_shape[1] *= 3
        return tuple(output_shape)

    x = Input((3,))
    y = Lambda(kproc_concat, kshape_concat)(x)
    m = Model(x, y)

    yp = m.predict_on_batch(([1, 2, 3], [3, 4, 8]))
    print(yp)


def main():
    print('Lambda with lambda')
    Lambda_with_lambda()

    print('Lambda function')
    Lambda_function()

    print('Backend for Lambda')
    Backend_for_Lambda()

    print('TF for Lambd')
    TF_for_Lambda()


if __name__ == '__main__':
    main()

# 02 텐서플로 기초와 모델 훈련

```Python
import tensorflow as tf

num_classes = 10
img_rows, img_cols = 28, 28
num_channels = 1
input_shaep = (img_rows, img_cols, num_channels)

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(num_classes, activation='softmax'))

model.summary()

model.compile(optimize='sgd',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']

model.fit(x_train, y_train, epochs=5, verbose=1, validation_data=(x_test, y_test))
```

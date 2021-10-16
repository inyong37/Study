# 02 텐서플로 기초와 모델 훈련

## 기술적 요구사항

## 텐서플로 2와 케라스 시작하기

### 텐서플로 소개

### 케라스를 사용한 간단한 컴퓨터 비전 모델
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

## 텐서플로 2와 케라스 자세히 알아보기 :star:

### 핵심개념

- 텐서 소개

- 텐서플로 그래프

- 느긋한 실행과 조급한 실행 비교

- 텐서플로 2에서 그래프 생성하기

- 텐서플로 오토그래프와 tf.function 소개
```Python
@tf.function
def compute(a, b, c):
    d = a * b + c
    e = a * b * c
    return d, e
```

- 그래디언트 테이프를 사용해 오차 역전파하기

### 고급 개념

## 텐서플로 생태계

### 텐서보드

### 텐서플로 애드온과 텐서플로 확장

### 텐서플로 라이트와 TensorFlow.js

### 모델 실행 장소

## 요약
- 케라스 API를 사용해 기초적인 컴퓨터 비전 모델을 훈련시키는 방법
- 텐서플로2의 기초가 되는 주요 개념인 텐서, 그래프, 오토그래프, 조급한 실행, 그래디언트 테이프 소개
- 모니터링을 위한 텐서보드, 데이터 전처리와 모델 분석을 위한 TFX
- 필요에 따라 이 모델을 어디에서 실행하는 것이 좋은지에 대한 검토

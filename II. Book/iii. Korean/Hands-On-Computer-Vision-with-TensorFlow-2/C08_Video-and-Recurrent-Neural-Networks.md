# Chapter 8. 동영상과 순환 신경망

지금까지 이 책에서는 스틸 이미지만 고려했다. 이 장에서는 동영상 분석에 적용되는 기법을 소개한다. 자율 주행 자동차부터 동영상 스트리밍 웹사이트에 이르기까지 컴퓨터 비전 기술은 이미지 시퀀스를 처리할 수 있게 개발됐다.

동영상 같은 순차적 입력을 위해 특별히 설계된 새로운 유형의 신경망인 순환 신경망(recurrent neural network, RNN)을 소개한다. 실용적인 애플리케이션으로 동영상 클립에 포함된 동작을 감지하기 위해 RNN을 합성곱 신경망(convolutional neural network, CNN)과 결합할 것이다.

- RNN 소개
- 장단기 메모리 네트워크의 내부 동작
- 컴퓨터 비전 모델을 동영상에 적용

## 8.1. 기술 요구사항

## 8.2. RNN 소개

RNN은 '순차적'(또는 '순환적') 데이터에 적합한 유형의 신경망이다. 순차적 데이터의 예에는 문장(단어 시퀀스), 시계열(예: 주가 시퀀스), 동영상(프레임 시퀀스)가 포함된다. 각 시간 단계가 '이전 단계와 관련되기' 때문에 순환 데이터로 볼 수 있다.

RNN은 원래 시계열 분석과 자연어 처리 작업을 위해 개발됐지만 지금은 다양한 컴퓨터 비전 작업에 적용된다.

### 8.2.1. 기본 형식

동영상은 N개의 프레임으로 구성된다. 동영상을 분류하는 가장 원초적인 방법은 각 프레임에 CNN을 적용한 다음 그 출력의 평균을 구하는 것이다.

이 원초적인 방식은 적절한 결과를 제공하지만, 동영상의 일부가 다른 부분보다 더 중요하다는 사실을 반영하지는 않는다. 또한 중요한 부분이 의미 없는 부분보다 항상 더 많은 프레임을 차지하지는 않는다. 따라서 출력의 평균을 구하면 중요한 정보를 잃어버릴 위험이 있다.

이 문제를 피하기 위해 RNN은 동영상의 모든 프레임에 첫 번째부터 마지막 프레임까지 차례대로 적용된다. RNN의 주요 특성은 의미 있는 결과를 생성하기 위해 모든 프레임에서 얻은 특징을 적절하게 결합한다는 데 있다.

:bulb: 여기서는 RNN을 프레임의 원시 픽셀에 직접 적용하지 않는다. 먼저 CNN을 사용해 특징 볼륨(특징 맵의 스택)을 생성한다. 특징 볼륨은 CNN의 출력으로 일반적으로 더 작은 차원으로 입력을 나타낸다.

그러기 위해 RNN은 상태(state)라는 새로운 개념을 도입한다. '상태'는 RNN의 메모리로 볼 수 있다. 실제로 '상태'는 부동소수점 행렬이다. 상태는 영행렬(zero matrix)로 시작해 동영상의 각 프레임을 사용해 업데이트된다. 프로세스가 끝나면 최종 상태는 RNN의 출력을 생성하는 데 사용된다. 실제로 '상태'는 부동소수점 행렬이다. 상태는 영행렬(zero matrix)로 시작해 동영상의 각 프레임을 사용해 업데이트된다. 프로세스가 끝나면 최종 상태는 RNN의 출력을 생성하는 데 사용된다.

RNN의 주요 구성요소는 RNN 셀(RNN cell)로, 모든 프레임에 적용된다. 셀은 '현재 프레임'과 '이전 상태'를 모두 입력으로 받는다.

널 상태(h^0)로 시작된다. 첫 번째 단계에서 셀은 현재 상태(h^0)를 현재 프레임(frame_1)과 결합해 새로운 상태(h^1)을 생성한다. 그런 다음 동일한 프로세스를 다음 프레임에 적용한다. 이 프로세스가 끝나면 최종 상태(h^n)이 된다.

:bulb: 'RNN'은 이미지를 받아들이고 최종 출력을 반환하는 구성 요소를 나타낸다. 'RNN 셀'은 프레임과 현재 상태를 결합해서 다음 상태를 반환하는 하위 구성요소를 나타낸다.

실제로 셀은 현재 상태와 프레임을 결합해 새로운 상태를 생성한다. 현재 상태와 프레임은 다음 공식에 따라 결합한다.

h^t = tanh(W_rec(h^(t-1)) + W_input(x^t) + b)

- b는 편향값이다.
- W_rec은 순환 가중치 행렬이고 W_input은 가중치 행렬이다.
- x^t는 입력이다.
- h^(t-1)은 현재 상태이고 h^t는 새로운 상태다.

은닉 상태(hidden state)는 그대로 사용되지 않는다. 가중치 행렬 V가 최종 예측을 계산하는 데 사용된다.

y_hat^t = softmax(V * h^t)

:bulb: 시간 정보를 표시하기 위해 `<>`를 사용한다. 햇 표시가 있는 `y_hat`는 일반적으로 신경망의 예측을 나타내고 `y`는 실제 정보를 나타낸다.

RNN을 동영상에 적용하면 전체 동영상 또는 모든 단일 프레임을 분류할 수 있다. 예를 들어, 전자의 경우 동영상이 폭력적인지 아닌지를 예측할 때 최종 예측, `y_hat^t`만 사용된다. 후자의 경우 어떤 프레임에 누드가 포함돼 있는지 탐지하려면 각 시간 단계에 대한 예측을 사용할 것이다.

### 8.2.2. RNN에 대한 일반적인 이해

### 8.2.3. RNN 가중치 학습

### 8.2.4. 장단기 메모리 셀

## 8.3. 동영상 분류

:bulb: 파이썬 제너레이터와 마찬가지로 return 키워드를 사용하는 대신 yield 키워드를 사용한다. 이를 통해 루프가 끝나기 전에 프레임을 반환할 수 있다. 이런 방식으로 네트워크는 모든 프레임이 사전처리 되는 것을 기다리지 않고도 훈련을 시작할 수 있다.

### 8.3.1. 컴퓨터 비전을 동영상에 적용하기

### 8.3.2. LSTM으로 동영상 분류하기

## 8.4. 요약

## 8.5. 질문

## 8.6. 참고 문헌

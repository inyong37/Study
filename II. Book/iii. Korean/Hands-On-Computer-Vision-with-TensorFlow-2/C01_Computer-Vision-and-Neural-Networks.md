# Chapter 1. 컴퓨터 비전과 신경망

## 1.1. 기술적 요구사항

## 1.2 컴퓨터 비전

### 1.2.1. 컴퓨터 비전 소개

### 1.2.2. 주요 작업 및 애플리케이션

## 1.3. 컴퓨터 비전의 약력

### 1.3.1. 최초 성공을 위한 첫 걸음

### 1.3.2. 딥러닝의 출현

## 1.4. 신경망 시작하기

### 1.4.1. 신경망 구성하기

### Activation Functions

입력 크기가 바뀌고 더해져서 결과를 만들면, 뉴런의 츨력을 얻기 위해 그 결과에 활성화 함수를 적용해야 한다.

Step Function:
- 퍼셉트론에서 사용하는 y가 임계값 t보다 크면 전기 자극을 반환하고 그렇지 않으면 0을 반환하는 이진 함수다.
- y = f(z) = 0 if z < t or 1 if z >= t
- 비선형성과 연속형 식별 가능성 같이 더 유리한 특성을 갖춘 발전된 활성화 함수가 소개됐다.

Sigmoid function:
- s(z) = 1/(1 + exp(-z))

Hyperbolic tangent:
- tanh(z) = (exp(z) - exp(-z)) / (exp(z) + exp(-z))

Rectified Linear Unit (ReLU):
-  ReLU(z) = max(0, z) = 0 if z < 0 or z if z >= 0

인공 뉴런은 신호를 받아 처리해서 다른 뉴런에 '전달(forward)'될 값을 출력으로 만들어서 네트워크를 구성할 수 있다.

:bulb: 비선형 활성화 함수를 사용하지 않고 뉴런을 연결하는 것은 단일 뉴런을 갖는 것과 마찬가지다. 따라서 복잡한 모델을 생성하려면 비선형 활성화 함수는 불가피하다.

```Python
import numpy as np

class Neuron(object):
  """간단한 전방 전달 인공 뉴런.
  Args:
    num_inputs (int): 입력 벡터 크기 / 입력 값 개수.
    activation_fn (callable): 활성화 함수.
  Attributes:
    W (ndarray): 각 입력에 대한 가중치.
    b (float): 편향값, 가중합에 더해짐
    activation_fn (callable): 활성화 함수.
  """
  
  def __init__(self, num_inputs, activation_fn):
    super().__init__()
    # 랜덤값으로 가중치 벡터와 편향값을 초기화함:
    self.W = np.random.rand(num_inputs)
    self.b = np.random.rand(1)
    self.activation_fn = activation_fn
    
  def forward(self, x):
    """뉴런을 통해 입력 신호를 전달."""
    z = np.dor(x, self.W) + self.b
    return self.activation_fn(z)
```

인스턴화해서 임의의 입력값을 이 퍼셉트론을 통해 전달하자.

```Bash
# 결과를 복제할 수 있도록 랜덤 숫자 생성기의 시드 값을 고정
np.random.seed(42)
# 3개의 랜덤 입력을 칼럼으로 받을 수 있는 배열 (shape = `(1, 3)`)
x = np.random.rand(3).reshape(1, 3)
# > [[0.37454012 0.95071431 0.73199394]]

# 퍼셉트론을 인스턴스화(계단 함수를 사용하는 간단한 뉴런):
step_fn = lambda y: 0 if y <= 0 else 1
perceptron = Neuron(num_inputs=x.size, activation_fn=step_fn)
# > perceptron.W = [0.59865848 0.15601864 0.15599452]
# > perceptron.b = [0.05808351]
out = perceptron.forward(x)
# > 1
```

일반적으로 신경망은 '계층', 즉 일반적으로 동일한 입력을 받고 동일한 연산을 적용하는 뉴런 집합으로 구성된다.

각 뉴런이 이전 계층에서 나온 모든 값에 연결돼 있는 계층을 완전 연결 계층(fully-connected layer) 또는 밀집 계층(dense layer)이라고 한다.

MNIST(Modified National Institute of Standards and Technology) 데이터셋이 수년간 이 인식 문제를 해결하는 기법을 테스트하기 위한 참고자료롤 사용됐다(얀 르쿤과 코리나 코르테스가 다음 이미지의 데이터셋에 대한 저작권을 보유하고 있다).

숫자를 분류하기 위해 필요한 작업은 이 이미지 중 하나를 입력으로 받아 '네트워크가 해당 이미지가 각 클래스에 대응하는지 확신하는 정도'를 출력 벡터로 반환하는 것이다. 여기서 우리가 할 일은 은닉 계층의 개수와 그 크기를 정의하는 것이다. 그런 다음 이미지의 클래스를 예측하기 위해 '이미지 벡터를 네트워크를 통해 전달하고, 출력을 수집해서 확신 점수가 가장 높은 클래스를 반환'하기만 하면 된다.

:bulb: 이 '확신' 점수(belief score)는 보통 추가 계산이나 해석을 단순화하기 위해 확률로 변환된다.

### 1.4.2. 신경망 훈련시키기

신경망은 가용 데이터로부터 학습해서 '훈련돼야'하는, 즉 신경망의 매개변수가 특정 과제에 맞게 최적화돼야 하는 특수한 알고리즘이다. 네트워크가 이 '훈련 데이터셋'에서 잘 동작하게 최적화되고 나면 비슷하지만 새로운 데이터에 사용돼 만족할 만한 수준의 결과를 제공할 수 있다.

지도 학습(Supervised Learning)

### 비지도 학습(Unsupervised Learning)

이 전략은 클러스터링(비슷한 속성을 갖는 이미지끼리 그룹으로 나누는)이나 압축(콘텐츠의 일부 속성은 유지하면서 크기를 줄이는) 같은 애플리케이션에 매우 적합하다. 클러스터링의 경우 손실 함수는 하나의 클러스터의 비슷한 이미지가 다른 클러스터의 이미지와 얼마나 다른지 측정할 수 있다. 압축의 경우 손실 함수는 원본 데이터와 비교해 압축된 데이터의 중요한 속성이 얼마나 잘 보존돼 있는지를 측정할 수 있다.

강화 학습(Reinforcement Learning)

## 1.5. 요약

1. 컴퓨터 비전, 그 도전 과제, SIFT, SVM 같은 역사적 기법을 소개
2. 신경망, 신경망을 구성하고 훈련시키고 적용하는 방법
3. MNIST 분류 네트워크 구현, 머신러닝 프레임워크 동작에 대한 이해

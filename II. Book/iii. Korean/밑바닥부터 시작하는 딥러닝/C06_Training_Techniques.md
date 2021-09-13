# Chapter 6 학습 관련 기술들

## 6.1 매개변수 갱신

### 6.1.1 모험가 이야기

### 6.1.2 확률적 경사 하강법(SGD)
W <- W - eta * dL/dW ... [eq. 6.1]

여기서 W는 갱신할 가중치 매개변수고 dL/dW은 W에 대한 손실 함수의 기울기이다. eta는 학습률을 의미하는데, 실제로는 0.01이나 0.001과 같은 값을 미리 정해서 사용한다. 또 <-는 우변의 값으로 좌변의 값을 갱신하다는 뜻이다. [eq. 6.1]에서 보듯 SGD는 기울어진 방향으로 일정 거리만 가겠다는 단순한 방법이다.

```Python
class SGD:
  def __init__(self, lr=0.01):
    self.lr = lr
  def update(self, params, grads):
    for key in params.keys():
      params[key] -= self.lr * grads[key]
```

초기화 때 받는 인수은 lr은 learning rate(학습률)를 뜻한다.

### 6.1.3 SGD의 단점

SGD의 단점은 비등방성(anisotropy) 함수(방향에 따라 성질, 기울기가 달라지는 함수)에서는 탐색 경로가 비효율적이라는 것이다.

### 6.1.4 모멘텀
모멘텀(Momentum)은 운동량을 뜻하는 단어로, 물리와 관계가 있다.

v <- alpha * v - eta * dL/dW ... [eq. 6.3]

W <- W + v ... [eq. 6.4]

여기에서도 W는 갱신할 가중치 매개변수, dL/dW은 에 대한 손실 함수의 기울기, eta는 학습률이다. v라는 변수가 새로 나오는데, 이는 물리에서 말하는 속도(velocity)에 해당한다. [eq. 6.3]은 기울기 방향으로 힘을 받아 물체가 가속된다는 물리 법칙을 나타낸다. 또 alpha * v 항은 물체가 아무런 힘을 받지 않을 때 서서히 하강시키는 역할을 한다. (alpha는 0.9 등의 값으로 설정한다.) 물리에서의 지면 마찰이나 공기 저항에 해당한다.

```Python
class Momentum:
  def __init__(self, lr=0.01, momentum=0.9):
    self.lr = lr
    self.momentum = momentum
    self.v = None
  def update(self, params, grads):
    if self.v is None:
      self.v = {}
      for key, val in params.items():
        self.v[key] = np.zeros_like(val)
    
    for key in params.key()
      self.v[key] = self.momentum * self.v[key] - self.lr * grads[key]
      params[key] += self.v[key]
```

인스턴스 변수 v가 물체의 속도이다. v는 초기화 때는 아무 값도 담지 않고, 대신 update()가 처음 호출될 때 매개변수와 같은 궂의 데이터를 딕셔너리 변수로 저장한다.

모멘텀의 갱신 경로는 공이 그릇 바닥을 구르듯 움직인다. SGD와 비교하면 지그재그 정도가 덜한 것을 알 수 있다. 이는 x축의 힘은 아주 작지만 방향은 변하지 않아서 한 방향으로 일정하게 가속하기 때문이다. 거꾸로 y축의 힘은 크지만 위아래로 번갈아 받아서 상충하여 y축 방향의 속도는 안정적이지 않는다. 전체적으로는 SGD보다 x축 방향으로 빠르게 다가가 지그재그 움직임이 줄어든다.

### 6.1.5 AdaGrad
신경망 학습에서는 학습률(eta) 값이 중요하다. 이 값이 너무 작으면 학습 시간이 너무 길어지고, 반대로 너무 크면 발산하여 학습이 제대로 이뤄지지 않는다.

이 학습률을 정하는 효과적 기술로 학습률 감소(learning rate decay)가 있다. 이는 학습을 진행하면서 학습률을 점차 줄여가는 방법이다. 처음에는 크게 학습하다가 조금씩 작게 학습한다는 얘기로, 실제 신경망 학습에 자주 쓰인다.

학습률을 서서히 낮추는 가장 간단한 방법은 매개변수 전체의 학습률 값을 일괄적으로 낮추는 것이다. 이를 더욱 발전시킨 것이 AdaGrad이다. AdaGrad는 각각의 매개변수에 맞춤형 값을 만들어준다.

AdaGrad는 개별 매개변수에 적응적으로(adaptive) 학습률을 조정하면서 학습을 진행한다. AdaGrad의 갱신 방법은 수식으로는 다음과 같다.

h <- h + dL/dW * dL/dW ... [eq. 6.5]

W <- W - eta * 1/(h^(1/2)) * dL/dW ... [eq. 6.6]

마찬가지로 W는 갱신할 가중치 매개변수, dL/dW은 W에 대한 손실 함수의 기울기, eta는 학습률을 뜻한다. 여기에서는 새로 h라는 변수가 등장한다. h는 [eq. 6.5]에서 보듯 기존 기울기 값을 제곱하여 계속 더해준다. 그리고 매개변수를 갱신할 때 1/(h*(1/2))을 곱해 학습률을 조정한다. 매개변수의 원소 중에서 많이 움직인(크게 갱신된) 원소는 학습률이 낮아진다는 뜻인데, 다시 말해 학습률 감소가 매개변수의 원소마다 다르게 적용됨을 뜻한다.

### Note
AdaGrad는 과거의 기울기를 제곱하여 계속 더해간다. 그래서 학습을 진행할수록 갱신 강도가 약해진다. 실제로 무한히 계속 학습한다면 어느 순간 갱신량이 0이 되어 전혀 갱신되지 않게 된다. 이 문제를 개선한 기법으로서 RMSProp이라는 방법이 있다. RMSProp은 과거의 모든 기울기를 균일하게 더해가는 것이 아니라, 먼 과거의 기울기는 서서히 잊고 새로운 기울기 정보를 크게 반영한다. 이를 지수이동평균(Exponential Moving Average, EMA)이라 하여, 과거 기울기의 반영 규모를 기하급수적으로 감소시킨다.

```Python
class AdaGrad:
  def __init__(self, lr=0.01):
    self.lr = lr
    self.h = None
  
  def update(self, params, grads):
    if self.h is None:
      self.h = {}
      for key, val in params.items():
        self.h[key] = np.zeros_like(val)
    for key in params.keys():
      self.h[key] += grads[key] * grads[key]
      params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7
```

여기에서 주의할 것은 마지막 줄에서 1e-7이라는 작은 값을 더하는 부분이다. 이 작은 값은 self.h[key]에 0이 담겨져 있다 해도 0으로 나누는 사태를 막아준다. 대부분의 딥러닝 프레임워크에서는 이 값도 인수로 설정할 수 있다.

### 6.1.6 Adam

## 6.2 가중치의 초깃값

## 6.3 배치 정규화

## 6.4 바른 학습을 위해

## 6.5 적절한 하이퍼파라미터 값 찾기

## 6.6 정리
- 매개변수 갱신 방법에는 확률적 경사 하강법(SGD) 외에도 모멘텀, AdaGrad, Adam 등이 있다.
- 가중치 초깃값을 정하는 방법은 올바른 학습을 하는 데 매우 중요하다.
- 가중치의 초깃값으로는 'Xavier 초깃값'과 'He 초깃값'이 효과적이다.
- 배치 정규화를 이용하면 학습을 빠르게 진행할 수 있으며, 초깃값에 영향을 덜 받게 된다.
- 오버피팅을 억제하는 정규화 기술로는 가중치 감소와 드롭아웃이 있다.
- 하이퍼파라미터 값 탐색은 최적 값이 존재할 법한 범위를 점차 좁히면서 하는 것이 효과적이다.

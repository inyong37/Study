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

# Chapter 4 신경망 학습

## 4.1 데이터에서 학습한다!

### 4.1.1 데이터 주도 학습
기계학습에서는 사람의 개입을 최소화하고 수집한 데이터로부터 패턴을 찾으려 시도한다. 신경망과 딥러닝은 기존 기계학습에서 사용하던 방법보다 사람의 개입을 더욱 배제할 수 있게 해주는 중요한 특성을 지녔다.

이미지에서 특징(feature)를 추출하고 그 특징의 패턴을 기계학습 기술로 학습하는 방법이 있다. 이미지의 특징으 보통 벡터로 기술하고, 컴퓨터 비전 분야에서는 SIFT, SURF, HOG 등의 특징을 많이 사용한다. 이런 특징을 사용하여 이미지 데이터를 벡터로 변환하고, 변환된 벡터를 가지고 지도 학습 방식의 배표 분류 기법인 SVM, KNN 등으로 학습할 수 있다.

이미지를 벡터로 변환할 때 사용하는 특징은 여전히 사람이 설계하는 것임에 주의해야 한다. 즉, 특징과 기계학습을 활용한 접근에도 문제에 따라서는 사람이 적절한 특징을 생각해내야 하는 것이다.

신경망은 이미지를 있는 그대로 학습한다. 신경망은 이미지에 포함된 중요한 특징까지도 기계가 스스로 학습한다.

### Note
딥러닝을 종단간 기계학습(end-to-end machine learning)이라고도 한다. 데이터(input)에서 목표한 결과(output)를 사람의 개입 없이 얻는다는 뜻을 담고 있다.

### 4.1.2 훈련 데이터와 시험 데이터

## 4.2 손실 함수

### 4.2.1 평균 제곱 오차
가장 많이 쓰이는 손실 함수는 평균 제곱 오차(mean squared error, MSE)이다.

E = 1/2 * sum((y[k]-t[k])**2) ... [eq. 4.1]

여기서 y는 신경망의 출력(신경망이 추정한 값), t는 정답 레이블, k는 데이터의 차원 수를 나타낸다.

```Python
def mean_squared_error(y, t):
  return 0.5 * np.sum((y-t)**2)
```

### 4.2.2 교차 엔트로피 오차
또 다른 손실 함수로서 교차 엔트로피 오차(cross entropy error, CEE)도 자주 이용한다.

E = -sum(t[k]*log(y[k])) ... [eq. 4.2]

여기에서 log는 밑이 e인 자연로그(loge)이다. y는 신경망의 출력, t는 정답 레이블이다. 또 t는 정답에 해당하는 인덱스의 원소만 1이고 나머지는 0이다(원-핫 인코딩). 그래서 [eq 4.2]는 정답일 때의 추정(t가 1일 때의 y)의 자연로그를 계산하는 식이된다. 즉, 교차 엔트로피 오차는 정답일 때의 출력이 전체 값을 정하게 된다.

```Python
def cross_entropy_error(y, t):
  return -np.sum(t * np.log(y + delta))
```

아주 작은 값을 더해서 절대 0이 되지 않도록, 즉 마이너스 무한대가 발생하지 않도록 한다.

### 4.2.3 미니배치 학습

E = -1/N * sum(sum(t[n][k]*log(y[n][k]))) ... [eq. 4.3]

데이터가 N개라면, t[n][k]는 n번째 데이터의 k번째 값을 의미한다. y[n][k]는 신경망의 출력, t[n][k]는 정답 레이블이다. 데이터 하나에 대한 손실 함수인 [eq. 4.2]를 단순히 N개의 데이터로 확장했을 뿐이다. 다만, 마지막에 N으로 나누어 정규화하고 있다. N으로 나눔으로써 평균 손실 함수를 구하는 것이다. 이렇게 평균을 구해 사용하면 훈련 데이터 개수와 관계없이 언제든 통일된 지표를 얻을 수 있다.

데이터 일부를 추려 전체의 근사치로 이용할 수 있다. 신경망 학습에서도 훈련 데이터로부터 일부만 골라 학습을 수행한다. 이 일부를 미니 배치(mini-batch)라 한다. 가령 60000장의 훈련 데이터 중에서 100장을 무작위로 뽑아 그 100장만을 사용하여 학습하는 것이다. 이러한 학습 방법을 미니배치 학습이라고 한다.

### 4.2.4 (배치용) 교차 엔트로피 오차 구현하기
```Python
def cross_entropy_error(y, k):
  if y.ndim == 1:
    t = t.reshape(1, t.size)
    y = y.reshape(1, y.size)
  batch_size = y.shape[0]
  return -np.sum(t * np.log(y)) / batch_size
```

y가 1차원이라면, 즉 데이터 하나당 교차 엔트로피 오차를 구하는 경우는 reshape 함수로 데이터의 형상을 바꿔준다. 그리고 배치의 크기로 나눠 정규화하고 이미지 1장당 평균의 교차 엔트로피 오차를 계산한다.

정답 레이블이 원-핫 인코딩이 아니라 2나 7 등의 숫자 레이블로 주어졌을 때의 교차 엔트로피 오차는 다음과 같이 구현한다.

```Python
def cross_entropy_error(y, t):
  if y.ndim == 1:
    t = t.reshape(1, t.size)
    y = y.reshape(1, y.size)
  batch_size = y.shape[0]
  return -np.sum(np.log(y[np.arange(batch_size), t])) / batch_size
```

이 구현에서는 원-핫 인코딩일 때 t가 0인 원소는 교차 엔트로피 오차도 0이므로, 그 계산은 무시해도 좋다는 것이 핵심이다. 그래서 원-핫 인코딩 시 t*np.log(y)였던 부분을 레이블 표현일 때는 np.log(y[np.arange(batch_size), t])로 구현한다.

### 4.2.5 왜 손실 함수를 설정하는가?
신경망을 학습할 때 정확도를 지표로 삼아서는 안 된다. 정확도를 지표로 하면 매개변수의 미분이 대부분의 장소에서 0이 되기 때문이다.

## 4.3 수치 미분
```Python
def numerical_diff(f, x):
  h = 1e-4
  return (f(x+h) - f(x-h)) / (2*h)
```

### Note
여기에서 하는 것처럼 아주 작은 차분(임의 두 점에서의 함수 값들의 차이)으로 미분하는 것을 수치 미분이라 한다. 수식을 전개해 미분하는 것은 해석적(analytic)이라는 말을 이용하여 해석적 해 혹은 해석적으로 미분하다는 등으로 표현한다. 수치 미분은 근사치로 계산하는 방법이다. 이들 용어 관련하여, 수치해석학은 해석학 문제에서 수치적인 근삿값을 구하는 알고리즘을 연구하는 학문이다.

## 4.4 기울기
모든 변수의 편미분을 벡터로 정리한 것을 기울기(gradient)라고 한다.
```Python
def numerical_gradient(f, x):
  h = 1e-4
  grad = np.zeros_like(x)
  for idx in range(x.size):
    tmp_val = x[idx]
    x[idx] = tmp_val + h
    fxh1 = f(x)
    
    x[idx] = tmp_val - h
    fxh2 = f(x)
    
    grad[idx] = (fxh1 - fxh2) / (2*h)
    x[idx] = tmp_val
  return grad
```

기울기는 각 지점에서 낮아지는 방향을 가리킨다. 기울기가 가리키는 쪽은 각 장소에서 함수의 출력 값을 가장 크게 줄이는 방향이다.

### 4.4.1 경사법(경사 하강법)
기울기를 잘 이용해 함수의 최솟값(도는 가능한 한 작은 값)을 찾으려는 것이 경사법이다.

### WARNING
함수가 극솟값, 최솟값, 또 안장점(saddle point)이 되는 장소에서는 기울기가 0이다. 경사법은 기울기가 0인 장소를 찾지만 그것이 반드시 최솟값이라고는 할 수 없다. 또, 복잡하고 찌그러진 모양의 함수라면 (대부분) 평평한 곳으로 파고들면서 고원(plateau)이라 하는, 학습이 진행되지 않는 정체기에 빠질 수 있다.

경사법은 현 위치에서 기울어진 방향으로 일정 거리만큼 이동한다. 그런 다음 이동한 곳에서도 마찬가지로 기울기를 구하고, 또 그 기울어진 방향으로 나아가기를 반복한다. 이렇게 해서 함수의 값을 점차 줄이는 것이 경사법(gradient method)이다. 경사법은 기계학습을 최적화하는 데 흔히 쓰는 방법이다. 특히 신경망 학습에는 경사법을 많이 사용한다.

### Note
경사법은 최솟값을 찾느냐, 최댓값을 찾느냐에 따라 이름이 다르다. 전자를 경사 하강법(gradient descent method) 후자를 경사 상승법(gradient ascent method)라 한다. 다만 손실 함수의 부호를 반전시키면 최솟값을 찾는 문제와 최댓값을 찾는 문제는 같은 것이니 하강이냐 상승이냐는 본질적으로 중요하지 않다. 일반적으로 신경망(딥러닝) 분야에서의 경사법은 경사 하강법으로 등장할 때가 많다.

x0 = x0 - eta*delta(f)/delta(x0)

x1 = x1 - eta*delta(f)/delta(x1) ... [eq. 4.7]

eta는 갱신하는 양을 나타낸다. 이를 신경망 학습에서는 학습률(learning rate)이라고 한다. 한 번의 학습으로 얼마만큼 학습해야 할지, 즉 매개변수 값을 얼마나 갱신하느냐를 정하는 것이 학습률이다.

[eq. 4.7]은 1회에 해당하는 갱신이고, 이 단계를 반복한다. 변수의 수가 늘어도 같은 식 (각 변수의 편미분 값)으로 갱신하게 된다.

또한 학습률 값은 0.01이나 0.001 등 미리 특정 값으로 정해두어야 하는데, 일반적으로 이 값이 너무 크거나 작으면 좋은 장소를 찾아갈 수 없다. 신경망 학습에서는 보통 이 학습률 값을 변경하면서 올바르게 학습하고 있는지를 확인하면서 진행한다.

```Python
def gradient_descent(f, init_x, lr=0.01, step_num=100):
  x = init_x
  for i in range(step_num):
    grad = numerical_gradient(f, x)
    x -= lr * grad
  return x
```

인수 f는 최적화하려는 함수, init_x는 초깃값, lr은 learning rate를 의마하는 학습률, step_num은 경사법에 따른 반복 횟수를 뜻한다. 함수의 기울기는 numerical_gradient(f, x)로 구하고, 그 기울기에 학습률을 곱한 값으로 갱신하는 처리를 step_num번 반복한다.

학습률이 너무 크면 큰 값으로 발산해버린다. 반대로 너무 작으면 거의 갱신되지 않은 채 끝나버린다.

### Note
학습률 같은 매개변수를 하이퍼파라미터(hyper parameter)라고 한다. 이는 가중치와 편향 같은 신경망의 매개변수와는 성질이 다른 매개변수이다. 신경망의 가중치 매개변수는 훈련 데이터와 학습 알고리즘에 의해서 자동으로 획득되는 매개변수인 반면, 학습률 같은 하이퍼파라미터는 사람이 직접 설정해야하는 매개변수인 것이다. 일반적으로는 이 하이퍼파라미터는 여러 후보 값 중에서 시험을 통해 가장 잘 학습하는 값을 찾는 과정을 거쳐야 한다.

### 4.4.2 신경망에서의 기울기
신경망 학습에서도 기울기를 구해야 한다. 여기서 말하는 기울기는 가중치 매개변수에 대한 손실 함수의 기울기이다. 

파이썬에서는 간단한 함수라면 람다(lambda) 기법을 쓰면 더 편하다. 가령 lambda를 쓰면 다음과 같이 구현할 수 있다.
```Python
f = lambda w: net.loss(x, t)
dW = numerical_gradient(f, net.W)
```

신경망의 기울기를 구한 다음에는 경사법에 따라 가중치 매개변수를 갱신하면 된다.

## 4.5 학습 알고리즘 구현하기
신경망 학습의 절차는 다음과 같다.
- 전제
  - 신경망에는 적응 가능한 가중치와 편향이 있고, 이 가중치와 편향을 훈련 데이터에 적응하도록 조정하는 과정을 학습이라 한다. 신경망 학습은 다음과 같이 4단계로 수행한다.
- 1단계 - 미니배치
  - 훈련 데이터 중 일부를 무작위로 가져온다. 이렇게 선별한 데이터를 미니배치라 하며, 그 미니배치의 손실 함수 값을 줄이는 것이 목표이다.
- 2단계 - 기울기 산출
  - 미니배치의 손실 함수 값을 줄이기 위해 각 가중치 매개변수의 기울기를 구한다. 기울기는 손실 함수의 값을 가장 작게 하는 방향을 제시한다.
- 3단계 - 매개변수 갱신
  - 가중치 매개변수를 기울기 방향으로 아주 조금 갱신한다.
- 4단계 - 반복
  - 1~3단계를 반복한다.

이것이 신경망 학습이 이뤄지는 순서이다. 이는 경사 하강법으로 매개변수를 갱신하는 방법이며, 이때 데이터를 미니배치로 무작위로 선정하기 때문에 확률적 경사 하강법(stochastic gradient descent, SGD)이라고 부른다. 확률적으로 무작위로 골라낸 데이터에 대해 수행하는 경사 하강법이라는 의미다. 대부분의 딥러닝 프레임워크는 확률적 경사 하강법의 영어 머리글자를 딴 SGD라는 함수로 이 기능을 구현하고 있다.

### Note
numerical_gradient(self, x, t)는 수치 미분 방식으로 매개변수의 기울기를 계산한다. 오차역전파법을 쓰면 수치 미분을 사용할 때와 거의 같은 결과를 훨씬 빠르게 얻을 수 있다.

### 4.5.3 시험 데이터로 평가하기
1에폭별로 훈련 데이터와 시험 데이터에 대한 정확도를 기록한다.

### Note
에폭(epoch)은 하나의 단위이다. 1에폭은 학습에서 훈련 데이터를 모두 소진했을 때의 횟수에 해당한다. 예컨대 훈련 데이터 10000개를 100개의 미니배치로 학습할 경우, 확률적 경사 하강법을 100회 반복하면 모든 훈련 데이터를 소진한 게 된다. 이 경우 100회가 1에폭이 된다.

훈련 데이터에 지나치게 적응하면, 즉 오버피팅되면 훈련 데이터와는 다른 데이터를 보면 잘못된 판단을 하기 시작한다. 어느 순간부터 시험 데이터에 대한 정확도가 점차 떨어지기 시작한다는 뜻이다. 이 순간이 오버피팅이 시작되는 순간이다. 이 순간을 포착해 학습을 중단하면 오버피팅을 효과적으로 예방할 수 있다. 이 기법을 조기 종료(early stopping)라 하며, 가중치 감소, 드롭아웃과 함께 대표적인 오버피팅 예방법이다.

## 4.6 정리
- 기계학습에서 사용하는 데이터셋은 훈련 데이터와 시험 데이터로 나눠 사용한다.
- 훈련 데이터로 학습한 모델의 범용 능력을 시험 데이터로 평가한다.
- 신경망 학습은 손실 함수를 지표로, 손실 함수의 값이 작아지는 방향으로 가중치 매개변수를 갱신한다.
- 가중치 매개변수를 갱신할 때는 가중치 매개변수의 기울기를 이용하고, 기울어진 방향으로 가중치의 값을 갱신하는 작업을 반복한다.
- 아주 작은 값을 주었을 때의 차분으로 미분하는 것을 수치 미분이라고 한다.
- 수치 미분을 이용해 가중치 매개변수의 기울기를 구할 수 있다.
- 수치 미분을 이용한 계산에는 시간이 걸리지만, 그 구현은 간단하다. 한편, 다음 장에서 구현하는 오차역전파법은 기울기를 고속으로 구할 수 있다.
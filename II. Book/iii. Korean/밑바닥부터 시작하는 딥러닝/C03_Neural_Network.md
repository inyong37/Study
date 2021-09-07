# Chapter 3 신경망

## 3.1 퍼셉트론에서 신경망으로

## 3.2 활성화 함수 (Activation Function)

### 3.2.1 시그모이드 함수 (Sigmoid Function)
h(x) = 1 /  (1 + exp(-x)) ... eq(3.6)

### 3.2.2 계단 함수 (Step Function) 구현하기
```Python
def step_function(x):
  y = x > 0
  return y.astype(np.int)
```

### 3.2.4 시그모이드 함수 구현하기
```Python
def sigmoid(x):
  return 1 / (1 + np.exp(-x))
```

### 3.2.6 비선형 함수

### 3.2.7 ReLU 함수 (Rectified Linear Unit Function, 렐루)

h(x) = x if x > 0 else 0 ... eq(3.7)

```Python
def relu(x):
  return np.maximum(0, x)
```

## 3.3 다차원 배열의 계산

## 3.4 3층 신경망 구현하기

## 3.5 출력층 설계하기

### 3.5.1 항등 함수 (Identify Function) 와 소프트맥스 함수 (Softmax Function) 구현하기
항등 함수를 사용하면 입력 신호가 그대로 출력 신호가 됩니다.

소프트맥스 함수는 다음과 같습니다.

y[k] = exp(a[k])/sum(exp(a)) ... eq(3.10)

```Python
def softmax(a):
  exp_a = np.exp(a)
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a
  return y
```

### 3.5.2 소프트맥스 함수 구현 시 주의점
```Python
def softmax(a):
  c = np.max(a)
  exp_a = np.exp(a - c)
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a
  return y
```

### 3.5.3 소프트맥스 함수의 특징

## 3.6 손글씨 숫자 인식

## 3.7 정리
- 신경망에서는 활성화 함수로 시그모이드 함수와 ReLU 함수 같은 매끄럽게 변화하는 함수를 이용한다.
- 넘파이의 다차원 배열을 잘 사용하면 신경망을 효율적으로 구현할 수 있다.
- 기계학습 문제는 크게 회귀와 분류로 나눌 수 있다.
- 출력층의 활성화 함수로는 회귀에서는 주로 항등 함수를, 분류에서는 주로 소프트맥스 함수를 이용한다.
- 분류에서는 출력층의 뉴런 수를 분류하려는 클래스 수와 같게 설정한다.
- 입력 데이터를 묶은 것을 배치라 하며, 추론 처리를 이 배치 단위로 진행하면 결과를 훨씬 빠르게 얻을 수 있다.

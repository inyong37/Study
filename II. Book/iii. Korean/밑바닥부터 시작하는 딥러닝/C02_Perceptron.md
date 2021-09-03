# Chapter 2 퍼셉트론

## 2.1 퍼셉트론이란?

## 2.2 단순한 논리 회로

## 2.3 퍼셉트론 구현하기

```Python
def AND(x1, x2):
  w1, w2, theta = 0.5, 0.5, 0.7
  tmp = x1*w1 + x2*w2
  if tmp <= theta:
    return 0
  elif tmp > theta:
    return 1
```

```Python
import numpy as np

def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  tmp = np.sum(w*x) + b
  if tmp <= 0:
    return 0
  else:
    return 1

def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5])
  b = 0.7
  tmp = np.sum(w*x) + b
  if tmp <= 0:
    return 0
  else:
    return 1

def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.2
  tmp = np.sum(w*x) + b
  if tmp <= 0:
    return 0
  else:
    return 1
```

## 2.4 퍼셉트론의 한계

## 2.5 다층 퍼셉트론이 출동한다면 (Multi-layer perceptron)

```Python
def XOR(x1, x2):
  s1 = NANA(x1, x2)
  s2 = OR(x1, x2)
  y = AND(s1, s2)
  return y
```

## 2.6 NANA에서 컴퓨터까지

## 2.7

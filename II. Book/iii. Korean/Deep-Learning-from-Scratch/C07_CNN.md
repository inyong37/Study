# Chapter 7 합성곱 신경망 (CNN)

## 7.1 전체 구조

## 7.2 합성곱 계층

### 7.2.3 패딩

### 7.2.4 스트라이드

## 7.3 풀링 계층

## 7.4 합성곱/풀링 계층 구현하기

## 7.5 CNN 구현하기

## 7.6 CNN 시각화하기

## 7.7 대표적인 CNN

### 7.7.1 LeNet

### 7.7.2 AlexNet

## 7.8 정리
- CNN은 지금까지의 완전연결 계층 네트워크에 합성곱 계층과 풀링 계층을 새로 추가한다.
- 합성곱 계층과 풀링 계층은 im2col (이미지를 행렬로 전개하는 함수)을 이용하면 간단하고 효율적으로 구현할 수 있다.
- CNN을 시각화해보면 계층이 깊어질수록 고급 정보가 추출되는 모습을 확인할 수 있다.
- 대표적인 CNN에는 LeNet과 AlexNet이 있다.
- 딥러닝의 발전에는 빅 데이터와 GPU가 크게 기여했다.
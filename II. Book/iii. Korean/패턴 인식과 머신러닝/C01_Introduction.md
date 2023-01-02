# Chapter 1. 소개

패턴 인식은 컴퓨터 알고리즘을 활용하여 데이터의 규칙성을 자동적으로 찾아내고, 이 규칙성을 이용하여 데이터를 각각의 카테고리로 분류하는 등의 일을 하는 분야다.

training set -> target vector

training phase ~ learning phase

test set

generalization

preprocessed or feature extraction or dimensionality reduction

supervised learning:
- classification
- regression

unsupervised learning:
- clustering
- density estimation
- visualization

reinforcement learning: 
- credit assignment
- exploration <-> exploitation; trade off

## 1.1. 예시: 다항식 곡선 피팅

order

error function

model comparison or model selection

over-fitting

root mean square error, RMS error

maximum likelihood

Bayesian

regularization

shrinkage method

quadratic - ridge regression

weight decay

training set, validation set, hold-out set

## 1.2. 확률론

### 1.2.1. 확률 밀도

### 1.2.2. 기댓값과 공분산

### 1.2.3. 베이지안 확률

### 1.2.4. 가우시안 분포

normal distribution = Gaussian distribution

### 1.2.5. 곡선 피팅

### 1.2.6. 베이지안 곡선 피팅

## 1.3. 모델 선택

## 1.4. 차원의 저주 (Curse of Dimensionality)

## 1.5. 결정 이론 (Decision Theory)

inference

decision

### 1.5.1. 오분류 비율의 최소화

decision region

decision boundary = decision surface

### 1.5.2. 기대 손실의 최소화

cost function = loss function

utility function

loss matrix

### 1.5.3. 거부 옵션 (Reject Option)

몇몇 적용 사례에서는 오류 비율을 최소화하기 위해 이처럼 결정을 내리기 힘든 지역에 대해서는 결정을 피하는 것이 적절할 수도 있다. 이것이 바로 거부 옵션이다. 예를 들면 우리의 가상 의학 진단 예시에서 어떤 클래스에 속하는지가 비교적 확실한 엑스레이 이미지들은 자동화 시스템이 분류하고, 다소 불확실한 이미지들은 사람이 직접 확인하도록 하는 것이 적절할 수도 있다.

### 1.5.4. 추론과 결정

inference stage

decision stage

discriminant function

1. 직간접적으로 입력값과 출력값의 분포를 모델링하는 이러한 방식을 생성 모델(generative model)이라고 한다. 왜냐하면 이렇게 만들어진 분포로부터 표본을 추출함으로써 입력 공간에 합성 데이터 포인트들을 생성해 넣는 것이 가능하기 때문이다.
2. 사후 확률을 직접 모델링하는 이러한 방식을 판별 모델(discriminative model)이라고 한다.
3. 각각의 입력값 x를 클래스에 사상하는 판별 함수 f(x)를 찾는다. 예를 들어, 두 개의 클래스를 가진 문제의 경우에 f(.)은 이진값을 출력으로 가지는 함수로써, f=0일 경우 클래스 C1을, f=1일 경우 클래스 C2를 표현할 수 있다. 이 방식에서는 확률론이 사용되지 않는다.

이러한 데이터 포인트들에 대해서는 예측 모델이 낮은 정확도를 보이게 될 것이다. 이런 검출 방식을 이상점 검출(outlier detection) 혹은 새것 검출(novelty detection)이라고 한다.

위험의 최소화

거부 옵션

클래스 사전 확률에 대한 보상

모델들의 결합

조건부 독립(conditional independence)

특정 조건부 독립 가정은 나이브 베이즈 모델(naive Bayes model)의 예시다.

### 1.5.5. 회귀에서의 손실 함수

회귀 함수(regression function)

제곱 손실을 일반화한 예시인 민코프스키 손실(Minkowski loss)

## 1.6. 정보 이론

entropy

엔트로피와 가장 짧은 코드 길이 사이의 관계는 일반적인 것이다. 노이즈 없는 코딩 이론(noiseless coding theorem)에 따르면 엔트로피는 확률 변수의 상태를 전송하기 위해 필요한 비트 숫자의 하한선이다. 

내트(nats)

다중도(multiplicity)

스털링 근사식(Stirling's approximation)

통 안의 물체들의 순서를 미시 상태(microstate)라 하며, ni/N으로 표현되는 통 각각이 가지고 있는 물체의 숫자 비율을 일컬어 거시 상태(macrostate)라 한다. 다중도 W를 거시 상태의 가중치(weight)라 일컫기도 한다.

옌센의 부등식(Jensen's inequality)

평균값의 정리(mean value theorem)

미분 엔트로프(differential entropy)

조건부 엔트로프(conditional entropy)

### 1.6.1. 상대적 엔트로피와 상호 정보량

상대 엔트로피(relative entropy) 또는 쿨백 라이블러 발산(Kullback-Leibler divergence, KL divergence)

볼록 함수(convex function)

순볼록(strictly convex)

오목(concav)

순오목(strictly concave)

상호 정보량(mutual information)

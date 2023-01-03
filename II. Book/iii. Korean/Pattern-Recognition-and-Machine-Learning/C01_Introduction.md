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

확률의 두 가지 기본 법칙은 바로 합의 법칙(sum rule)과 곱의 법칙(product rule)이다.

X와 Y라는 두 가지 확률 변수가 있다. X는 xi(i=1, ..., M) 중 아무 값이나 취할 수 있고, Y는 yi(i=1, ..., L) 중 아무 값이나 취할 수 있다고 하자. 또한, X와 Y 각각에서 표본을 추출하는 시도를 N번 한다고 하자. 그리고 X=xi, Y=yi인 시도의 개수를 nij라 표현하자. 그리고 Y의 값과는 상관없이 X=xi인 시도의 숫자를 ci, X의 값과는 상관없이 Y=yi인 시도의 숫자를 rj로 표현할 것이다.

X가 xi, Y가 yj일 확률을 p(X=xi, Y=yj)로 적고 이를 X=xi, Y=yj일 결합 확률(joint probability)이라 칭한다. 이는 i, j칸에 있는 포인트의 숫자를 전체 포인트들의 숫자로 나눠서 구할 수 있다. 따라서 다음의 식 1.5와 같이 표현된다.

p(X=xi, Y=yj) = nij/N ... (식 1.5)

여기서 lim N->inf를 가정하였다. 비슷하게 Y값과 무관하게 X가 xi값을 가질 확률을 p(X=xi)로 적을 수 있다. 이는 i열에 있는 포인트들의 숫자를 전체 포인트들의 숫자로 나눔으로써 구할 수 있다.

p(X=xi) = ci/N ... (식 1.6)

이는 ci = sum j (nij)로 표현 가능하다. 따라서 식 1.5와 식 1.6을 바탕으로 다음을 도출해 낼 수 있다.

p(X=xi) = sum j=1~L (pX=xi, Y=yj) ... (식 1.7)

이것이 바로 확률의 합의 법칙(sum rule)이다. 때때로 p(X=xi)는 주변 확률(marginal probability)이라고 불린다.

X=xi인 사례들만 고려해 보자. 그들 중에서 Y=yj인 사례들의 비율을 생각해 볼 수 있고, 이를 확률 p(Y=yj|X=xi)로 적을 수 있다. 이를 조건부 확률(conditional probability)이라고 부른다. 이 경우엔 X=xi가 주어졌을 경우 Y=yj일 조건부 확률이다. 이 확률은 i행에 있는 전체 포인트 수와 i, j칸에 있는 포인트 수의 비율을 통해서 계산할 수 있다.

p(Y=yj|X=xi) = nij/ci ... (식 1.8)

식 1.5, 식 1.6, 식 1.8에서 다음의 관계를 도출해 낼 수 있다.

p(X=xi, Y=yj) = nij/N = nij/ci * ci/N = p(Y=yj|X=xi)p(X=xi) ... (식 1.9)

이것이 바로 확률의 곱의 법칙(product rule)이다.

간단한 표현법을 사용해서 확률의 두 가지 기본 법칙을 다음과 같이 적을 수 있다.

확률의 법칙

합의 법칙 p(X) = sum Y p(X, Y) ... (식 1.10)

곱의 법칙 p(X, Y) = p(Y|X)(X) ... (식 1.11)

여기서 p(X, Y)는 결합 확률인데 'X와 Y의 확률'이라고 읽으면 된다. 조건부 확률 p(Y|X)는 'X가 주어졌을 경우 Y의 확률'이라고 읽을 수 있다. p(X)는 주변 확률이며, 'X의 확률'이라고 읽으면 된다. 이 두 법칙은 이 책 전반에서 사용할 확률과 관련된 내용의 기본 토대가 된다.

곱의 법칙과 대칭성 p(X, Y)=P(Y, X)로부터 조건부 확률 간의 관계인 다음 식을 도출해 낼 수 있다.

p(Y|X) = p(X|Y)p(Y) / p(X) ... (식 1.12)

이 식 1.12가 머신 러닝과 패턴 인식 전반에 걸쳐서 아주 중요한 역할을 차지하고 있는 베이즈 정리(Bayes' theorem)다. 합의 법칙을 사용해서 베이지안 정리의 분모를 분자에 있는 항들로 표현할 수 있다.

p(X) = sum Y p(X|Y)p(Y) ... (식 1.13)

베이지안 정리의 분모는 정규화 상수로 볼 수 있다. 식 1.12의 왼쪽 항을 모든 Y 값에 대하여 합했을 때 1이 되도록 하는 역할인 것이다.

만약 어떤 과일이 선택되었는지를 알기 전에 어떤 박스를 선택했냐고 묻는다면 그 확률은 p(B)일 것이다. 이를 사전 확률(prior probability)이라고 부른다. 왜냐하면 어떤 과일이 선택되었는지 관찰하기 '전'의 확률이기 때문이다. 선택된 과일이 오렌지라는 것을 알게 된다면 베이지안 정리를 활용하여 p(B|F)를 구할 수 있다. 이는 사후 확률(posterior probability)이라고 부를 수 있는데, 그 이유는 사건 F를 관측한 '후'의 확률이라 그렇다.

p(X, Y) = p(X)p(Y)인 경우를 고려해 보자. 이처럼 각각의 주변 확률을 곱한 것이 결합 확률과 같을 경우 두 확률 변수를 독립적(independent)이라고 한다. 곱의 법칙에 따라 p(Y|X)=p(Y)임을 알 수 있고 따라서 X가 주어졌을 때 Y의 조건부 확률은 실제로 X의 값과 독립적임을 확인할 수 있다. 이를 우리의 과일 상자 예시에 적용해 보자. 만약에 각각의 상자가 같은 수의 사과와 오렌지를 가지고 있다면 p(F|B)=P(F)가 된다. 즉, 사과(또는 오렌지)를 고를 확률은 어떤 상자를 골랐는지와는 독립적이 된다는 것이다.

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

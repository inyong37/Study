# CHAPTER 8 Dimensionality Reduction

## 8.3 PCA
주성분 분석<sup>Principal Component Analysis</sup>(PCA)은 가장 인기 있는 차원 축소 알고리즘입니다. 먼저 데이터에 가장 가까운 초평면<sup>hyperplane</sup>을 정의한 다음, 데이터를 이 평면에 투영시킵니다.

### 8.3.1 분산 보존

### 8.3.2 주성분

### 8.3.3 d차원으로 투영하기

### 8.3.4 사이킷런 사용하기

### 8.3.5 설명된 분산의 비율

### 8.3.6 적절한 차원 수 선택하기

### 8.3.7 압축을 위한 PCA

### 8.3.8 점진적 PCA

### 8.3.9 랜덤 PCA

## 8.4 커널 PCA

### 8.4.1 커널 선택과 하이퍼파라미터 튜닝

## 8.5 LLE
지역 선형 임베딩<sup>Locally Linear Embedding</sup>(LLE)은 또 다른 강력한 비선형 차원 축소<sup>nonlinear dimensionality reduction</sup>(NLDR) 기술입니다. 이전 알고리즘처럼 투영에 의존하지 않는 매니폴드 학습입니다.

## 8.6 다른 차원 축소 기법
사이킷런은 다양한 차원 축소 기법을 제공합니다. 다음은 그중에서 가장 널리 사용되는 것들입니다.

- 다차원 스케일링<sup>Multidimensional Scaling</sup>(MDS)은 샘플 간의 거리를 보존하면서 차원을 축소합니다.
- Isomap은 각 샘플을 가장 가까운 이웃과 연결하는 식으로 그래프를 만듭니다. 그런 다음 샘플 간의 지오데식 거리<sup>geodesic distance</sup>를 유지하면서 차원을 축소합니다.
- t-SNE<sup>t-Distributed Stochastic Neighbor Embedding</sup>는 비슷한 샘플은 가까이, 비슷하지 않은 샘플은 멀리 떨어지도록 하면서 차원을 축소합니다. 주로 시각화에 많이 사용되며 특히 고차원 공간에 있는 샘플의 군집을 시각화할 때 사용됩니다(예를 들면 MNIST 데이터셋을 2D로 시각화할 때).
- 선형 판별 분석<sup>Linear Discriminant Analysis</sup>(LDA)은 사실 분류 알고리즘입니다. 하지만 훈련 과정에서 클래스 사이를 가장 잘 구분하는 축을 학습합니다. 이 축은 데이터가 투영되는 초평면을 정의하는 데 사용할 수 있습니다. 이 알고리즘의 장점은 투영을 통해 가능한 한 클래스를 멀리 떨어지게 유지시키므로 SVM 분류기 같은 다른 분류 알고리즘을 적용하기 전에 차원을 축소시키는 데 좋습니다.

## 8.7 연습문제

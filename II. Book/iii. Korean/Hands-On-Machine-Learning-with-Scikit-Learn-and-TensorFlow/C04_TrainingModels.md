# CHAPTER 4 모델 훈련
많은 경우 구현의 상세사항을 실제로 알아야 할 필요는 없습니다.

하지만 어떻게 작동하는지 잘 이해하고 있으면 적절한 모델, 올바른 훈련 알고리즘, 작업에 맞는 좋은 하이퍼파라미터를 빠르게 찾을 수 있습니다. 작동 원리를 이해하고 있으면 디버깅이나 에러를 효율적으로 분석하는 데 도움이 됩니다. 

이 장에서는 가장 간단한 모델 중 하나인 선형 회귀부터 시작합니다. 이 모델을 훈련시키는 두 가지 방법을 설명하겠습니다.

- 직접 계산할 수 있는 공식을 사용하여 훈련 세트에 가장 잘 맞는 모델 파라미터(즉, 훈련 세트에 대해 비용 함수를 최소화하는 모델 파라미터)를 해석적으로 구합니다.
- 경사 하강법(GD)이라 불리는 반복적인 최적화 방식을 사용하여 모델 파라미터를 조금씩 바꾸면서 비용 함수를 훈련 세트에 대해 최소화시킵니다. 결국에는 앞의 방법과 동일한 파라미터로 수렴합니다. 경사 하강법의 변종으로 2부에서 신경망을 공부할 때 계속 사용하게 될 배치<sup>Batch</sup> 경사 하강법, 미니배치<sup>Min-batch</sup> 경사 하강법, 확률적<sup>Stochastic</sup> 경사 하강법(SGD)도 살펴보겠습니다.
# 21장 그리디 알고리즘(Greedy Algorithm)

그리디 알고리즘은 글로벌 최적을 찾기 위해 각 단계에서 로컬 최적의 선택하는 휴리스틱 문제 해결 알고리즘이다.

바로 눈앞의 이익만을 좇는 알고리즘이다. 대부분의 경우에는 뛰어난 결과를 도출하지 못하지만, 드물게 최적해를 보장하는 경우도 있다. 그런대로 괜찮은 해를 찾는 것을 목표로 삼는다.

그리디 알고리즘이 잘 작동하는 문제들은 탐욕 선택 속성(Greedy Choice Property)을 갖고 있는 최적 부분 구조(Optimal Substructure)인 문제들이다. 여기서 탐욕 선택 속성이란 앞의 선택이 이후 선택에 영향을 주지 않는 것을 말한다. 다시 말해 그리디 알고리즘은 선택을 다시 고려하지 않는다.

13장에서 살펴본 최단 경로 문제를 풀이하는 다익스트라 알고리즘은 대표적인 그리디 알고리즘의 예로서 최적해를 찾을 수 있다. 또한 압축 알고리즘인 허프만 코딩(Huffman Coding) 알고리즘은 허프만 트리를 빌드할 때 그리디 알고리즘을 사용하며, 머신러닝 분야에서는 의사결정 트리(Decision Tree) 알고리즘으로 유명한 ID3 알고리즘이 그리디 알고리즘이다. 

최적 부분 구조 문제를 푼다는 점에서 흔히 다이나믹 프로그래밍과 비교되는데, 서로 풀 수 있는 문제의 성격이 다르며 알고리즘의 접근 방식 또한 다르다. 다이나믹 프로그래밍이 하위 문제에 대한 최적의 솔루션을 찾은 다음, 이 결과들을 결합한 정보에 입각해 전역 최적 솔루션(Globally Optimum Solution)에 대한 선택을 한다면, 이에 반해 그리디 알고리즘은 각 단계마다 로컬 최적해를 찾는 문제로 접근해 문제를 더 작게 줄여나가는 형태로, 서로 반대 방향으로 접근하는 구조를 띤다.

## 배낭 문제(Knapsack Problem)
배낭 문제(Knapsack Problem)는 조합 최적화(Combinatorial Optimization) 분야의 매우 유명한 문제로, 배낭에 담을 수 있는 무게의 최댓값이 정해져 있고 각각 짐의 가치와 무게가 있는 짐들을 배낭에 넣을 때 가치의 합이 최대가 되도록 짐을 고르는 방법을 찾는 문제다.

짐을 쪼갤 수 있는 경우인 분할 가능 배낭 문제(Fractional Knapsack Problem, 그리디 알고리즘으로 해결)와 짐을 쪼갤 수 없는 경우인 0-1 배낭 문제(다이나믹 프로그래밍으로 해결)로 나뉜다.

```Python
def fractional_knapsack(cargo):
  capacity = 15
  pack = []
  
  for c in cargo:
    pack.append((c[0] / c[1], c[0], c[1]))
  pack.sort(reverse=True)
  
  total_value: float = 0
  for p in pack:
    if capacity - p[2] >= 0:
      capacity -= p[2]
      total_value += p[1]
    else:
      fraction = capacity / p[2]
      total_value += p[1] * fraction
      break
  
  return total_value
```

## 동전 바꾸기 문제

## 가장 큰 합

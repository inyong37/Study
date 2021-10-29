# 15장 힙
힙은 힙의 특성(최소 힙, Min Heap에서는 부모가 항상 자식보다 작거나 같다)을 만족하는 거의 완전한 트리(Almost Complete Tree)인 특수한 트리 기반의 자료구조다.

힙(Heap)은 그래프나 트리와는 전혀 관계 없어 보이는 독특한 이름과 달리, 트리 기반의 자료구조다. 앞서 우선순위 큐를 사용할때 매번 활용했던 heapq 모듈이 바로 힙으로 구현도어 있으며, 그중에서도 파이썬에는 최소 힙만 구현되어 있다. 최소 힙은 부모가 항상 자식보다 작기 때문에 루트가 결국 가장 작은 값을 갖게 되며, 우선순위 큐에서 가장 작은 값을 추추라는 것은 매번 힙의 루트를 가져오는 형태로 구현된다. 기반 구현을 살펴보면, 우선순위 큐 ADT(추상 자료형)는 주로 힙으로 구현하고, 힙은 주로 배열로 구현한다. 따라서 우선순위 큐는 결국은 배열로 구현하는 셈이 된다.

힙은 정렬된 구조가 아니다. 최소 힙의 경우 부모 노드가 항상 작다는 조건만 만족할 뿐, 서로 정렬되어 있지 않다. 부모, 자식 간의 관계만 정의할 뿐, 좌우에 대한 관계는 정의하지 않기 때문이다. 자식이 둘인 힙은 특별히 이진 힙(Binary Heap)이라 하며, 대부분은 이진 힙이 널리 사용된다. 트리 중에는 이진 트리가 널리 사용되는 이유와 비슷하다.

힙이라는 자료구조 자체는 J. W. J. 윌리엄스(Willianms)라는 영국의 컴퓨터과학자가 1964년 힙 정렬 알고리즘을 고안하면서 설계했다. 사실상 힙이라는 자료구조는 힙 정렬의 부산물인 셈이다. 힙은 완전 이진 트리이기 때문에 배열에 순서대로 표현하기에 적합하다. 완전 이진 트리 형태인 이진 힙은 배열에 빈틈없이 배치가 가능하며, 대개 트리의 배열 표현의 경우 계산을 편하게 하기 위해 인덱스는 1부터 사용한다.

힙은 항상 균형을 유지하는 특징 때문에 다양한 분야에 널리 활용된다. 대표적으로 우선순위 큐뿐만 아니라 이를 이용한 다익스트라 알고리즘에도 활용된다. 힙 덕분에 다익스트라 알고리즘의 시간 복잡도는 O(V^2)에서 O(E log V)로 줄어들 수 있었다. 이외에도 원래의 용도인 힙 정렬과 최소 신장 트리(Minimum Spanning Tree)를 구현하는 프림 알고리즘(Prim's Algorithm) 등에도 활용되며, 중앙값의 근사값(Approximation)을 빠르게 구하는 데도 활용할 수 있다. 부모, 자식 관계가 정의되어 있는 완전 이진 트리이기 때문에 적절히 중간 레벨의 노드를 추출하면 중앙값에 가까운 값을 정확하지는 않지만 근사치로 빠르게 추출할 수 있기 때문이다.

## 힙 연산
```Python
class BinaryHeap(object):
  def __init__(self):
    self.items = [None]
  
  def __len__(self):
    return len(self.items) - 1
  
  def _percolate_up(self):
    i = len(self)
    parent = i // 2
    while parent >= 0:
      if self.items[i] < self.items[parent]:
        self.items[parent], self.items[i] = self.items[i], self.items[parent]
      i = parent
      parent = i // 2
  
  def insert(self, k):
    self.items.append(k)
    self._percolate_up()
  
  def _percolate_down(self, idx):
    left = idx * 2
    right = idx * 2 + 1
    smallest = idx
    
    if left <= len(self) and self.items[left] < self.items[smallest]:
      smallest = left
    
    if right <= len(self) and self.items[right] < self.items[smallest]:
      smallest = right
    
    if smallest != idx:
      self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
      self._percolate_down(smallest)
  
  def extract(self):
    extracted = self.items[l]
    self.items[l] = self.items[len(self)]
    self.items.pop()
    self._percolate_down(l)
    return extracted
```

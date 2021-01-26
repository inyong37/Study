# :deciduous_tree: 퀵 정렬 알고리즘(Quick Sort Algorithm)
퀵 정렬 알고리즘은 현존하는 정렬 알고리즘 중에서 가장 빠르다고 알려져 있는 정렬 알고리즘이다. 1960년 C.A.R hoare에 의해 처음 소개되었고 그 이후로도 많은 사람들에 의해 수정되고 보완되어 온 알고리즘이다. 구현하기가 단순하며 사용하는 메모리가 적기 때문에 주로 사용된다. 

정 가운데를 기준이 되는 데이터로 선택하고 기준 데이터의 왼쪽 부분을 왼쪽 팀, 오른쪽 부분을 오른쪽 팀으로 설정한다. 왼쪽 팀의 가장 선두를 왼쪽 팀장으로 하고, 오른쪽 팀의 가장 오른쪽 데이터를 오른쪽 팀장으로 선택하고 왼쪽 팀과 오른쪽 팀의 데이터와 기준이 되는 가운데 데이터를 비교해서 기준이 되는 데이터보다 작으면 왼쪽으로 이동, 기준이 되는 데이터보다 크면 오른쪽 팀으로 이동한다. 왼쪽 팀에서 다시 가운데를 기준이 되는 데이터를 선택하고 오른쪽도 마찬가지로 가운데를 기준이 되는 것으로 선택한다. 그 다음부터는 동일하다. 이러한 과정을 전체 데이터가 모두 정렬될 때까지 반복하면 퀵 정렬 알고리즘이 종료하게 된다.

```Python
def swap(x, i, j):
  x[i], x[j] = x[j], x[i]

def pivotFirst(x, lmark, rmark):
  pivot_val = x[lmark]
  pivot_idx = lmark
  while lmark <= rmark:
    while lmark <= rmark and x[lmark] <= pivot_val:
      lmark += 1
    while lmark <= rmark and x[rmark] >= pivot_val:
      rmark += 1
    if lmark <= rmark:
      swap(x, lmark, rmark)
      lmark += 1
      rmark +=1 
  swap(x, pivot_idx, rmark)
  return rmark

def quickSort(x, pivotMethod=pivotFirst):
  def _qsort(x, first, last):
    if first < last:
      splitpoint = pivotMethod(x, first, last)
      _qsort(x, first, splitpoint-1)
      _qsort(x, splitpoint+1, last)
  _qsort(x, 0, len(x)-1)
```

재귀 호출을 사용하고 있다. 퀵 정렬의 특성상 재귀 호출을 사용하는 것이 훨씬 간단하다. 한 놈을 골라서 그 놈을 기준으로 양쪽으로 나눠서 데이터를 정렬하는 방법이다. 또한 가르고 나서 다시 왼쪽 데이터들은 왼쪽대로, 오른쪽 데이터들은 오른쪽대로 나눠서 퀵 정렬 함수를 진행한다. 반복문을 하나만 사용하는 대신에 재귀 호출을 사용하여 데이터를 2개의 그룹으로 분할하여 정렬을 하는 방법을 사용한다. 이러한 알고리즘을 분할 정복(Divide and Conquer) 알고리즘이라고 말한다.

퀵 정렬 알고리즘의 성능을 O(NlogN)이다. 데이터가 역으로 정렬되어 있는 경우인 최악의 경우에는 오히려 성능이 많이 떨어진다. 최악의 경우에는 O(N^2)으로 다른 선택, 삽입, 거품, 셸 알고리즘과 별반 차이가 없게 된다.

1. 시간의 효율성: O(NlogN)의 실행 시간을 갖는다. 다른 정렬 알고리즘들이 O(N^2)의 실행 시간을 갖는데 비해서 보면 상당히 빠른 정렬 알고리즘이다. 그러나 최악의 경우와 같이 이미 역으로 정렬되어 있는 상태에서는 아무리 퀵 정렬 알고리즘이라고 할질도 기존의 정렬 알고리즘과 동일하게 O(N^2)의 시간 복잡도를 갖게 된다.
2. 공간의 효율성: 별도의 저장 공간이 필요가 없다. 그런 점에서는 뛰어난 알고리즘이라고 할 수 있다.
3. 코드의 효율성: 재귀 호출을 사용한다. 코드의 길이가 짧아지고 컴팩트(Compact)하다는 장점이 있는 반면에, 디버깅이 어렵고 코드를 이해하기가 좀 어려워진다는 단점이 있다. 그러한 단점을 피하기 위해 재귀 호출을 사용하지 않고 스택을 사용하여 퀵 정렬 알고리즘을 구현할 수도 있다.

# :evergreen_tree: 기수 정렬 알고리즘(Radix Sort Algorithm)

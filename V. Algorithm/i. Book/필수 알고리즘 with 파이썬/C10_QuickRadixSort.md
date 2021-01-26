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
기수 정렬이란 정렬할 데이터의 자릿수를 이용하여 데이터를 정렬하는 방법이다. 모든 데이터를 가장 아래의 자릿수에 따라서 정렬을 한다. 일의 자릿수로 정렬한 데이터를 일렬로 배열한다. 10의 자리로 정렬한다. 다시 위 데이터를 하나씩 꺼내어 일렬로 만든다.

```Python
from math import log10

def get_digit(number, base, pos):
  return (number // base ** pos) % base

def prefix_sum(array):
  for i in range(1, len(array)):
    array[i] = array[i] + array[i-1]
  return array

def radixsort(l, base=10):
  passes = int(log10(max(l))+1)
  output = [0] * len(l)
  
  for pos in range(passes):
    count = [0] * base
    
    for i in l:
      digit = get_digit(i, base, pos)
      count[digit] += 1
    
    count = prefix_sum(count)
    
    for i in reversed(l):
      digit = get_digit(i, base, pos)
      count[digit] -= 1
      new_pos = count[digit]
      output[new_pos] = i
      
    l = list(output)
  return output
```

자릿수로 데이터들을 정렬하기 때문에 데이터들을 비교하거나 이동하는 횟수가 거의 없다.

기수 정렬 알고리즘의 특징은 정렬할 데이터의 자릿수에 따라 결정된다. 성능은 자릿수와 정렬할 데이터의 수 그리고 각 자릿수에 따른 큐의 수에 따라 좌우된다. 데이터 자릿수 D와 정렬할 데이터 수 N 그리고 그에 해당하는 큐의 수 Q가 있다고 가정할 때 다음과 같은 알고리즘 성능을 갖게 된다. O(RadixSort) = O(D(N + Q)) 비교 횟수나 이동 횟수가 데이터의 정렬된 상태와 상관없이 데이터의 수 + 큐의 수와 더불어 데이터의 자릿수에 의해 영향을 받게 된다.

이진수로 표한하는 경우에는 자릿 수가 급격히 증가되므로 알고리즘의 전체 성능이 저하되는 단점이 생긴다. 그럼에도 불구하고 이진수 표현법을 사용하는 것은 모든 데이터에 대한 처리를 원할하게 하기 위한 점이 가장 크고, 두 번째는 이진수로 표현하는 경우 프로그램 코드에서 비트 연산을 사용할 수 있으므로 한 번의 연산속도는 비트 연산이 훨씬 빠르다.

1. 시간의 효율성: 기수 정렬 알고리즘은 O(D(N + Q)) 성능을 갖고 있다. 향상시키는 조건은 데이터의 수가 적거나 정렬할 데이터의 자릿수가 적은 경우이다.
2. 공간의 효율성: 기수 정렬 알고리즘은 공간의 효율성이 가장 알고리즘 중의 하나이다. 정렬할 데이터 공간 이외에 별도의 큐를 위한 공간을 확보해야 하기 떄문이다. 이와 같이 메모리를 많이 소비하는 알고리즘은 아무리 정렬 속도가 빠르다고 해도 그다지 좋은 알고리즘이라고 보기 어렵다.
3. 코드의 효율성: 기수 정렬 알고리즘의 코드는 그다지 복잡하지 않다. 하지만 10진수의 경우에는 그다지 복잡하지 않아도 이진수로 데이터를 정렬하는 방법을 사용하면 비트 연산이 포함되기 때문에 코드 내용이 상당히 어려워진다.

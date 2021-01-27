# :deciduous_tree: 이진 검색 알고리즘(Binary Search Algorithm)
검색 알고리즘 중에서 가장 간단한 알고리즘은 주어진 데이터의 처음부터 끝까지 차례로 비교하여 원하는 데이터를 검색하는 방법이다. 이러한 방법을 순차 검색 알고리즘이라고 한다. 순차 검색 알고리즘은 데이터를 검색하는 방법이 간단하다는 장점이 있지만 데이터를 검색하는 시간이 O(N)을 갖는다는 단점이 있다. 데이터의 개수가 많으면 많을수록 검색하는데 필요한 시간이 많이 걸린다는 뜻이다.

이진 검색 알고리즘은 주어진 데이터를 앞에서 배운 여러 가지 정렬 알고리즘을 사용하여 미리 정렬해두어야 한다. 미리 정렬되어 있는 데이터를 절반씩 잘라서 검색하는 방법이다. 이진 탐색에서 N가의 키가 저장되어 있을 때 최악의 경우 (log2N+1)회 비교 횟수가 필요하다.

```Python
from random import randint

global counter

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

def binary_search(a_list, wanted_data):
  global counter
  first = 0
  last = len(a_list)-1
  
  while first <= last:
    idx = (first + last) // 2
    counter += 1
    if a_list[idx] == wanted_data:
      print('{item} found at position {i}'.format(item=wanted_data, i=idx))
      return Ture
    elif a_list[idx] > wanted_data:
      last = idx - 1
    elif a_list[idx] < wanted_data:
      first = idx + 1
    else:
      print('{item} not found in the list'.format(item=wanted_data))
      return False

if __name__ == '__main__':
  data = []
  counter = 0
  input_n = input("전체 데이터의 수:")
  data = [randint(1, 100) for x in range(int(input_n))]
  
  print("<정렬 후>")
  quickSort(data)
  print(data)
  
  msg = binary_search(data, 50)
  if msg == True:
    print("총 {}번의 비교만으로 {}을 검색했습니다.".format(counter, 50))
  print(msg)
```

위 코드에서 퀵 정렬 알고리즘을 사용했다.

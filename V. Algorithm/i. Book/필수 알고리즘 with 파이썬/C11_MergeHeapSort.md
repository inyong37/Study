# :evergreen_tree: 병합 정렬 알고리즘(Merge Sort Algorithm)
기존의 정렬 알고리즘과는 달리 병합 정렬 알고리즘은 이미 정렬되어 있는 데이터들을 하나로 합쳐서 정렬하는 방법이다. 파일에 정렬되어 있는 데이터들을 하나로 합쳐서 정렬하는 경우에도 종종 사용된다. 하드디스크의 용량이 부족하고 지금처럼 대용량의 데이터 저장 장치가 없었던 시절에는 유일한 데이터 백업 장치가 테입 드라이브였다. 테입 드라이브의 특징은 데이터를 처음부터 순차적으로 읽어야 한다는 점이다. 결국 병합 정렬 알고리즘의 특징은 이미 정렬되어 있는 데이터의 그룹 혹은 묶음들을 하나로 합칠 떄 사용하는 방법이 된다.

3개의 서로 다른 데이터 그룹을 하나로 합치는 병합 정렬 알고리즘을 3-way 병합 정렬 알고리즘이라고 하며, 보통의 경우 자주 사용되는 것은 2개의 데이터 그룹을 하나로 합치는 2-way 병합 정렬 알고리즘이다. 하나의 리스트에 저장되어 있는 정렬되지 않는 데이터를 병합 정렬 알고리즘을 사용하는 경우, 정렬되지 있지 않은 데이터들을 정렬하기 위해서 그룹으로 묶는다. 하나의 데이터 리스트를 여러 개로 쪼갠다. 2-way 방식에서는 2개씩 그룹으로 묶는다. 병합을 하기 위한 데이터를 (RUN)이라고 표현한다. 2개의 런을 묶어서 하나의 런으로 합치는 정렬을 하게 된다. 이 다음부터는 모든 데이터가 하나의 런으로 합쳐질 때까지 반복하게 된다. 병합 정렬의 키포인트는 1부터 2의 배수로 하나의 런에 들어가는 데이터의 수를 늘려서 병합하는 과정을 반복한다는 점이다. 이와 같이 반복하여 병합하게 되면 결국 저체 데이터를 모두 정렬하게 되는 결과를 얻을 수 있다.

```Python
def merge_sort(mylist):
  if len(mylist) <= 1: return mylist
  half = len(mylist) // 2
  left_list = merge_sort(mylist[:half]
  right_list = merge_sort(mylist[half:])
  merged_list = []
  
  while len(left_list) > 0 and len(right_list) > 0:
    if left_list[0] > right_list[0]:
      merged_list.append(right_list[0]
      right_list.pop(0)
    else:
      merged_list.append(left_list[0])
      left_list.pop(0)
  
  if len(left_list) > 0: merged_list += left_list
  if len(right_list) > 0: merged_list += right_list
  return merged_list
```

성능은 수치적으로만 보면 퀵 정렬 알고리즘과 비슷하다. 모두 데이터를 분할한 후에 재귀 호출을 사용하기 때문이다.정렬할 데이터가 N개라고 가정하면 데이터를 분할하는데 걸리는 시간은 log2N이 된다. 일단 분할한 후에 2개의 데이터 그룹을 하나로 합치는 데는 O(N)의 시간이 걸린다. 결국 병합 정렬의 성능을 O 표기법으로 표시하면 O(N * log2N)이 된다.

1. 시간의 효율성: O(NlogN)의 실행 시간을 갖아 다른 정렬 알고리즘에 비해서 상당히 빠른 정렬 알고리즘이다. 일반적인 경우에는 빠를지 몰라도 최악의 경우와 같이 이미 정렬이 되어 있는 상태에서는 성능이 급격히 저하된다. 그러나 퀵 정렬 알고리즘이 최악의 경우에 O(N^2)의 성능을 갖는 것에 비하면 오히려 최악의 경우에는 퀵 정렬 알고리즘보다는 나은 정렬 알고리즘이다.
2. 공간의 효율성: 가장 큰 단점이 원래의 데이터 공간 이외에 별도의 데이터 공간이 필요하다는 점이다. 이러한 단점을 극복하는 방법으로는 데이터들을 연결 리스트로 만든 후에 병합 정렬 알고리즘을 사용하는 방법도 있다.
3. 코드의 효율성: 보통의 경우 재귀 호출을 사용한다. 재귀 호출을 사용하면 코드의 길이가 짧아지고 컴팩트(Compact)하다는 장점이 있는 반면에 디버깅이 어렵고 코드를 이애하기 좀 어려워진다는 단점이 있다. 그러한 단점을 피하기 위해 재귀 호출을 사용하지 않고 병합 정렬 알고리즘을 구현할 수도 있다. 그러나 재귀 호출을 사용하는 방식에 비해 코드가 길어지게 된다.

# :palm_tree: 힙 정렬 알고리즘(Heap Sort Algorithm)
힙 정렬 알고리즘은 일반 사용자들이 선호하지는 않지만 운영체제나 네트워크 등 시스템 내부에서 가장 많이 사용되는 정렬 알고리즘이다. 힙 정렬 알고리즘은 우선순위 큐(Priority Queue)를 이용하여 우선순위에 따라 정렬을 하는 알고리즘이다. 우선순위 큐는 앞에서 배운 큐와는 개념적으로 많은 차이가 있다. 스택이나 큐처럼 특별한 형태를 갖는 자료구조가 있는 개념은 아니다. 가장 앞쪽에 있는 데이터가 가장 큰 값을 갖는 데이터가 되어야 한다. 그 외에 다른 데이터들은 어떻게 정렬이 되어 있던지 별 상관이 없다. (자료구조를 배운 학생들이나 심지어 몇 년 동안 프로그램 개발을 업으로 삼고 살고 있는 프로그래머들조차도 우선순위 큐라고 하면 앞에서 배운 큐의 일종이거나 그와 비슷한 무엇이라고 생각하기 쉽지만 결코 그렇지 않다.)

힙 정렬 알고리즘은 트리 구조로 구성되며 루트 노드가 가장 큰 값을 갖게 된다. 일차원 리스트로 주어진 데이터를 힙으로 만드는 과정은, 첫 번째 데이터를 힙에 추가한다. 그리고 다음 데이터를 자식 노드에 추가한다. 그런데 자식 노드의 데이터가 크면 부모와 위치를 바꾼다. 새롭게 추가되는 데이터가 작으면 힙의 규칙에 적합하므로 재구성 작업은 필요없다. 클 때마다 자리를 서로 바꾸어 힙을 구성한다.

```Python
# UPHEAP이기 때문에 정렬은 내림차순으로 된다.

import random

def left_node(idx=None):
  return ((idx + 1) << 1) - 1

def right_node(idx=None):
  return (idx + 1) << 1

def up_head(mylist=None, idx=None, heap_size=None):
  l_node = left_node(idx)
  r_node = right_node(idx)
  
  if l_node <= heap_size and mylist[l_node] > mylist[idx]:
    largest = l_node
  else:
    largest = idx
  if r_node <= heap_size and mylist[r_node] > mylist[largest]:
    largest = r_node
  if largest != idx:
    mylist[idx], mylist[largest] = mylist[largest], mylist[idx]
    up_heap(mylist, largest, heap_size)

def build_heap(mylist=None):
  heap_size = len(mylist) - 1
  for i in reversed(range(len(mylist) // 2)):
    up_heap(mylist, i, heap_size)

def heap_sort(heap=None):
  tmp_arry = list()
  for i in range(len(heap)):
    tmp_arry.append(heap.pop(0))
    up_heap(heap, 0, len(heap) - 1)
  return tmp_arry

if __name_- == '__main__':
  data = []
  input_n = input("정렬할 데이터의 수:")
  data = [random.randint(1, 99999] for x in range(int(input_n))]
  
  build_heap(data)
  
  sorted_data = heap_sort(data)
```

힙 정렬 알고리즘은 트리 구조를 사용하기 떄문에 이진 트리의 성능과 거의 동일하다. 힙에서 사용하는 트리의 깊이가 D라고 했을 때 힙에서 사용하는 데이터 N은 다음과 같은 식이 성립한다. `2D - 1 <= N < 2D - 1` 따라서 힙에서 사용하는 트르의 깊이인 D는 log2N + 1이 된다. 힙 정렬 알고리즘은 최선, 일반, 최악의 경우에 따라 거의 차이가 없다. 따라서 안정된 정렬 알고리즘이라고 볼 수 있지만 정렬을 할 때마다 힙 내부에서 노드들을 반복적으로 이동하므로 실제 성능은 퀵 정렬 알고리즘에 비해서 떨어진다고 볼 수 있다.

1. 시간의 효율성: O(N * log2N)의 성능을 갖고 있다. 따라서 퀵 정렬과 비슷한 성능을 보여주지만 아무래도 힙을 다시 재구성하는 과정이 실행되기 때문에 실제 성능은 퀵 정렬 알고리즘보다 떨어지게 된다.
2. 공간의 효율성: 트리 구조를 사용할 수 있다는 점과 리스트를 사용해서도 구현이 가능하다는 점에서 공간 효율성은 뛰어나다는 볼 수 있다.
3. 코드의 효율성: 힙 정렬 알고리즘의 코드는 퀵 정렬이나 병합 정렬 알고리즘처럼 재귀 호출을 사용하는 것도 아니고 단순히 트리 구조만 알고 있다면 쉽게 이해할 수 있는 만큼 단순하다. 따라서 다른 알고리즘에 비해 코드의 효율성은 좋다고 볼 수 있다.

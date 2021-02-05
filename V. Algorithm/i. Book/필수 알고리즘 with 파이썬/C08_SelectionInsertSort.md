# :palm_tree: 선택 정렬 알고리즘(Selection Sort Algorithm)
선택 정렬 알고리즘의 기본 개념은 데이터의 처음부터 끝까지 훑어가면서 가장 작은 값을 찾은 후에 그 값을 첫 번째 데이터와 자리를 바꾸고, 그 다음에 두 번째로 작은 데이터를 찾아서 두 번째의 데이터와 자리를 바꾸는 방법으로 구현되는 정렬 알고리즘이다.

```Python
import random

def selected_sort(random_list):
  for sel in range(len(random_list)-1):
    min = random_list[sel]
    minindex = sel
    # find min value
    for step in range(sel+1, len(random_list)):
      if min > random_list[step]:
        min = random_list[step]
        minindex = step
    # swap
    random_list[minindex] = random_list[sel]
    random_list[sel] = min

if __name__ == '__main__':
  list = []
  for i in range(10):
    list.append(random.randint(1, 10))
  print("<Before Sort>")
  print(list)
  selected_sort(list) # now sorting
  print("<After Sort>")
  print(list)
```

선택 정렬 알고리즘의 코드에서 아직 정렬되지 않은 부분(제어 변수 step)부터 데이터의 끝까지 for문을 반복하면서 남아 있는 정렬되지 않은 데이터 중의 가장 작은 값을 갖는 데이터를 찾게 된다. 다시 말하면 현재 정렬되지 않은 데이터 중에서 가장 작은 값을 선택 한다는 의미가 된다. 바로 이 선택(Select)이 이 알고리즘의 이름이 선택 정렬(Select Sort) 알고리즘이 된 이유이다.

이와 같은 선택 정렬 알고리즘의 장점은 정렬할 데이터 하나하나의 크기가 큰 경우에 유용하다. 비교 횟수는 (N^2)/2회나 되기 때문에 큰 편이지만 데이터 교환 횟수는 (N-1)회이면 충분하게 된다. 따라서 교환 횟수가 상대적으로 적기 때문에 정렬할 데이터의 크기가 큰 경우라면 다른 정렬 알고리즘보다 유용하다고 볼 수 있다.

# :evergreen_tree: 삽입 정렬 알고리즘(Insert Sort Algorithm)
삽입 정렬 알고리즘은 선택 정렬 알고리즘과 비슷한 알고리즘이다. 선택 정렬 알고리즘이 정렬되지 않은 데이터 중에 가장 작은 값을 찾아서 정렬을 하는 방식이라면 삽입 정렬은 그러한 작은 값을 찾는 검색 과정이 필요 없는 정렬 알고리즘이다. 오히려 순차적으로 정렬하면서 현재의 값을 정렬되어 있는 값들과 비교하여 위치로 삽입하는 방식이다.

```Python
import random
import time

compare_counter = 0
swap_counter = 0

def insertiong_sort(my_list):
  global compare_counter, swap_counter
  my_list.append(0, -1)
  for s_idx in range(2, len(my_list)):
    temp = my_list[s_idx]
    ins_idx = s_idx
    compare_counter += 1
    while my_list[ins_idx-1] > temp:
      swap+counter += 1
      my_list[ins_idx] = my_list[ins_idx-1]
      ins_idx = ins_idx - 1
    
    my_list[ins_idx] = temp
  del my_list[0]

if __name__ == '__main__':
  list = []
  input_n = input("정렬할 데이터 수: ")
  for i in range(int(input_n)):
    list.append(random.randint(1, int(input_n)))
  
  print("<정렬 전>")
  print(list)
  
  start_time = time.time()
  insertion_sort(list)
  running_time = time.time() - start_time
  print("<정렬 후>")
  print(list)
  
  print("데이터의 크기: {}".format(int(input_n)))
  print("비교 횟수: {}".format(compare_counter))
  print("교환 횟수: {}".format(swap_counter))
  print("실행 시간: {}".format(running_time))
```

삽입 정렬 알고리즘의 경우에는 이미 정렬된 데이터, 즉 최선의 경우에는 선택 정렬 알고리즘에 비해 월등히 좋은 성능을 보여준다. 그것은 데이터의 비교 횟수가 입력 데이터의 양에 비례하기 때문이다. 그에 비하여 선택 정렬 알고리즘의 경우에는 N*(N-1)/2에 가까운 수가 된다. 이 경우에는 정렬할 데이터의 수가 많으면 많을수록 선택 정렬 알고리즘에 비해 삽입 정렬 알고리즘의 성능이 좋아진다는 것을 의미한다. 

그러나 최악의 경우가 되면 상황은 달라진다. 선택 정렬보다 삽입 정렬의 성능이 더 안 좋다는 것을 알 수 있다. 삽입 정렬 알고리즘의 경우에는 최악의 경우 비교 횟수도 N*(N-1)/2가 되고, 데이터의 이동 횟수도 N*(N-1)/2가 된다. 이것은 선택 정렬 알고리즘에서 데이터의 이동 횟수가 N인 것에 비해 성능을 감소시키는 요인이 된다.

따라서 삽입 정렬 알고리즘의 성능을 O 표기법으로 표시하면 O(N^2)이 된다. 선택 정렬 알고리즘의 경우에도 동일하기 때문에 두 알고리즘의 성능은 그다지 차이가 없다고 볼 수 있다.

결론적으로 선택 정렬이 비교 횟수가 많고 데이터의 이동 횟수가 적은 반면에, 삽입 정렬은 비교 횟수가 적고 상대적으로 데이터의 이동 횟수가 많은 편에 속한다.

1. 시간의 효율성: 삽입 정렬 알고리즘은 O 표기법에 의하면 O(N^2)의 실행 시간을 갖는다. 실행 시간만을 보면 그다지 좋은 정렬 알고리즘이라고는 볼 수 없다. 그러나 정렬이 어느 정도 되어 있는 경우, 특히 이미 거의 정렬이 되어 있는 경우에는 N에 가까운 성능을 보여준다. 이러한 삽입 정렬의 특성은 이후에 배우게 될 좀 더 발전된 정렬 알고리즘과 함께 사용하면 전반적인 시스템의 성능을 크게 향상 시킬 수 있다.
2. 공간의 효율성: 삽입 정렬 알고리즘은 데이터의 크기가 큰 경우에는 데이터의 교환 횟수가 상대적으로 많기 때문에 그다지 바람직한 정렬 방법은 아니다. 그러나, 하나당 데이터의 크기가 큰 경우에도 인덱스를 사용하는 간접 정렬 방식을 사용하면 삽입 정렬의 단점 중에 하나인 공간의 효율성이 떨어지는 단점을 해결할 수 있다.
3. 코드의 효율성: 삽입 정렬 알고리즘의 코드 복잡도는 반복문을 2번 사용하여 O(N^2)의 성능이 되므로 그다지 좋은 알고리즘이라고 보기는 어렵다.

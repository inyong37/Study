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

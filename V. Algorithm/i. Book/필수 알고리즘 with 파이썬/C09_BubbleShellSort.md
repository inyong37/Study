# :evergreen_tree: 버블 정렬 알고리즘(Bubble Sort Algorithm)
거품 정렬 알고리즘은 순차적으로 바로 옆에 있는 데이터와 비교해서 옆의 데이터가 크면 자신과 위치를 변경한다.

```Python
def bubble_sort(random_list):
  for start_index in range(len(random_list)-1):
    for index in range(1, len(random_list) - start_index):
      if random_list[index-1] > random_list[index]:
        temp = random_list[index-1]
        random_list[index-1] = random_list[index]
        random_list[index] = temp
```

거품 정렬 알고리즘의 성능의 최선의 경우에는 이미 정렬되어 있는 경우이기 때문에 이동 횟수는 이미 0이지만, 비교 횟수는 (NxN)/2가 된다. 최악의 경우에는 비교 횟수와 이동 횟수가 모두 (NxN)/2가 된다. 알고리즘 자체의 성능이 다른 정렬 알고리즘에 비해 많이 떨어진다. 그 이유는 배열끼리의 비교 및 복사를 계속 반복해서 실행하기 때문이다. 성능을 O 표기법으로 표시하면 O(N^2)이 된다.

1. 시간의 효율성: 선택 정렬이나 삽입 정렬보다도 실행 시간을 더 많이 소요한다. 따라서 좋은 알고리즘이라고 볼 수는 없다.
2. 공간의 효율성: 배열끼리의 비교 및 데이터 이동을 하고 있기 때문에 공간적인 면에서는 삽입 정렬이나 선택 정렬과 비슷하다.
3. 코드의 효율성: 복잡도는 for 문을 2번 사용하여 O(N^2)의 성능이 되므로 그다지 좋은 알고리즘이라고 보기는 어렵다.

# :deciduous_tree: 셸 정렬 알고리즘(Shell Sort Algorithm)
셸 정렬 알고리즈의 기본 구조는 삽입 정렬 알고리즘과 같지만 성능면에서는 삽입 정렬 알고리즘과 비교가 되지 않을 정도로 우수하다. 그 이유는 정렬할 데이터를 일정한 구간별로 쪼개서 그 구간 내에서 정렬을 한 후에 구간을 합쳐서 정렬을 하기 때문이다. 다시 말하면 일정 그룹으로 쪼개서 정렬할 후 그룹 내의 정렬이 완료된 후에 전체 정렬을 하기 때문에 비교 횟수가 데이터의 이동 횟수가 훨씬 줄어들게 된다.

```Python
def shell_sort(random_list):
  h = 1
  while h < len(random_list):
    h = h * 3 + 1
  h = h // 3
  
  while h > 0:
    for i in range(h):
      start_index = i + h
      
      while start_index < len(random_list):
        temp = random_list[start_index]
        insert_index = start_index
        
        while insert_index > h - 1 and random_list[insert_index - h] > temp:
          random_list[insert_index] = random_list[insert_index - h]
          insert_index = insert_index - h
        
        random_list[insert_index] = temp
        start_index = start_index + h
      h = h // 3
```

셸 정렬 알고리즘은 선택, 삽입, 거품 정렬 알고리즘에 비해 엄청나게 좋은 성능을 보여주는데, 이는 하나의 데이터와 그룹 간에 비교 이동을 몇 개의 단계로 나누어서 진행하므로 O(N(log2N)) 정도의 성능을 보여주기 때문이다. 데이터의 비교 횟수와 이동 횟수가 현저하게 줄어든다는 점이 셸 정렬 알고리즘의 속도가 빠른 이유가 된다.

1. 시간의 효율성: O 표기법에 의하면 O(N(log2N))의 실행 시간을 갖게 되므로 선택, 삽입, 거품 정렬이 O(N^2)의 실행 시간을 갖는데 비해 월등히 좋은 성능을 보여준다. 현존하는 가장 빠른 정렬 알고리즘이라는 퀵 정렬과 비교해도 손색이 없을 만큼의 성능을 보여준다.
2. 공간의 효율성: 인덱스의 조작만으로 정렬을 하는 독특한 방식이기 때문에 여분의 공간이 필요하거나 불필요한 공간을 사용하지 않는다.
3. 코드의 효율성: 가장 큰 문제는 이해하기가 그리 쉬운 알고리즘이 아니라는 점이다.

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

# :deciduous_tree: 셸 정렬 알고리즘(Shell Sort Algorithm)
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

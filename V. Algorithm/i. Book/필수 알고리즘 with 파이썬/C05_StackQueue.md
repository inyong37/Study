# :dog: 스택(Stack)
스택이란 바닥부터 데이터를 차곡차곡 쌓는 개념이다.

입력과 출력을 한 방향으로 제한한 알고리즘이다.

LIFO(Last In First Out): 마지막으로 들어간 것이 제일 처음 나온다.

시간의 효율성에서 연결 리스트를 사용한다고 배열보다 나은 점은 없다.

공간의 효율성에서 대부분의 스택을 사용하는 경우에는 스택의 크기를 정해놓고서 사용하는 것이 일반적이기 때문에 배열로 구현했다고 공간의 효율성이 저하된다고 보기 어렵다.

코드의 효율성에서 연결 리스트에 대한 코드를 이해할 수 있다면 이것을 이용해서 만든 스택의 코드는 쉽게 이해할 수 있다.

```python
def push(item):
  stack.append(item)

def pop():
  return stack.pop()

if __name__ == '__main__':
  stack = []
  print(stack)
  push(1)
  print(stack)
  push(2)
  while stack:
    print(stack)
    print('pop: {}'.format(pop()))
```

# :cat: 큐(Queue)
큐를 사용하는 대표적인 프로그램은 Windows, Linux와 같은 운영체제이다.

FIFO(First In First Out): 처음으로 저장한 데이터를 처음 사용하는 방식이다.

큐 역시 배열이든 연결 리스트든 어떤 것으로 만들어도 상관없지만, 스택과 달리 큐는 배열을 사용하는 것이 좀 더 편리하다.

시간의 효율성에서 스택과 큐 모두 검색과정이 필요 없기 때문에 배열로 하든 연결 리스트로 하든 상관없다.

공간의 효율성에서 큐의 겨우 미리 정해놓은 배열의 크기만큼으로 한정적이긴 하지만 원형 큐(Circular Queue)형태로 사용하기 때문에 크기와는 상관없이 빙빙 돌면서 사용 가능하다.

코드의 효율성에서 배열의 인덱스 형태로 사용하기 때문에 코드가 간단하다는 장점이 있고, 쉽게 구현이 가능하다.

```python
def put(item):
  queue.append(item)
 
 def get():
  return queue.pop()

if __name__ == '__main__':
  queue = []
  print(queue)
  put(1)
  print(queue)
  put(2)
  while queue:
    print(queue)
    print('get: {}'.format(get()))
```

# :rabbit: 연결 리스트(Linked List)
1. 시간의 효율성

데이터나 노드를 삽입하기 위해서 위치 검색 과정과 삽입 과정이 필요한데, 연결 리스트는 배열에 비해서 삽입하는 과정 시간이 적게 걸린다.

2. 공간의 효율성

배열은 프로그램의 실행 중에 배열의 크기를 변경시키지 못하지만, 연결 리스트는 언제든지 필요할 때 동적으로 공간(메모리)을 할당하여 사용할 수 있으므로 배열에 비해 공간의 효율성이 좋다.

3. 코드의 효율성

배열의 경우 인덱스만으로도 사용 가능하기 때문에 연결 리스트에 비해 코드를 작성할 떄 간단하고, 코드를 이해하기 훨씬 수월하다. 하지만 연결 리스트는 포인터와 구조체로 되어 있기 떄문에 배열에 비해 이해하기 쉽지 않다.

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def init_list():
    global node_A
    node_A = Node("A")
    node_B = Node("B")
    node_C = Node("C")
    node_D = Node("D")
    node_A.next = node_B
    node_B.next = node_C
    node_C.next = node_D


def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print()


if __name__ == '__main__':
    init_list()
    print_list()
```

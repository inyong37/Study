# 이중 연결 리스트 (Double Linked List)
단일 연결 리스트에 비해 링크가 2개 존재하는 이중 연결 리스트는 어디에서도 양쪽 방향으로 탐색이 가능하여 전체적인 탐색 시간을 줄일 수 있다는 장점이 있다.

그에 비해 새로운 노드의 삽입과 삭제를 할 때 코드가 복잡해진다는 단점이 존재한다.

원형 연결 리스트는 마지막 노드가 처음 노드를 가리킨다는 것만 다르다.

```python
class Node:
  def __init__(self, data, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev
```

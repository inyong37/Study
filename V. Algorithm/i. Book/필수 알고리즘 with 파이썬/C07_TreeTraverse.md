# :rabbit: 트리 순회 알고리즘
트리 구조가 많은 알고리즘에서 사용되는 이유는 다른 자료 구조보다 자료를 저장하거나 검색하는 등의 방법이 간단하며 메모리를 효율적으로 사용하기 때문이다.

트리 구조에서 사용하는 트리 순회 알고리즘은 다음과 같이 4가지 알고리즘이 존재한다.

1. 전위 순회(Pre-Order Traverse)
2. 중위 순회(In-Order Traverse)
3. 후위 순회(Post-Order Traverse)
4. 단계 순위 순회(Level-Order Traverse)

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
```

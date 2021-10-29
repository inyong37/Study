# 14장 트리

## 트리의 각 명칭
Root, Child node, Edge, Degree, Size, Height, Depth, Subtree, Uni-Directional

## 그래프 vs 트리
트리는 순환 구조를 갖지 않는 그래프이다.

## 이진 트리
Binary Tree, Binary Search Tree,

- Full Binary Tree(정 이진 트리) 모든 노드가 0개 또는 2개의 자식 노드를 갖음.
- Complete Binary Tree(완전 이진 트리) 마지막 레벨을 제외하고 모든 레벨이 완전히 채워져 있음, 마지막 레벨의 모든 노드는 가장 왼쪽부터 채워져 있음.
- Perfect Binary Tree(포화 이진 트리) 모든 노드가 2개의 자식 노드를 갖고 있음, 모든 리프 노드가 동일한 깊이 또는 레벨을 갖음.

## 이진 탐색 트리(BST)
정렬된 트리, 노드의 왼쪽 서브트리에는 그 노드의 값보다 작은 값들을 지닌 노드들로 이뤄져 있음, 노드의 오른쪽 서브트리에는 그 노드의 값과 같거나 큰 값들을 지닌 노드들로 이루어져있음, 탐색 시 시간 복잡도는 O(logn)임

### 자가 균형 이진 탐색 트리(Self-Balancing Binary Search Tree)
삽입, 삭제 시 자동으로 높이를 작게 유지하는 노드 기반의 이진 탐색 트리

## 트리 순회
그래프 순회의 한 형태로 트리 자료구조에서 각 노드를 정확히 한번 방문하는 과정, Pre-Order(전위) 순회(NLR), In-Order(중위) 순회(LNR), Post-Order(후위) 순회(LRN)

```Python
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def preorder(node):
  if node is None:
    return
  print(node.val)
  preorder(node.left)
  preorder(node.right)

def inorder(node):
  if node is None:
    return
  inorder(node.left)
  print(node.val)
  inroder(node.right)

def postorder(node):
  if node is None:
    return
  postorder(node.left)
  postorder(node.right)
  print(node.val)
```

:bulb: 중첩 함수에서 클래스 변수를 사용한 이유

중첩 함수는 부모 함수의 변수를 자유롭게 읽어드릴 수 있다. 그러나 중첩 함수에서 부모 함수의 변수를 재할당하게 되면 참조 ID가 변경되며 별도의 로컬 변수로 선언된다. 만약 숫자나 문자가 아니라 리스트나 딕셔너리 같은 자료형이라면 append() 등의 메소드를 이용해 재할당 없이 조작이 가능하다. 중첩 함수 내에서도 변수의 값을 조작할 수 있다. 그러나 숫자나 문자인 경우 불변 객체이기 때문에 중첩 함수 내에서는 값을 변경할 수 없다. 이 때문에 클래스 변수를 사용한다.

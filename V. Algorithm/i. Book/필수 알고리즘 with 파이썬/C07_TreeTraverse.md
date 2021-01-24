# :palm_tree: 트리 순회 알고리즘
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

```python
     A
   /   \
  B     C
 / \   / \
D   E F   G
```

## :hamster: 전위 순회(Pre-Order Traverse) 알고리즘
트리 구조를 순회하기 위해 반드시 지켜야 할 기본적인 규칙은 "노드는 오직 한번만 방문한다"이다.

트리 구조에서 트리 구조를 순회하는 방법에는 가운데 노드를 먼저 방문하고 그 다음에는 왼쪽 노드를 방문하고 그리고 나서 오른쪽 노드를 방문하는 방법이다.

`A->B->D->E->C->F->G`

```python
def preorder_traverse(node):
  if node == None: return
  print(node.data, end='->')
  preorder_traverse(node.left)
  preorder_traverse(node.right)
```

## :dog: 중위 순회(In-Order Traverse) 알고리즘
중위 순회 알고리즘은 "왼쪽 자식 노드를 방문하고 그 다음 부모 노드를 방문한 후 다시 오른쪽 자식 노드를 방문"하는 알고리즘이다.

`D->B->E->A->F->C->G`

```python
def inorder_traverse(node):
  if node == None: return
  inorder_traverse(node.left)
  print(node.data, end='->')
  inorder_traverse(node.right)
```

## :cat: 후위 순회(Post-Order Traverse) 알고리즘
중위 순회 알고리즘과는 달리 후위 순회 알고리즘은 왼쪽 자식 노드를 방문하고 다음에 오른쪽 자식 노드를 방문한 후에 마지막으로 부모 노드를 방문하는 알고리즘이 된다.

후위 순회 알고리즘도 중위 순회 알고리즘과 마찬가지로 재귀적 호출 방법으로 구현할 수 있다. 재귀적 호출을 이용한 후위 순회 알고리즘은 재귀적 호출을 사용한 중위 순회 알고리즘과 별반 차이가 없다.

`D->E->B->F->G->C->A`

```python
def postorder_traverse(node):
  if node == None: return
  postorder_traverse(node.left)
  postorder_traverse(node.right)
  print(node.data, end'->')
```

## :hamster: 단계 순회(Level-Order Traverse) 알고리즘
단계 순회 알고리즘은 루트 노드부터 단계 순서대로 왼쪽부터 오른쪽으로 방문하는 순회 알고리즘이다.

`A->B->C->D->E->F->G`

```python
levelq = []

def levelorder_traverse(node):
  global levelq
  levelq.append(node)
  while len(levelq) != 0:
    # visit
    visit_node = levelq.pop(0)
    print(visit_node.data, end='->')
    # child put
    if visit_node.left != None:
      levelq.append(visit_node.left)
    if visit_node.right != None:
      levelq.append(visit_node.right)

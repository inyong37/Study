# 12장 그래프

## 오일러 경로

## 해밀턴 경로

## 그래프 순회(Graph Traversals)

### DFS(깊이 우선 탐색, Depth First Search)

#### 재귀 구조로 표현

```Python
def recursive_dfs(v, discovered=[]):
  discovered.append(v)
  for w in graph[v]:
    if not w in discovered:
      discovered = recursive_dfs(w, discovered)
  return discovered
```

#### 스택을 이용한 반복 구조로 표현

```Python
def iterative_dfs(start_v):
  discovered= []
  stack = [start_v]
  while stack:
    v = stack.pop()
    if v not in discovered:
      discovered.append(v)
      for w in graph[v]:
        stack.append(w)
  return discovered
```

### BFS(너비 우선 탐색, Breadth First Search)

#### 큐를 이용한 반복 구조로 구현

```Python
def iterative_bfs(start_v):
  discovered = [start_v]
  queue = [start_v]
  while queue:
    v = queue.pop(0)
    for w in graph[v]:
      if w not in discovered:
        discovered.append(w)
        queue.append(w)
  return discovered
```

#### 재귀 구현 불가

## 백트래킹
백트래킹(Backtracking)은 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기(백트랙, Backtrack)해 정답을 찾아가는 범용적인 알고리즘으로 제약 충족 문제(Constraint Statisfaction Problems)에 특히 유용하다.

백트래킹은 DFS보다 좀 더 광의의 의미를 지닌다. 백트래킹은 탐색을 하다가 더 갈 수 없으면 왔던 길을 되돌아가 다른 길을 찾는다는 데서 유래했다. 백트래킹은 DFS와 같은 방식으로 탐색하는 모든 방법을 뜻하며, DFS는 백트래킹의 골격을 이루는 알고리즘이다. 백트래킹은 주로 재귀로 구현하며, 알고리즘마다 DFS 변형이 조금씩 일어나지만 기본적으로 모두 DFS의 범주에 속한다. 백트래킹은 가보고 되돌아오고를 반복한다. 운이 좋으면 시행착오를 덜 거치고 목적지에 도착할 수 있지만 최악의 경우에는 모든 경우를 다 거친 다음에 도착할 수 있다. 이 때문에 브루스 포스와 유사하다. 하지만 한번 방문 후 가능성이 없는 경우에는 즉시 후보를 포기한다는 점에서 매번 같은 경로를 방문하는 브루트 포스보다는 훨씬 더 우아한 방식이라 할 수 있다. 

트리가 있을 때 DFS로 탐색을 시도하고, 가능성이 없는 후보는 즉시 포기하고 백트래킹한다면 트리의 불필요한 거의 대부분을 버릴 수 있다. 이를 트리의 가지치기(Pruning)라고 하며, 이처럼 불필요한 부분을 일찍 포기한다면 탐색을 최적화할 수 있기 떄문에, 가지치기는 트리의 탐색 최적화 문제와도 관련이 깊다.

## 제약 충족 문제
제약 충족 문제란 수많은 제약 조건(Constraints)을 충족하는 상태(States)를 찾아내는 수학 문제를 일컫는다.

백트래킹은 제약 충족 문제(Constraint Satisfaction Problems, 이하 CSP)를 풀이하는 데 필수적인 알고리즘이다. 앞서 살펴본 가지치기를 통해 제약 충족 문제를 최적화 하기 때문이다. 특히 제약 충족 문제는 인공지능이나 경영 과학 분야에서 심도 있게 연구되고 있으며, 합리적인 시간 내에 문제를 풀기 위해 휴리스틱과 조합 탐색 같은 개념을 함께 결합해 문제를 풀이한다. 제약 충족 문제는 대표적으로 스도쿠(Sudoku)처럼 1에서 9까지 숫자를 한 번만 넣는(제약 조건 충족) 정답(상태)을 찾아내는 모든 문제 유형을 말한다. 스도쿠를 잘 풀이하려면 백트래킹을 하면서 가지치기를 통해 최적화하는 형태로 풀이할 수 있다. 스도쿠 외에도 십자말 풀이, 8퀸 문제, 4색 문제 같은 퍼즐 문제와 배낭 문제, 문자열 파싱, 조합 최적화 문제 등이 모두 제약 충족 문제에 속한다.

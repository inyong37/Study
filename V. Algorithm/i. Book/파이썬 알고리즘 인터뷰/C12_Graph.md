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

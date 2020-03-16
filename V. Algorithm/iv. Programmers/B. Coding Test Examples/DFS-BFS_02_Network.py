# -*- coding: utf-8 -*-
# Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2020-03-16-Mon
# Programmers
# Coding Test Examples/DFS-BFS_02_Network.py
# 코딩테스트 연습/DFS-BFS/네트워크

# Breath First Search
def bfs(graph, start):
    visit = list()
    queue = list()
    queue.append(start)
    while queue:
      node = queue.pop(0)
      if node not in visit:
          visit.append(node)
          queue.extend(graph[node])
    return visit

# Dpeth First Search
def dfs(graph, start):
    visit = list()
    stack = list()
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit

def solution(n, computers):
    graph = {node: [] for node in range(n)}
    
    for i, computer in enumerate(computers):
        for j, connection in enumerate(computer):
            if i != j and connection == 1:
                graph[i].append(j)
    
    paths = map(sorted, [dfs(graph, node) for node in graph])
    return len(set(["".join(map(str, path)) for path in paths]))

# Reference: https://itholic.github.io/kata-network/
# Reference: https://itholic.github.io/python-bfs-dfs/

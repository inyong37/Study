# Author      : Inyong Hwang (inyong1020@gmail.com).
# Date        : 2020-05-07-Thu.
# Description : Breath First Search (BFS), Depth First Search (DFS)
# State       : Study.
# Environment : Python 3.6.8, PyCharm 2018.1 (Professional), Windows Home 10.0.18362.720.
# Input       : None.
# Output      : None.
# Reference   : https://itholic.github.io/python-bfs-dfs/


def bfs(input_graph, start_node):
    visit = list()
    # first in first out
    queue = list()
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(input_graph[node])
    return visit


def dfs(input_graph, start_node):
    visit = list()
    stack = list()
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(input_graph[node])
    return visit


if __name__ == '__main__':
    # input
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(bfs(graph, 'A'))
    print(dfs(graph, 'A'))

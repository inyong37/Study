# Used Floyd-Warshall Algorithm that makes every nodes to every nodes's the shortest distance.
# Dijkstra algorithm gets the shortest distance from one node to every nodes.

from collections import Counter

def solution(n, results):
    # table of every nodes to every nodes's result of match.
    p = [[0] * n for _ in range(n)]
    # build table using Floyd-Warshall algorithm.
    for a, b in results:
        p[a-1][b-1] = 1
        p[b-1][a-1] = -1
    # fill p(i, j) if it is 0 with p(i, k) and p(k, j).
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if p[i][j] == 0:
                    if p[i][k] == 1 and p[k][j] == 1:
                        p[i][j] = 1
                    elif p[i][k] == -1 and p[k][j] == -1:
                        p[i][j] = -1
    # count all elements are 1 except route of itself.
    answer = 0
    for i in range(n):
        if Counter(p[i])[0] == 1:
            answer += 1
    return answer

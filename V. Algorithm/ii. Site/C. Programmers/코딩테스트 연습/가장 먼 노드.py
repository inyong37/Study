from collections import defaultdict, deque

def solution(n, edge):
    # counts dictonary
    cnts = {i: 0 for i in range(1, n+1)}
    
    # make graph (dictionary) with edge.
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # BFS for distance counts.
    q = deque(graph[1])
    cnt = 1
    while q:
        for i in range(len(q)):
            next = q.popleft()
            # put cnt in counts due to the minimum distance from node '1'.
            if cnts[next] == 0:
                cnts[next] = cnt
                for next_next in graph[next]:
                    q.append(next_next)
        cnt += 1
    
    # remove distance from 1.
    del cnts[1]
    
    # check the most farther nodes with the maximum value.
    max_val = max(cnts.values())
    answer = 0
    for cnt in cnts.values():
        if cnt == max_val:
            answer += 1

    return answer

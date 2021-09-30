from collections import defaultdict, deque

def solution(arrows):
    # move arrow using x, y coordinate system.
    move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    # init point: (0, 0)
    now = (0, 0)
    # queue for points(nodes)
    q = deque()
    q.append(now)
    for idx in arrows:
        # move twice for check crosspoint
        for _ in range(2):
            now = (now[0] + move[idx][0], now[1] + move[idx][1])
            q.append(now)
    now = q.popleft()
    # visited nodes.   
    n = defaultdict(int)
    # visited edges.
    e = defaultdict(int)
    n[now] = 1
    answer = 0
    while q:
        next = q.popleft()
        # already been node for start
        if n[next] == 1:
            # haven't used edge
            if e[(now, next)] == 0:
                answer += 1
        else:
            n[next] = 1
        e[(now, next)] = 1
        e[(next, now)] = 1
        now = next
    return answer

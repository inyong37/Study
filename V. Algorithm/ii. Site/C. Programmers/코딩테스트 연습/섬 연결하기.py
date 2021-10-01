# Kruskal Algorithm with Union Find Algorithm
# Kruskal Algorithm Blog KR, https://it-garden.tistory.com/411, 2021-09-28-Tue.
# Union Find Algorithm Blog KR, https://hellominchan.tistory.com/259, 2021-09-28-Tue.

def solution(n, costs):
    costs.sort(key=lambda cost: cost[2])
    route = []
    num_island = [0]
    for i in range(1, n + 1):
        num_island.append(i)
    
    def find(x):
        if x != num_island[x]:
            num_island[x] = find(num_island[x])
        return num_island[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        num_island[root_x] = root_y
    
    num_edge = 0
    answer = 0
    
    while True:
        if num_edge == n - 1:
            break
        x, y, cost = costs.pop(0)
        if find(x) != find(y):
            union(x, y)
            route.append((x, y))
            answer += cost
            num_edge += 1
    return answer
            

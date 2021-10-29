from typing import List
from collections import defaultdict
import heapq, sys


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        weight = [(sys.maxsize, k)] * n
        
        for f, t, p in flights:
            graph[f].append((t, p))
        
        Q = [(0, src, k)]
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for t, p in graph[node]:
                    alt = price + p
                    if alt < weight[t][0] or k-1 >= weight[t][1]:
                        weight[t] = (alt, k-1)
                        heapq.heappush(Q, (alt, t, k - 1))
        return -1

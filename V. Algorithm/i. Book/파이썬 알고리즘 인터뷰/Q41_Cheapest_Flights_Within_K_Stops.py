class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        Q = [(0, src, k)]
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1

'''
import collections

def findCheapestPrices(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
  graph = collections.deafaultdict(list)
  # 그래프 인접 리스트 구성
  for u, v, w in flights:
    graph[u].append((v, w))
  
  # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
  Q = [(0, src, K)]
  
  # 우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
  while Q:
    price, node, K = heapq.heappop(Q)
    if node == dst:
      return price
    if K >= 0:
      for v, w in graph[node]:
        alt = price + w
        heapq.heappush(Q, (alt, v, k - 1))
  return -1
'''

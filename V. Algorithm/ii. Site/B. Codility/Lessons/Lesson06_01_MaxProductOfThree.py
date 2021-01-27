# 0% https://app.codility.com/demo/results/trainingJFKRTD-HJ7/

def solution(A):
    result = []
    for p in range(0, len(A)-2):
        for q in range(p, len(A)-1):
            for r in range(q, len(A)):
                value = A[p] * A[q] * A[r]
                result.append(value)
    return max(result)

# 44% https://app.codility.com/demo/results/trainingG5FU68-RUE/

def solution(A):
    A = sorted(A)
    return max(A[0] * A[1] * A[2], A[-3] * A[-2] * A[-1])

# 100% https://app.codility.com/demo/results/trainingU8MASD-2QY/

import heapq

def solution(A):
    
    min_heap = []
    max_heap = []
    
    for item in A:
        if len(min_heap) < 2:
            heapq.heappush(min_heap, -item)
        else:
            heapq.heappushpop(min_heap, -item)
        
        if len(max_heap) < 3:
            heapq.heappush(max_heap, item)
        else:
            heapq.heappushpop(max_heap, item)
    
    max_value = heapq.heappop(max_heap) * heapq.heappop(max_heap)
    top_value = heapq.heappop(max_heap)
    max_value *= top_value
    min_value = -heapq.heappop(min_heap) * -heapq.heappop(min_heap) * top_value
    
    return max(max_value, min_value)

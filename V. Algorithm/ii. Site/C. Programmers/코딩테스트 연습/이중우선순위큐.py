# Python's default heap is min-heap, to make max-heap, you have to push with minux(-1).
# or use nlargest to sorted list and then heapify again to make heap.

import heapq

def solution(operations):
    heap = []
    for op in operations:
        if 'I' in op:
            heapq.heappush(heap, int(op.split()[-1]))
        elif 'D 1' == op:
            if heap:
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
        elif 'D -1' == op:
            if heap:
                heapq.heappop(heap)
    if heap:
        answer = heapq.nlargest(1, heap)
        answer.append(heapq.heappop(heap))
        return answer
    return [0, 0]

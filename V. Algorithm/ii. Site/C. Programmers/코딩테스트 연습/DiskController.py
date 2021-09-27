import heapq

def solution(jobs):
    time_cost = 0
    current_time = 0
    i = 0
    start = -1
    heap = []
    while i < len(jobs):
        for in_time, end_time in jobs:
            if start < in_time <= current_time:
                heapq.heappush(heap, [end_time, in_time])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = current_time
            current_time += current[0]
            time_cost += (current_time - current[1])
            i += 1
        else:
            current_time += 1
    return int(time_cost/len(jobs))

# Example is 'First Come First Served (FCFS)' algorithm.
# The solution is 'Shorted Job First (SJF)' non-preemptive algorithm.

import heapq
from math import floor

def solution(jobs):
    time_cost = 0
    current_time = 0
    i = 0
    start = -1
    task_queue = []
    while i < len(jobs):
        for AT, BT in jobs:
            if start < AT <= current_time:
                heapq.heappush(task_queue, [BT, AT])
        if task_queue:
            task_BT, task_AT = heapq.heappop(task_queue)
            start = current_time
            current_time += task_BT
            time_cost += (current_time - task_AT)
            i += 1
        else:
            current_time += 1
    return floor(time_cost/len(jobs))

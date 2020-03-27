# 2020-03-27-Fri
# 기능개발

# Try 1

from collections import deque

def solution(progresses, speeds):
    days = deque()
    answer = list()
    
    # Calculate days of finishing each tasks.
    for index, item in enumerate(progresses):
        count = 1
        while(progresses[index] + count*speeds[index] < 100):
            print('not end', index, count, progresses[index] + count*speeds[index])
            count += 1
        print('end', index, count)
        days.append(count)
    
    # Calculate release days.
    count = 1
    while len(days) >= 2:
        day = days.pop()
        if days[-1] > day:
            count += 1
        else:
            answer.append(count)
            count = 1
    answer.append(count)
    answer.reverse()
    return answer

# Try 2

import math

def solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)]
    front = 0
    for i in range(len(progresses)):
        if progresses[front] < progresses[i]:
            answer.append(i-front)
            front = i
    answer.append(len(progresses)-front)
    return answer

# reference: https://geonlee.tistory.com/122

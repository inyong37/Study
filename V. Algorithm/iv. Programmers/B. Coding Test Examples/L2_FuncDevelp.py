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

# Tried to use combination and brute force method but didn't make it.

from itertools import combinations

def solution(distance, rocks, n):
    # start, destination
    s, d = 0, distance
    # points
    points = [s]
    for rock in sorted(rocks):
        points.append(rock)
    points.append(d)
    # distance between each points
    diff = []
    for i in range(1, len(points)):
        diff.append(points[i] - points[i-1])
    com = list(combinations(diff, n))
    print(com)
    
    answer = 0
    return answer

# Used binary search method.

def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    answer = 0
    while left <= right:
        # assumed max value.
        mid = (left + right) // 2
        # temp min value of min values.
        tmp = float('inf') 
        # current position.
        cur = 0
        # count of removed rocks.
        cnt = 0
        for pos in rocks:
            dif = pos - cur
            # remove the position to make mid is the min value.
            if dif < mid:
                cnt += 1
            else:
                cur = pos
                tmp = min(tmp, dif)
        # if count of removed rocks are bigger than given number n.
        if cnt > n:
            right = mid - 1
        # else count of removed rocks are smaller than given number n.
        else:
            answer = tmp
            left = mid + 1 
    return answer

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

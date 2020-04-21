# 2020-04-21-Tue

# Try 1

def solution(v):
    x1, x2, y1, y2 = 0, 0, 0, 0
    a1, a2, b1, b2 = 0, 0, 0, 0
    p = [x2, y2]
    v.sort()
    for i in range(0, len(v)-1):
        if v[i][0] == v[i+1][0]:
            a1 = v[i][0]
        elif v[i][0] != v[i+1][0] and v[i][0] != a1:
            a2 = v[i][0]
        else:
            a2 = v[i][0]
        if v[i][1] == v[i+1][1]:
            b1 = v[i][1]
        elif v[i][1] != v[i+1][1] and v[i][0] != b1:
            b2 = v[i][1]
        else:
            b2 = v[i][1]
    print(a1, a2, b1, b2)
    return p

# Try 2

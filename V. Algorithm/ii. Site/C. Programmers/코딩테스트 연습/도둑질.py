def solution(money):
    # case 1: the first house is included.
    f = [0] * len(money)
    f[0] = money[0]
    f[1] = max(money[0:2])
    for i in range(2, len(money) -1):
        f[i] = max(f[i-1], f[i-2] + money[i])
    # case 2: the last house is included.
    l = [0] * len(money)
    l[0] = 0
    l[1] = money[1]
    for i in range(2, len(money)):
        l[i] = max(l[i-1], l[i-2] + money[i])
    return max(max(f), max(l))

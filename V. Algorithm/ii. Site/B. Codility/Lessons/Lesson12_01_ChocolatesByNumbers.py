# 12%, https://app.codility.com/demo/results/training6F4DRJ-C4C/

def solution(N: int, M: int) -> int:
    # write your code in Python 3.6
    l = [1] * N
    pos = 0
    cnt = 0
    target = l[pos]
    while target == 1:
        if pos + M < N:
            l[pos] = 0
            pos = pos + M
            target = l[pos]
        else:
        # if pos + M >= N:
            l[pos] = 0
            pos = pos + M - N
            target = l[pos]
        cnt += 1
    return cnt

# 2020-04-08-Wed

def solution(hs):
    a = [0] * len(hs)
    for i in range(len(hs)-1, -1, -1):
        for j in range(i, -1, -1):
            if hs[i] < hs[j]:
                a[i] = j+1
                break
            else:
                pass
    return a

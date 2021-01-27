# 2020-04-21-Tue

def solution(brown, red):
    ans = list()
    # vertical, horizontal
    # (h - 2) * (v - 2) == red
    # h * v - red == brown
    total = brown + red
    for i in range(3, total//2 + 1):
        r = total % i
        if  r == 0:
            v = i
            h = total // i
            if v > h:
                break
            # print(i, h, v)
            ans.append([h, v])
    for itm in ans:
        # if (itm[0] - 2) * (itm[1] - 2) == red and itm[0] * itm[1] - red == brown:
        if (itm[0] - 2) * (itm[1] - 2) == red:
            return itm

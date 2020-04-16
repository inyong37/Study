# 2020-04-16-Thu

# Try 1

from string import ascii_uppercase

def solution(nam):
    # input  : nam (name)
    # output : cnt (count to make name)
    alp = list(ascii_uppercase) # alpabet list
    now = alp[0]                # now alpabet
    idx = 0                     # now index
    cnt = 0
    lng = 25                    # length of alpabet list
    haf = 13                    # half length
    for c in nam:
        nxt = alp.index(c)      # next index
        if  abs(nxt - idx) > haf:
            cnt += idx + lng - nxt
            print('big', idx + lng - nxt, cnt)
        else:
            cnt += abs(nxt - idx)
            print('small', nxt - idx, cnt)
        idx = nxt  
        now = alp[idx]
        print(cnt, now)
        cnt += 1
    return cnt

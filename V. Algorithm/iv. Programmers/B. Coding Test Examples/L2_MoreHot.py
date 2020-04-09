# Author: Inyong Hwang
# 2020-04-09-Thu

# Try 1 72/100

def solution(s, k):
    a = 0
    s.sort(reverse=True)
    while min(s) < k:
        if len(s) == 1:
            return -1
        else:
            l1 = s[-1]
            s.pop()
            l2 = s[-1]
            s.pop()
            s.append(l1 + (l2 * 2))
            a += 1
            s.sort(reverse=True)
    return a

# Reference: http://blog.naver.com/PostView.nhn?blogId=h0609zxc&logNo=221492095742

# Try 2

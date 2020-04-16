# 2020-04-05-Sun

# Try 1

from math import gcd

def solution(w,h):
    if w == h:
        return (w * h) - w
    else:
        d = gcd(w, h)
        wd = w // d # width divided gcd
        hd = h // d # height divided gcd
        a = abs(wd-hd) # absolute value or wd - hd
        return (w * h) - d * (wd * hd - 2 * a)
        #  print(w * h, d, wd * hd, a)
        # answer = (w * h) - d * (wd * hd - 2 * a)
        # return answer

# Try 2

from math import gcd

def solution(w,h):
    if w == h:
        return (w * h) - w
    else:
        '''
        d = gcd(w, h) # d = greates common dividor
        wd = w // d # width divided gcd
        hd = h // d # height divided gcd
        a = abs(wd-hd) # absolute value or wd - hd
        return (w * h) - d * (wd * hd - 2 * a)
        '''
        # using graph/coordinate system
        # passing (0, h), (w, 0) -> m=(0-h)/(w-0)=-1*(h/w)  -> (y)=-1*(h/w)(x-w) -> y = -1*h/w*x+h
        for i in range(0, w):
            print(i, -1*h/w*i+h)

# Try 3

from math import gcd

def solution(w,h):
    if w == h:
        return w * (w - 1)
    else:
        d = gcd(w, h) # d = greates common dividor
        return (w * h) - (w + h - d)

# Reference: https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95-in-python

# Try 4

from math import gcd

def solution(w,h):
    return (w * h) - (w + h - gcd(w, h))

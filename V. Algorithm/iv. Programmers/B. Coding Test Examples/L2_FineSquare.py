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

# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 0. 들어가는 글

import math


def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a


def abs_square(a):
    b = a * a
    return math.sqrt(b)


print(abs_sign(5))
print(abs_sign(-3))
print()
print(abs_square(5))
print(abs_square(-3))

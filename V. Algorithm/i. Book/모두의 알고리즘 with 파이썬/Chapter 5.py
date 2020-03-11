# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 5. 최대공약수 구하기


def gcd_1(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1


print(gcd_1(1, 5))
print(gcd_1(3, 6))
print(gcd_1(60, 24))
print(gcd_1(81, 27))


def gcd_2(a, b):
    if b == 0:
        return a
    return gcd_2(b, a % b)


print(gcd_2(1, 5))
print(gcd_2(3, 6))
print(gcd_2(60, 24))
print(gcd_2(81, 27))

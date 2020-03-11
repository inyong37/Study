# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 4. 팩토리얼 구하기


def fact_1(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


print(fact_1(1))
print(fact_1(5))
print(fact_1(10))


def fact_2(n):
    if n <= 1:
        return 1
    return n * fact_2(n-1)


print(fact_2(1))
print(fact_2(5))
print(fact_2(10))

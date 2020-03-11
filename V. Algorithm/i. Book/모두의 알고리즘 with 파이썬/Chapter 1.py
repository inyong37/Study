# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 1. 1부터 n까지의 합 구하기


def sum_n_1(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s


print(sum_n_1(10))
print(sum_n_1(100))


def sum_n_2(n):
    return n * (n+1) // 2


print(sum_n_2(10))
print(sum_n_2(100))

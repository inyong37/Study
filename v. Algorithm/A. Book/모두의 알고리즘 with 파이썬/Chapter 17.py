# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 17. 가짜 동전 찾기 알고리즘


def weigh(a, b, c, d):
    fake = 29
    if a <= fake <= b:
        return -1
    if c <= fake <= d:
        return 1
    return 0


def find_fake_coin_1(left, right):
    for i in range(left + 1, right + 1):
        result = weigh(left, left, i, i)
        if result == -1:
            return left
        elif result == 1:
            return i
    return -1


n = 100
print(find_fake_coin_1(0, n - 1))


def find_fake_coin_2(left, right):
    if left == right:
        return left
    half = (right - left + 1) // 2
    g1_left = left
    g1_right = left + half - 1
    g2_left = left + half
    g2_right = g2_left + half - 1
    result = weigh(g1_left, g1_right, g2_left, g2_right)
    if result == -1:
        return find_fake_coin_2(g1_left, g1_right)
    elif result == 1:
        return find_fake_coin_2(g2_left, g2_right)
    else:
        return right


n = 100
print(find_fake_coin_2(0, n - 1))

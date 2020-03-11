# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 8. 선택 정렬


def find_min_idx_1(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx


def sel_sort_1(a):
    result = []
    while a:
        min_idx = find_min_idx_1(a)
        value = a.pop(min_idx)
        result.append(value)
    return result


d = [2, 4, 5, 1, 3]
print(sel_sort_1(d))


def sel_sort_2(a):
    n = len(a)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]


d = [2, 4, 5, 1, 3]
sel_sort_2(d)
print(d)

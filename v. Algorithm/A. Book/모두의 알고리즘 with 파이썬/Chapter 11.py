# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 11. 퀵 정렬


def quick_sort_1(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[-1]
    g1 = []
    g2 = []
    for i in range(0, n - 1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])
    return quick_sort_1(g1) + [pivot] + quick_sort_1(g2)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort_1(d))


def quick_sort_sub(a, start, end):
    if end - start <= 0:
        return
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    quick_sort_sub(a, start, i - 1)
    quick_sort_sub(a, i + 1, end)


def quick_sort_2(a):
    quick_sort_sub(a, 0, len(a) - 1)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
quick_sort_2(d)
print(d)

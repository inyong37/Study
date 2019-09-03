# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 9. 삽입 정렬


def find_ins_dix(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)


def ins_sort_1(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_dix(result, value)
        result.insert(ins_idx, value)
    return result


d = [2, 4, 5, 1, 3]
print(ins_sort_1(d))


def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0  and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)

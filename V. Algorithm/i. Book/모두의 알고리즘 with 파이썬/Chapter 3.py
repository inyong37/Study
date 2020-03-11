# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 3. 동명이인 찾기 1


def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result


name = ['Tom', 'Jerry', 'Mike', 'Tom']
print(find_same_name(name))
name2 = ['Tom', 'Jerry', 'Mike', 'Tom', 'Mike']
print(find_same_name(name2))

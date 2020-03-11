# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 14. 동명이인 찾기 2


def find_same_name(a):
    name_dict = {}
    for name in a:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1

    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)
    return result


name_1 = ['Tom', 'Jerry', 'Mike', 'Tom']
print(find_same_name(name_1))

name_2 = ['Tom', 'Jerry', 'Mike', 'Tom', 'Mike']
print(find_same_name(name_2))

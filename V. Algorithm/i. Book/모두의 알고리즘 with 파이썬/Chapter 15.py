# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 15. 친구의 친구 찾기


def print_all_friends_1(g, start):
    qu = []
    done = set()
    qu.append(start)
    done.add(start)
    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)


fr_info_1 = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_friends_1(fr_info_1, 'Summer')
print()
print_all_friends_1(fr_info_1, 'Jerry')
print()


def print_all_friends_2(g, start):
    qu = []
    done = set()
    qu.append((start, 0))
    done.add(start)
    while qu:
        (p, d) = qu.pop(0)
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x, d + 1))
                done.add(x)


fr_info_2 = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_friends_2(fr_info_2, 'Summer')
print()
print_all_friends_2(fr_info_2, 'Jerry')

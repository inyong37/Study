# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 16. 미로 찾기 알고리즘


def solve_maze(g, start, end):
    qu = []
    done = set()
    qu.append(start)
    done.add(start)
    while qu:
        p = qu.pop(0)
        v = p[-1]
        if v == end:
            return p
        for x in g[v]:
            if x not in done:
                qu.append(p + x)
                done.add(x)
    return '?'


maze = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l']
}
print(solve_maze(maze, 'a', 'p'))

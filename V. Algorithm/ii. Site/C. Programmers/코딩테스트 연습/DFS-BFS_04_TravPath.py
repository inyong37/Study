# -*- coding: utf-8 -*-
# Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2020-03-19-Thu
# Programmers
# Coding Test Examples/DFS-BFS_04_TravPath.py
# 코딩테스트 연습/DFS-BFS/여행경로

# Try 1

def solution(tickets):
    g = dict()
    for (start, dest) in tickets:
        g[start] = g.get(start, []) + [dest]
    for key in g.keys():
        g[key].sort(reverse = True)
    s = ["ICN"]
    path = []
    while s:
        top = s[-1]
        if top not in g or len(g[top]) == 0:
            path.append(s.pop())
        else:
            s.append(g[top][-1])
            g[top] = g[top][:-1]
    return path[::-1]

# Reference: https://gurumee92.tistory.com/165

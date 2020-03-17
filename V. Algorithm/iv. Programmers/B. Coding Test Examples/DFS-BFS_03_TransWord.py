# -*- coding: utf-8 -*-
# Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2020-03-17-Tue
# Programmers
# Coding Test Examples/DFS-BFS_03_TransWord.py
# 코딩테스트 연습/DFS-BFS/단어 변환

# Try 1

from collections import deque as queue
transistable = lambda x, y: sum((1 if a!=b else 0) for a, b in zip(x, y)) == 1
def solution(begin, target, words):
    q, d = queue(), dict()
    q .append((begin, 0))
    d[begin] = set(filter(lambda x:transistable(x, begin), words))
    for word in words:
        d[word] = set(filter(lambda x:transistable(x, word), words))
    while q:
        cur, level = q.popleft()
        if level > len(words):
            return 0
        for w in d[cur]:
            if w == target:
                return level + 1
            else:
                q.append((w, level + 1))
    return 0

# Reference: https://cocojelly.github.io/algorithm/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%97%B0%EC%8A%B5-DFS-BFS-(3)/

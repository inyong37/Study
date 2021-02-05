# -*- coding: utf-8 -*-
# Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2020-03-13-Fri
# Programmers
# Coding Test Examples/Sort_03_H-Index
# 코딩테스트 연습/정렬/H-index

# Try 1
def solution(citations):
    for h in range(max(citations), -1, -1):
        count = 0
        for citation in citations:
            if citation >= h:
                count += 1
            if count is h:
                return h

# Try 2
def solution(citations):
    citations.sort(reverse=True)
    return max(map(min, enumerate(citations, start=1)))

# Referece: https://itholic.github.io/kata-h-index/
# Referece: https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-HIndex-in-python

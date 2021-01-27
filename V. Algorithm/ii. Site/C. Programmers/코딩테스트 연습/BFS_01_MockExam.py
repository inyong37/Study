# -*- coding: utf-8 -*-
# Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2020-03-20-Fri
# Programmers
# Coding Test Examples/BFS_01_MockExam
# 코딩테스트 연습/완전탐색/모의고사

from collections import Counter

def solution(answers):
    l = len(answers)
    v1, v2, v3 = int(0), int(0), int(0)
    p1, p2, p3 = list(), list(), list()
    cnt = [0, 0, 0]
    for i in range(l):
        # person 1
        v1 = i % 5 + 1
        p1.append(i % 5 + 1)
        # person 2
        if i % 2 == 0:
            v2 = 2
            p2.append(2)
        else:
            if i % 8 == 1:
                v2 = 1
                p2.append(1)
            elif i % 8 == 3:
                v2 = 3
                p2.append(3)
            elif i % 8 == 5:
                v2 = 4
                p2.append(4)
            else:
                v2 = 5
                p2.append(5)
        # person 3
        if i % 10 == 0 or i % 10 == 1:
            v3 = 3
            p3.append(3)
        elif i % 10 == 2 or i % 10 == 3:
            v3 = 1
            p3.append(1)
        elif i % 10 == 4 or i % 10 == 5:
            v3 = 2
            p3.append(2)
        elif i % 10 == 6 or i % 10 == 7:
            v3 = 4
            p3.append(4)
        else:
            v3 = 5
            p3.append(5)
        # compare
        if answers[i] is v1:
            cnt[0] += 1
        if answers[i] is v2:
            cnt[1] += 1
        if answers[i] is v3:
            cnt[2] += 1
    
    answer = []
    cnt_max = max(cnt)
    
    if cnt.count(cnt_max) == 1:
        return answer.append(cnt.index(max(cnt))+1)
    else:
        for i in range(cnt.count(cnt_max)):
            answer.append(cnt.index(max(cnt))+1)
    return answer
from collections import Counter

def solution(answers):
    l = len(answers)
    v1, v2, v3 = int(0), int(0), int(0)
    p1, p2, p3 = list(), list(), list()
    cnt = [0, 0, 0]
    for i in range(l):
        # person 1
        v1 = i % 5 + 1
        p1.append(i % 5 + 1)
        # person 2
        if i % 2 == 0:
            v2 = 2
            p2.append(2)
        else:
            if i % 8 == 1:
                v2 = 1
                p2.append(1)
            elif i % 8 == 3:
                v2 = 3
                p2.append(3)
            elif i % 8 == 5:
                v2 = 4
                p2.append(4)
            else:
                v2 = 5
                p2.append(5)
        # person 3
        if i % 10 == 0 or i % 10 == 1:
            v3 = 3
            p3.append(3)
        elif i % 10 == 2 or i % 10 == 3:
            v3 = 1
            p3.append(1)
        elif i % 10 == 4 or i % 10 == 5:
            v3 = 2
            p3.append(2)
        elif i % 10 == 6 or i % 10 == 7:
            v3 = 4
            p3.append(4)
        else:
            v3 = 5
            p3.append(5)
        # compare
        if answers[i] is v1:
            cnt[0] += 1
        if answers[i] is v2:
            cnt[1] += 1
        if answers[i] is v3:
            cnt[2] += 1
    
    answer = []
    cnt_max = max(cnt)
    
    answer = [index + 1 for index, content in enumerate(cnt) if content == cnt_max]
    '''
    if cnt.count(cnt_max) == 1:
        answer.append(cnt.index(cnt_max)+1)
    else:
        for i in range(cnt.count(cnt_max)):
            index = cnt.index(cnt_max)
            answer.append(index+1)
            cnt.pop(index)
    '''
    return answer

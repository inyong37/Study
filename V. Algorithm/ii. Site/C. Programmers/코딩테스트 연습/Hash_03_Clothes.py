# -*- coding: utf-8 -*-
# Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2020-03-12-Thu
# Programmers
# Coding Test Examples/Hash_03_Clothes
# 코딩테스트 연습/해시/위장

# Try 1: Counter, for loop for lst

from collections import Counter

def solution(clothes):
    types = []
    types = Counter([value for _, value in clothes])
    answer = 1
    for key in types:
        answer *= (types[key] + 1)
    return answer - 1

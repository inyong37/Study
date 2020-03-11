# -*- coding: utf-8 -*-
# Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2020-03-11-Wed
# Programmers
# Coding Test Examples/Hash_01_Player
# 코딩테스트 연습/해시/완주하지 못한 선수

# Try 1

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(0, len(completion)):
        if participant[i] is not completion[i]:
            answer = participant[i]
        else:
            answer = participant[-1]
    return answer

# Try 2

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(0, len(completion)):
        if participant[i] is not completion[i]:
            return(participant[i])
    return(participant[-1])

# -*- coding: utf-8 -*-
# Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2020-03-13-Fri
# Programmers
# Coding Test Examples/Sort_01_Knum
# 코딩테스트 연습/정렬/K번째수

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        sliced_array = []
        if int(commands[i][0]) == int(commands[i][1]):
            sliced_array = array[int(commands[i][0])-1:int(commands[i][1])]
        else:
            sliced_array = array[int(commands[i][0])-1:int(commands[i][1])]
        sliced_array.sort()
        # answer.append(sliced_array[int(commands[i][2]-1):int(commands[i][2])])
        answer += sliced_array[int(commands[i][2]-1):int(commands[i][2])]
    return answer

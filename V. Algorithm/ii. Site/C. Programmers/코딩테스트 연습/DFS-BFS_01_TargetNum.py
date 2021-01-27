# -*- coding: utf-8 -*-
# Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2020-03-16-Mon
# Programmers
# Coding Test Examples/DFS-BFS_01_TargetNum.py
# 코딩테스트 연습/DFS-BFS/타겟 넘버

# Try 1

def solution(numbers, target):
    answer_list = [0]
    for number in numbers:
        temp_list = []
        for num in answer_list:
            temp_list.append(num+1)
            temp_list.append(num-1)
        answer_list = temp_list
    answer = answer_list.count(target)
    return answer

# Try 2

def solution(numbers, target):
    count = 0
    length = len(numbers)
    
    def function(index=0):
        if index < length:
            numbers[index] *= +1
            function(index+1)
            numbers[index] *= -1
            function(index+1)        
        elif sum(numbers) == target: # and index == length
            nonlocal count
            count += 1
    
    function()
    return count

# Reference: https://itholic.github.io/kata-target-number/

# -*- coding: utf-8 -*-
# Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2020-03-13-Fri
# Programmers
# Coding Test Examples/Sort_02_BigNum
# 코딩테스트 연습/정렬/가장 큰 수

# Try 1
# Using all of numbers in array will be alaway the biggest
def solution(numbers):   
    answer = ''
    answers = []
    n = []
    for i in range(len(numbers)):
        n.append(list(map(int, list(str(numbers[i])))))
    n.sort(reverse=True)
    # print(n)
    arr = []
    for i in range(len(n)):
        temp = []
        if len(n[i]) == 1:
            arr.append(n[i])
        else:
            for j in reversed(range(len(n[i]))):
                temp += str(n[i][j]*(10**j))
            arr.append(temp)
    print(arr)
    for i in range(len(numbers)):
        answer += str(numbers[i])
        answers.append(answer)
    answers.sort()
    return str(answers[0])

# Try 2
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))

# Reference: https://mentha2.tistory.com/9

# 2020-04-08-Wed

# Try 1

def solution(arr):
    laserCount = 0
    stick = list()
    l = 0
    length = list()
    start, end = 0, 0
    stickPos = list()
    for i, a in enumerate(arr):
        if arr[i-1] == '(' and arr[i] == ')':
            laserCount += 1
        
        if a == '(':
            stick.append(a)
            l += 1
            start = i
        elif a == ')':
            stick.pop()
            l += 1
            end = i
        if len(stick) == 0:
            length.append(l)
            l = 0
            stickPos.append([start, end])
            start, end = 0, 0
    print(laserCount, length, stickPos)
    answer = 0
    return answer

# Try 2

def solution(arr):
    stack = list()
    answer = 0
    for a in arr:
        if a == '(':
            stack.append(a)
            last = a
        else: # a = ')'
            if last == '(':
                stack.pop()
                answer += len(stack)
                last = a
                # print(len(stack))
            else: # last = ')'
                stack.pop()
                answer += 1
    return answer

# Refernce: https://itholic.github.io/kata-iron-stick/

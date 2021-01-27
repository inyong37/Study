# 2020-04-03-Fri

def solution(a, b):
    if a > b:
        answer = b
        for i in range(b+1, a+1):
            answer += i
        return answer
    elif a < b:
        answer = a
        for i in range(a+1, b+1):
            answer += i
        return answer
    else:
        return a

# 2020-04-14

def solution(s):
    answer = 1000 # the longest string length
    for i in range(1, len(s)//2 + 1): # the last case that can compare is half length of string
        ret = '' # comparing word
        cnt = 1 # number that matches
        pre = s[:i] # previous comparing word
        for j in range(i, len(s) + i, i):
            if pre == s[j:j + i]: # match with previous comparing word and next
                cnt += 1 # if matches count
            else:
                if cnt != 1: 
                    ret = ret + str(cnt) + pre
                else:
                    ret = ret + pre
                pre = s[j:j+i]
                cnt = 1
        answer = min(answer, len(ret))
    return min(answer, len(s))

# Reference: https://copy-driven-dev.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-ProgrammersPython-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%95%95%EC%B6%95

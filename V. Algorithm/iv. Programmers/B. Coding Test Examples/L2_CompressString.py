# 2020-04-14

def solution(s):
    answer = 1000   # the longest string length
    # the last case that can compare is half length of string
    for i in range(1, len(s)//2 + 1): 
        leg = ''    # legacy
        cnt = 1     # number that matches
        pre = s[:i] # previous comparing word
        # compare with string set for each
        for j in range(i, len(s) + i, i):
            # matched plus count
            if pre == s[j:j + i]:
                cnt += 1
            # not matched stack legacy and reset
            else:
                # stack legacy with count
                if cnt != 1: 
                    leg = leg + str(cnt) + pre
                # stack legacy without count
                else:
                    leg = leg + pre
                # reset
                pre = s[j:j + i]
                cnt = 1
        # choose smaller one while comparing
        answer = min(answer, len(leg))
    # choose minimum between smaller one in answer and string
    return min(answer, len(s))

# Reference: https://copy-driven-dev.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-ProgrammersPython-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%95%95%EC%B6%95

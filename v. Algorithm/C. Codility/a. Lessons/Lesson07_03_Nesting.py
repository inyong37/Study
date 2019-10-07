# 100% https://app.codility.com/demo/results/training9S6T8S-WXM/

def solution(S):
    if len(S) == 0:
        return 1
    elif len(S) % 2 != 0:
        return 0
    else:
        count = 0
        for i in S:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
            
            if count < 0:
                return 0
        
        if count != 0:
            return 0
        
        return 1

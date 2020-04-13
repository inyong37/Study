# 2020-04-13-Mon
# 숫자 야구

from itertools import permutations

def check(question, candidate, strike, ball):
    temp_strike = 0
    for i in range(len(question)):
        if question[i] == candidate[i]:
            temp_strike += 1
    if strike != temp_strike:
        return False
    temp_ball = len(set(question) & set(candidate))-temp_strike
    if ball != temp_ball:
        return False
    return True

def solution(baseball):
    l = list(permutations([i for i in range(1, 10)], 3))
    for i in baseball:
        for item in l[:]:
            if not check([int(i) for i in list(str(i[0]))], item, i[1], i[2]):
                l.remove(item)
    return len(l)

# Reference: https://geonlee.tistory.com/116

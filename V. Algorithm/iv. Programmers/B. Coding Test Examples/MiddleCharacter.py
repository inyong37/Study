# 2020-03-24-Tue
# 코딩테스트 연습>연습문제>가운데 글자 가져오기


import math

def solution(s):
    if len(s) % 2 == 0:
        # print('even', len(s), len(s)/2)
        return s[math.floor(len(s)/2)-1:math.ceil(len(s)/2)+1]
    else:
        # print('odd', len(s), math.floor(len(s)/2), math.ceil(len(s)/2))
        return s[math.floor(len(s)/2)]

# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2019-09-11-Wed
# 필수 알고리즘 with 파이썬
# Problem 1. 반복문을 사용하여 0부터 n까지의 합 출력하기


def p1_1(a):
    i = 0
    result = 0
    while i <= a:
        result = result + i
        i = i + 1
    return result


def p1_2(a):
    result = (a * (a + 1)) // 2
    return result


if __name__ == '__main__':
    n = 100
    answer = p1_1(n)
    print(answer)
    answer = p1_2(n)
    print(answer)

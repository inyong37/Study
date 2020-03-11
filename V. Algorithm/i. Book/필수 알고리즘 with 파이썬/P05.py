# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2019-09-18-Wed
# 필수 알고리즘 with 파이썬
# Problem 5. 3과 5의 배수 계산하기


def p5(a):
    i = 1
    while i < a:
        if (i % 3 == 0) and (i % 5 == 0):
            print('%d' % i)
        i = i + 1


if __name__ == '__main__':
    n = 100
    p5(n)


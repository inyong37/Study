# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2019-09-18-Wed
# 필수 알고리즘 with 파이썬
# Problem 4. 재귀 호출을 사용하여 n부터 1까지 출력하기


def p4(a):
    print(a)
    if a > 1:
        p4(a - 1)


if __name__ == '__main__':
    n = 20
    p4(n)


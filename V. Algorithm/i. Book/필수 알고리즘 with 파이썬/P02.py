# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2019-09-11-Wed
# 필수 알고리즘 with 파이썬
# Problem 2. 재귀 호출을 사용하여 1부터 20까지 출력하기


def p2(a):
    if a > 0:
        p2(a - 1)
    print(a)


if __name__ == '__main__':
    n = 20
    p2(n)

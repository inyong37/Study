# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: 2019-10-17-Thu
# 필수 알고리즘 with 파이썬
# Problem 30. 이진 트리에서 두 노드사이의 거리 구하기


def p30_1(node1, node2):
    if node1 == node2:
        return 0

    if node1 < node2:
        return p30_1(node1, node2 // 2) + 1

    if node1 > node2:
        return p30_1(node1 // 2, node2) + 1


def p30_2(node1, node2):
    if node1 == node2:
        return 0

    elif node1 < node2:
        return p30_1(node1, node2 // 2) + 1

    elif node1 > node2:
        return p30_1(node1 // 2, node2) + 1


if __name__ == '__main__':
    a = int(input('first node:'))
    b = int(input('second node:'))
    # print('distance between %d and %d is: %d' % (a, b, p30_1(a, b)))
    print('distance between %d and %d is: %d' % (a, b, p30_2(a, b)))

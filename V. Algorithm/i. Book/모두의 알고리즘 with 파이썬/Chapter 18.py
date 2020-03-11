# -*- coding: utf-8 -*-
# Modified Author: Inyong Hwang (inyong1020@gmail.com)
# Date: *-*-*-*
# 모두의 알고리즘 with 파이썬
# Chapter 18. 최대 수익 알고리즘

import time
import random


def max_profit_1(prices):
    n = len(prices)
    max_profit = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit


stock_1 = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit_1(stock_1))


def max_profit_2(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]
    for i in range(1, n):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]
    return max_profit


stock_2 = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit_2(stock_2))


def test(n):
    a = []
    for i in range(0, n):
        a.append(random.randint(5000, 20000))
    start = time.time()
    mp_1 = max_profit_1(a)
    end = time.time()
    time_1 = end - start
    start = time.time()
    mp_2 = max_profit_2(a)
    end = time.time()
    time_2 = end - start
    print(n, mp_1, mp_2)
    m = 0
    if time_2 > 0:
        m = time_1 / time_2
    print('%d %.5f %.5f %.2f' % (n, time_1, time_2, m))


test(100)
test(10000)

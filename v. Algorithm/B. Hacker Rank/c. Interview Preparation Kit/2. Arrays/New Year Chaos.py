#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    for index, item in enumerate(q):
        if (item - 1) - index > 2:
            return 'Too chaotic'
        for j in range(max(0, item - 2), index):
            if q[j] > item:
                count += 1
    return count

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        result = minimumBribes(q)
        print(result)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level=valley=0
    for i in range(n):
        if(s[i]=='U'):
            level+=1
            if(level==0):
                valley+=1
        else:
            level-=1
    return valley

'''
def countingValleys(n, s):
    result = 0
    d_count = 0
    u_count = 0
    index = 0
    while True:
    # for index, item in enumerate(s):
        if s[index] is 'U':
            u_count += 1
        elif s[index] is 'D':
            d_count += 1
        else:
            print("input is wrong")
            break
        if u_count > d_count:
            if s[index] is 'U':
                result += 1
                index += 1
        elif u_count < d_count:
            if s[index] is 'U':
                result += 1
                index += 1
        elif abs(u_count - d_count) is 1:
            result -= 1
        else:
            pass
        # print('u:', u_count)
        # print('d:', d_count)
        index += 1
        if index >= len(s):
            break
    return result
'''


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

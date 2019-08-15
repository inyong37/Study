#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n, c):
    jumps = 0
    index = 0
    while True:
        if c[index] == 0 and c[index+1] == 0:
            jumps += 1
            index += 2
        elif c[index] == 0 and c[index+1] == 1:
            jumps += 1
            index += 2
        elif c[index] == 1:
            jumps += 1
            index += 1
        else:
            print('input is wrong')
            break
        if  index >= n-1:
            break
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()

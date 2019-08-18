#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    '''
    arguments
    input
    a: array
    d: rotation constant
    output
    ra: rotated array
    '''
    '''
    ra = a
    for i in range(0, len(a)):
        if i + d > len(a) - 1:
            ra[i] = a[i + d - len(a)]
        else:
            ra[i] = a[i + d]
    return ra
    '''
    return a[d:] + a[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

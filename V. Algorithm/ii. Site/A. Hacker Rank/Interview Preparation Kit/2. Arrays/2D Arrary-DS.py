#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    '''
    [i][j]
    [0][0]  [0][1]  [0][2]
            [1][1]
    [2][0]  [2][1]  [2][2]
    '''
    arr_sums = []
    i = j = 0
    while True:
        arr_sum = 0
        arr_sum = arr_sum + arr[i][j] + arr[i][j+1] + arr[i][j+2]
        arr_sum = arr_sum + arr[i+1][j+1]
        arr_sum = arr_sum + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        arr_sums.append(arr_sum)
        if j + 2 == len(arr) - 1:
            i += 1
            j = 0
        else:
            j += 1
        if i + 2 == len(arr):
            break
    print(arr_sums)
    return max(arr_sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

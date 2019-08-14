#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    pair_count = 0
    index = 0
    while True:
        if index >= 1 and ar[index] is ar[index-1]:
            pair_count += 1
            index += 2     
        else:
            index += 1
        if index >= len(ar):
            break

    result = pair_count
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

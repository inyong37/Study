#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    occurrences = 0
    # step 1
    for _, item in enumerate(s):
        if item == 'a':
            occurrences += 1
    # step 2
    value = int(n / len(s))
    occurrences = occurrences * value
    # step 3
    rest_count = n - value * len(s)
    rest_value = 0
    for i in range(rest_count):
        if s[i] == 'a':
            rest_value += 1
    occurrences = occurrences + rest_value
    return occurrences

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

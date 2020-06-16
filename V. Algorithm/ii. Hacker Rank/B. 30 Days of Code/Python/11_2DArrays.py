# Author      : inyong1020@gmail.com
# Date        : 2020-06-16-Tue.
# Description : Hacker Rank; 30 Days of code; Day 11: 2D Arrays.
# State       : Passed.
# Environment : -
# Input       : -
# Output      : -

"""
Objective
Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video!

Context
Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Input Format

There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .

Constraints

Output Format

Print the largest (maximum) hourglass sum found in .

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
Explanation

 contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4
"""
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0],
          [0, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [0, 0, 2, 4, 4, 0],
          [0, 0, 0, 2, 0, 0],
          [0, 0, 1, 2, 4, 0]]
    # arr = []
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    result = []
    for i in range(2, len(arr)):
        for j in range(2, len(arr[i])):
            # tmp = arr[i-2][j-2] + arr[i-2][j-1] + arr[i-2][j] + arr[i-1][j-1] + arr[i][j-2] + arr[i][j-1] + arr[i][j]
            tmp = sum(arr[i-2][j-2:j+1]) + arr[i-1][j-1] + sum(arr[i][j-2:j+1])
            # if result < tmp:
            #     result = tmp
            result.append(tmp)
    # print(result)
    print(max(result))
    # max(result) works

# Author      : inyong1020@gmail.com
# Date        : 2020-06-27-Sat.
# Description : Hacker Rank; 30 Days of code; Day 25: Running Time and Complexity.
# State       : Not passed.
# Environment : -
# Input       : -
# Output      : -
# Reference   : https://brownbears.tistory.com/445
"""
Objective
Today we're learning about running time! Check out the Tutorial tab for learning materials and an instructional video!

Task
A prime is a natural number greater than  that has no positive divisors other than  and itself. Given a number, , determine and print whether it's  or .

Note: If possible, try to come up with a  primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code!

Input Format

The first line contains an integer, , the number of test cases.
Each of the  subsequent lines contains an integer, , to be tested for primality.

Constraints

Output Format

For each test case, print whether  is  or  on a new line.

Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime
Explanation

Test Case 0: .
 is divisible by numbers other than  and itself (i.e.: , , ), so we print  on a new line.

Test Case 1: .
 is only divisible  and itself, so we print  on a new line.

Test Case 2: .
 is only divisible  and itself, so we print  on a new line.
 """
# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from math import ceil, sqrt


def sieveOfEratosthenes(integers):
    answers = dict()
    for idx, itm in enumerate(integers):
        answers[itm] = True
    integer = max(integers)
    sieve = [0, 0] + [1] * (integer-1)
    for i in range(2, ceil(sqrt(integer+1))):
        if sieve[i]:
            for j in range(2*i, integer+1, i):
                if i in list(answers.keys()) or j in list(answers.keys()):
                    answers[itm] = False
                sieve[j] = 0
    return answers


n = int(sys.stdin.readline())
input_integers = list()
for _ in range(n):
    input_integers.append(int(sys.stdin.readline()))

answers = sieveOfEratosthenes(input_integers)
for answer in answers.values():
    if answer:
        print('Prime')
    else:
        print('Not prime')

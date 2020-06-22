# Author      : inyong1020@gmail.com
# Date        : 2020-06-22-Mon.
# Description : Hacker Rank; 30 Days of code; Day 19: Interfaces.
# State       : Passed.
# Environment : -
# Input       : -
# Output      : -
# Reference   : Abstract Base Class(ABC), https://bluese05.tistory.com/61, 2020-06-22-Mon.

"""
Objective
Today, we're learning about Interfaces. Check out the Tutorial tab for learning materials and an instructional video!

Task
The AdvancedArithmetic interface and the method declaration for the abstract divisorSum(n) method are provided for you in the editor below.

Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface. The implementation for the divisorSum(n) method must return the sum of all divisors of .

Input Format

A single line containing an integer, .

Constraints

Output Format

You are not responsible for printing anything to stdout. The locked template code in the editor below will call your code and print the necessary output.

Sample Input

6
Sample Output

I implemented: AdvancedArithmetic
12
Explanation

The integer  is evenly divisible by , , , and . Our divisorSum method should return the sum of these numbers, which is . The Solution class then prints  on the first line, followed by the sum returned by divisorSum (which is ) on the second line.
"""


class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        result = int()
        for idx in range(1, n + 1):
            if n % idx == 0:
                result += idx
        return result


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

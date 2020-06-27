import sys


def game(idx, n):
    x = 1
    if x > n:
        return print('#' + idx, 'Bob')
    else:
        return print('#' + idx, 'Alice')


cnt = int(sys.stdin.readline())
for idx in range(cnt):
    n = int(sys.stdin.readline())
    game(idx + 1, n)

"""
test case
N = 1: 1->2/3 b
2*x+1 = 3
2*x = 2 
N = 2: 1->2->4/5 a
2*x+1 = 3
2*x = 2

"""

import sys

n = input()
for _ in range(int(n)):
    a, b = map(int, sys.stdin.readline().split(','))
    print(a + b)
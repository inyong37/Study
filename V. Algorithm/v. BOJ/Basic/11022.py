import sys

n = input()
for i in range(int(n)):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{i + 1}: {a} + {b} = {a + b}')
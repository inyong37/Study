import sys

n = input()
for i in range(int(n)):
    print('Case #{0}: {1}'.format(i + 1, sum(map(int, sys.stdin.readline().split()))))
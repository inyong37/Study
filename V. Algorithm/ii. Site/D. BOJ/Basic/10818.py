import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
print(f'{min(nums)} {max(nums)}')
import sys

n = input()
total = 0
nums = str(input())
for character in nums:
    total += int(character)
print(total)
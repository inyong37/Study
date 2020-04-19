# 2020-04-19-Sun


# Try 1

from itertools import permutations

def solution(number, k):
    permute = list(permutations(number, len(number) - k))
    answer = str(max(permute))
    return answer

# Try 2


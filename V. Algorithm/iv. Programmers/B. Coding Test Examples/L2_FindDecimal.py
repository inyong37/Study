# 2020-04-07-Tue

from itertools import permutations

def solution(numbers):
    l = list(numbers)
    for i in range(2, len(numbers)+1):
        p = list(permutations(numbers, i))
        for j in p:
            if len(j) <= len(numbers):
                l.append(''.join(j))
    l = list(set([int(x) for x in l]))
    
    if l.count(1):
        l.remove(1)
    if l.count(0):
        l.remove(0)
    
    answer = 0
    for x in l:
        i = 2
        while i*i <= x:
            if x % i == 0:
                answer -= 1
                break
            i += 1
        answer += 1
    return answer

# Reference: https://yurimkoo.github.io/algorithm/2019/09/26/find_prime_number.html

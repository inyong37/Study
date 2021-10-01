from collections import defaultdict

def solution(N, number):
    if N == number:
        return 1
    s = [set() for _ in range(8)]
    # add N, NN, NNN, ... , NNNNNNNN to sets.
    for idx, ele in enumerate(s, start=1):
        ele.add(int(str(N) * idx))
    # add result of arithmetic operation to sets.
    for i in range(1, len(s)):
        for j in range(i):
            for x in s[j]:
                for y in s[i-j-1]:
                    s[i].add(x + y)
                    s[i].add(x - y)
                    s[i].add(x * y)
                    if y != 0: s[i].add(x // y)
        # check if number is in set.
        if number in s[i]:
            return i + 1
    return -1

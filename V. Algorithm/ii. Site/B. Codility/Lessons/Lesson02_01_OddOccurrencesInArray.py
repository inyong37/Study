def solution(A):
    A = sorted(A)
    
    if len(A) == 1:
        return A[0]
    else:
        for i in range(0, len(A)-1, 2):
            if A[i] != A[i+1]:
                return A[i]
    return A[-1]

# 2021-03-17-Tue_44% https://app.codility.com/demo/results/training6GPZPC-MA2/
import collections

def solution(A):
    result = collections.Counter(A)
    return result.popitem()[0]

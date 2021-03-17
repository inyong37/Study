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


# 2021-03-17-Tue_66% https://app.codility.com/demo/results/trainingD4W5BP-XJ9/ runtime error result[1] -> there might be 1/3/5... odd, 2 ,3, 4 
import collections

def solution(A):
    result = collections.Counter(A)
    result = {v: k for k, v in result.items()}
    return result[1]

# 2021-03-17-Tue_100% https://app.codility.com/demo/results/trainingE8FHXR-E68/ O(N) or O(N*logN)
import collections

def solution(A):
    result = collections.Counter(A)
    result = {v: k for k, v in result.items()}
    for key, val in result.items():
        if key % 2 == 1:
            return val

# 2021-03-17-Tue_100% https://app.codility.com/demo/results/trainingC7X2YY-DTT/
import collections

def solution(A):
    result = collections.Counter(A)
    for key, val in result.items():
        if val % 2 == 1:
            return key

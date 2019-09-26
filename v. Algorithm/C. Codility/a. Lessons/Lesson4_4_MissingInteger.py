# 33% https://app.codility.com/demo/results/training2SZWKV-83Y/

def solution(A):
    value = [0] * (len(A) + 1)
    result = 1
    for i in range(0, len(A)):
        if A[i] <= 0:
            pass
        else:
            value[A[i]-1] = 1
    for i in range(0, len(value)):
        if value[i] == 0:
            return i + 1
    return result

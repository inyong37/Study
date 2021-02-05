# 88% https://app.codility.com/demo/results/trainingZ8JPS2-24S/

def solution(N, A):
    result = [0] * N
    value = 0
    for i in range(0, len(A)):
        if A[i] == N + 1:
            result = [value] * N
        else:
            result[A[i]-1] += 1
            if result[A[i]-1] >= value:
                value = result[A[i]-1]
    return result

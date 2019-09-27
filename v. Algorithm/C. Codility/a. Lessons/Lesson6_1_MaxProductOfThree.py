# 0% https://app.codility.com/demo/results/trainingJFKRTD-HJ7/

def solution(A):
    result = []
    for p in range(0, len(A)-2):
        for q in range(p, len(A)-1):
            for r in range(q, len(A)):
                value = A[p] * A[q] * A[r]
                result.append(value)
    return max(result)

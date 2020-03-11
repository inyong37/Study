# 75% https://app.codility.com/demo/results/trainingWE98VD-YRT/

def solution(A):
    for p in range(0, len(A)-2):
        for q in range(p+1, len(A)-1):
            for r in range(q+1, len(A)):
                if A[p] + A[q] > A[r] and A[q] + A[r] > A[p] and A[r] + A[p] > A[q]:
                    # print(A[p], A[q], A[r])
                    return 1
    return 0

# 100% https://app.codility.com/demo/results/trainingSEZC8Q-C8B/

def solution(A):
    A = sorted(A)
    for i in range(0, len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0

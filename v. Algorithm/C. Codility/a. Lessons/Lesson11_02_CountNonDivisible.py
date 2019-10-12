# 55% https://app.codility.com/demo/results/trainingQJUSUT-CS4/

def solution(A):
    # init vars
    # B = sorted(set(A))
    # N = len(A)
    results = []
    for i in range(0, len(A)):
        result = []
        for j in range(0, len(A)):
            if A[i] % A[j] != 0:
                result.append(A[j])
        results.append(len(result))
    return results

# 55% https://app.codility.com/demo/results/training27ZA3X-PJX/

def solution(A):
    # init vars
    B = sorted(set(A))
    N = len(A)
    M = len(B)
    # algorithm
    results = []
    for i in range(0, N):
        # pick candidate
        C = []
        for j in range(0, M):
            # if divider is bigger, not divisible
            if A[i] < B[j]:
                C.append(B[j])
            elif A[i] % B[j] != 0:
                C.append(B[j])
            else:
                pass
        # find non divider in A
        result = []
        for j in range(0, N):
            if A[j] in C:
                result.append(A[j])
        results.append(len(result))
    return results

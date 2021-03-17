# 87% https://app.codility.com/demo/results/trainingX26ZAW-7FA/
def solution(A, K):
    n = K % len(A)
    if n == 0:
        return A
    else:
        RA = A[len(A) - n:]
        del A[len(A) - n:]
        RA.extend(A)
        return RA

# 12% https://app.codility.com/demo/results/trainingZD8BDA-3FC/

def solution(A, K):
    N = len(A)
    # K < N
    if K < N:
        return A[K-1:] + A[0:K-1]
    # K = N
    elif K == N:
        return A
    # K > N
    else:
        # aN + b = K
        a = (K - (N % K)) / N
        b = N % K
        c = K - b
        return A[c-1:] + A[0:c-1]

# 25% https://app.codility.com/demo/results/trainingUEGC8J-NWR/

def solution(A, K):
    N = len(A)
    # K < N
    if K < N:
        return A[K-1:] + A[0:K-1]
    # K = N
    elif K == N:
        return A
    # K > N
    else:
        # K = aN + b
        b = K % N
        # K = aN
        if b == 0:
            return A
        # K = aN + b
        else:
            c = N - b
            return A[c:] + A[:c]

# 87% https://app.codility.com/demo/results/trainingUHY26M-XXK/

def solution(A, K):
    N = len(A)
    # K = N
    if K == N:
        return A
    # K > N or K < N
    else:
        K = K % N
        return A[-K:] + A[:-K]

# 100% https://app.codility.com/demo/results/trainingEQYCVZ-4JQ/

def solution(A, K):
    N = len(A)
    if N == 0:
        return A
    # K = N
    elif K == N:
        return A
    # K > N or K < N
    else:
        K = K % N
        return A[-K:] + A[:-K]
        
# 2021-03-17-Wed_87% https://app.codility.com/demo/results/trainingHRTEBQ-8QX/ empty array
def solution(A, K):
    K = K % len(A)
    return A[-K:] + A[:-K]

# 2021-03-17-Wed_100% https://app.codility.com/demo/results/trainingAERJWQ-SWE/
def solution(A, K):
    if len(A) == 0:
        return A
    K = K % len(A)
    return A[-K:] + A[:-K]

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

# 2021-03-20-Sat_44% https://app.codility.com/demo/results/trainingMRDFC9-2ET/ Correctness 100%, Performance 0% runtime error O(N * M)
def solution(N, A):
    global result
    result = [0] * N
    def increase(X):
        result[X] += 1

    def max_counter():
        new = max(result)
        for idx in range(len(result)):
            result[idx] = new

    for val in A:
        if val is N + 1:
            max_counter()
        else:
            increase(val-1)
        
    return result

# 2021-03-20-Sat_66% https://app.codility.com/demo/results/trainingM533QS-V2Z/ Correctness 100%, Performance 40% runtime error O(N * M)
def increase(result, x):
    result[x] += 1
    return result

def max_counter(result, N):
    new = max(result)
    del result
    result = [new] * N
    return result

def solution(N, A):
    result = [0] * N
    for val in A:
        if val == N + 1:
            result = max_counter(result, N)
        else:
            result = increase(result, val-1)
    return result

# 2021-03-20-Sat_22% https://app.codility.com/demo/results/training2VSBHR-C2G/ wrong answer, timeout error
def solution(N, A):
    result = [0] * N
    big = 0
    for val in A:
        if val == N + 1:
            result = [big] * N
        else:
            result[val - 1] += 1
            if val >= big:
                big = result[val - 1]
    return result

# 2021-03-20-Thu_88% https://app.codility.com/demo/results/trainingV56EDC-FKB/ O(N+M) timeout error, extreme large, all max_counter operations
def solution(N, A):
    result = [0] * N
    new = 0
    for val in A:
        if val == N + 1:
            result = [new] * N
        else:
            result[val -1] += 1
            if result[val - 1] > new:
                new = result[val - 1]
    return result

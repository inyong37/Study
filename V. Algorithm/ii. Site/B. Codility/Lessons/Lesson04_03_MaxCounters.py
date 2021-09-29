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

# 2021-09-30-Thu, 55%, https://app.codility.com/demo/results/training72KYVC-96A/
def solution(N, A):
    cnt = [0] * N
    max_value = float('-inf')
    for idx, ele in enumerate(A):
        # increase(X) function
        if 1 <= ele and ele <= N:
            cnt[ele-1] += 1
            if max_value < cnt[ele-1]:
                max_value = cnt[ele-1]
        # max counter function
        elif ele == N + 1:
            cnt = [max_value] * N
    return cnt

# 2021-09-30-Thu, 100%, https://app.codility.com/demo/results/training4TMFVN-CZ6/
def solution(N, A):
    cnt = [0] * N
    # temporarly maximum value 'tmp'.
    tmp = 0
    # initiated the maximum value 'val' with 0 due to the smallest value in counters is 0.
    val = 0
    for ele in A:
        # 'increase' operation.
        if 1 <= ele <= N:
            # 'max counter' operation for each elements.
            if cnt[ele - 1] < val:
                cnt[ele - 1] = val
            # normal 'increase' operation.
            cnt[ele - 1] += 1
            # udpate the current maximum value in 'tmp'.
            if cnt[ele - 1] > tmp + val:
                tmp = cnt[ele - 1] - val
        # update the maximum value for 'max counter' oepration.
        elif ele == N + 1:
            val += tmp
            tmp = 0
    # check for not updated after 'max counter' operation.
    for idx, ele in enumerate(cnt):
        if ele < val:
            cnt[idx] = val
    return cnt

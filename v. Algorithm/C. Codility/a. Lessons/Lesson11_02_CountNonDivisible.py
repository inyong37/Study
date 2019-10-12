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

# 100% https://app.codility.com/demo/results/trainingNH2ZFX-BN6/

def solution(A):
    a = max(A)
    # make dictionary for elements and count each elements
    cnt = {}
    for ele in A:
        # make element
        if ele not in cnt:
            cnt[ele] = 1
        # count element
        else:
            cnt[ele] += 1
    
    # make dividor 1 and itself
    div = {}
    for ele in A:
        div[ele] = set([1, ele])
    
    # sieve algorithm
    # divisor
    d = 2
    while d * d <= a:
        # candiate
        can = d
        # check duplicated candidate
        while can <= a:
            if can in div and not d in div[can]:
                div[can].add(d)
                div[can].add(can//d)
                # print(can//d)
            can += d
        d += 1
    
    # pick result from substract dividor from A
    result = [0] * len(A)
    for idx, ele in enumerate(A):
        result[idx] = (len(A) - sum([cnt.get(d, 0) for d in div[ele]]))
        # print(sum(cnt.get(d, 0) for d in div[ele]))
    return result

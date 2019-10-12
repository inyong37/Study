# 55% https://app.codility.com/demo/results/training9DNXE9-ZP2/

def sieve(N):
    semi = []
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False
    
    i = 2
    while i * i <= N:
        if sieve[i] == True:
            for j in range(i * i, N + 1, i):
                sieve[j] = False
        i += 1
    
    i = 2
    while i * i <= N:
        if sieve[i] == True:
            for j in range(i * i, N + 1, i):
                if j % i == 0  and sieve[int(j/i)] == True:
                    semi.append(j)
        i += 1
    
    return semi
    
def solution(N, P, Q):
    semi = sieve(N)
    
    prefix = []
    prefix.append(0)
    prefix.append(0)
    prefix.append(0)
    prefix.append(0)
    prefix.append(1)
    
    for i in range(5, max(Q) + 1):
        if i in semi:
            prefix.append(prefix[-1]+1)
        else:
            prefix.append(prefix[-1])
    
    result = []
    
    for i in range(len(Q)):
        result.append(prefix[Q[i]] - prefix[P[i]-1])
        
    return result

# 66% https://app.codility.com/demo/results/trainingHMBPZJ-ZSB/

import math

def check_semiprime(n):
    cnt = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n /= i
            cnt += 1
        if cnt >= 2:
            break
    if n > 1:
        cnt += 1
    return cnt == 2

def solution(N, P, Q):
    M = len(P)
    result = []
    for i in range(0, M):
        cnt = 0
        for j in range(P[i], Q[i] + 1):
            if check_semiprime(j):
                cnt += 1
        result.append(cnt)
    return result

# 100% https://app.codility.com/demo/results/trainingR6AGKK-CKW/

def solution(N, P, Q):
    # init vars
    M = len(P)
    # filter for divided, 0 = not divided, 1 = divided
    Filter = [0] * (N + 1)
    # check prime from 2
    i = 2
    while i <= N:
        if Filter[i] == 0:
            k = i * i
            while k <= N:
                if Filter[k] == 0:
                    Filter[k] = i
                k += i
        i += 1
    
    cnt = 0
    semi_cnt = [0, 0, 0, 0]
    for i in range(4, N + 1):
        if Filter[i] != 0 and Filter[i//Filter[i]] == 0:
            cnt += 1
        semi_cnt.append(cnt)
    
    sol = []
    for i in range(M):
        sol.append(semi_cnt[Q[i]] - semi_cnt[P[i]-1])
    return sol

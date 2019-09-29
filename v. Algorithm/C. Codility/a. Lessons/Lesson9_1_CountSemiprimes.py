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
            

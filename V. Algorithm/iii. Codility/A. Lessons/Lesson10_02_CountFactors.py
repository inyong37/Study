# 57% https://app.codility.com/demo/results/training8WGCSK-K3F/

def solution(N):
    count = 0
    for i in range(1, N + 1):
        if N % i == 0:
            count += 1
    return count

# 100% https://app.codility.com/demo/results/trainingTACS76-75J/

def solution(N):
    count = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            if i * i == N:
                count += 1
            else:
                count += 2
        i += 1
    return count

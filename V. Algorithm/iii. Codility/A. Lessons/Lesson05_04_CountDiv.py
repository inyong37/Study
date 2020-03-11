# 50% https://app.codility.com/demo/results/trainingCEVM6R-26T/

def solution(A, B, K):
    count = 0
    for i in range(A, B+1):
        if i % K == 0:
            count += 1
        else:
            pass
    return count

# 100% https://app.codility.com/demo/results/training5EEUVS-PAQ/

def solution(A, B, K):
    return (B//K) - ((A-1)//K)

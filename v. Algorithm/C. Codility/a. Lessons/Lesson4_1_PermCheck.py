# 83% https://app.codility.com/demo/results/trainingRDE65Y-7EA/

def solution(A):
    A = sorted(A)
    if A[-1] != len(A):
        return 0
    else:
        return 1

# 100% https://app.codility.com/demo/results/trainingM9DE6F-9XS/

def solution(A):
    A = sorted(A)
    for i in range(0, len(A)):
        if A[i] == i + 1:
            pass
        else:
            return 0
    return 1

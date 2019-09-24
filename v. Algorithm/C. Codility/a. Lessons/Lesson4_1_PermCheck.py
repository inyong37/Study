# 83% https://app.codility.com/demo/results/trainingRDE65Y-7EA/

def solution(A):
    A = sorted(A)
    if A[-1] != len(A):
        return 0
    else:
        return 1

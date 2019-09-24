# https://app.codility.com/demo/results/trainingSEWFXA-6ET/

def solution(A):
    A = sorted(A)
    for i in range(0, len(A)):
        if A[i]+1 != A[i+1]:
            return A[i]+1
        else:
            pass

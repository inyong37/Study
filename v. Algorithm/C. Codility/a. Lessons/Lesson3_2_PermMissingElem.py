# 50% https://app.codility.com/demo/results/trainingSEWFXA-6ET/

def solution(A):
    A = sorted(A)
    for i in range(0, len(A)):
        if A[i]+1 != A[i+1]:
            return A[i]+1
        else:
            pass

# 70% https://app.codility.com/demo/results/trainingPRKTGF-58D/

def solution(A):
    A = sorted(A)
    
    if len(A) == 0:
        return 1
    elif len(A) == 1:
        if A[0] == 1:
            return 2
        elif A[0] == 2:
            return 1
    elif A[-1] != len(A) + 1:
        return len(A) + 1
    else:
        for i in range(0, len(A)):
            if A[i]+1 != A[i+1]:
                return A[i] + 1
            else:
                pass
    return A[-1] + 1

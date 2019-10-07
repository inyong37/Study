# 33% https://app.codility.com/demo/results/training2SZWKV-83Y/

def solution(A):
    value = [0] * (len(A) + 1)
    result = 1
    for i in range(0, len(A)):
        if A[i] <= 0:
            pass
        else:
            value[A[i]-1] = 1
    for i in range(0, len(value)):
        if value[i] == 0:
            return i + 1
    return result

# 100% https://app.codility.com/demo/results/training6QF6JW-JMT/

def solution(A):
    if max(A) < 1:
        return 1
    else:
        A = sorted(set([a for a in A if a > 0]))
        for index, item in enumerate(A):
            if index + 1 != item:
                return index + 1
        return A[-1] + 1

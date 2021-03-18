# 2021-03-18-Wed_63% https://app.codility.com/demo/results/trainingM2ZBQT-2DF/ timeout error O(N**)
def solution(A):
    cnt = 0
    for p in range(len(A)):
        for q in range(len(A[p+1:])):
            if A[p+q+1] < A[p]:
                cnt += 1
    return cnt

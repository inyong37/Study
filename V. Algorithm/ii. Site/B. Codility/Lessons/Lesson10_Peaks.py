# 2021-10-03-Sun, https://app.codility.com/c/run/training5TX2ES-MM5/

def solution(A):
    if len(A) <= 2:
        return 0
    # indexes of peaks
    idxs = []
    for i in range(1, len(A)):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            idxs.append(i)
    
    if len(idxs) == 0:
        return 0
    elif len(idxs) == 1:
        return 1

    # common factors of N
    cs = []
    for i in range(1, len(A)+1):
        if len(A) % i == 0:
            cs.append(i)
    for i in range(len(cs)-1, -1, -1):
        k = len(A) // cs[i]
        for j in range(1, k-1):
            for idx in idxs:
                print(j*k, idx, ((j+1) * k) - 1)
                if idx == 0 or idx  == len(A) - 1:
                    continue
                if j * k <= idx and idx <= ((j+1) * k) - 1:
                    continue
                else:
                    break
        return i
    return 1
    

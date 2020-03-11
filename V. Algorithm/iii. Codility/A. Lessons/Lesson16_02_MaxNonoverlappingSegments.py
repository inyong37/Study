# 100% https://app.codility.com/demo/results/training3KZBC2-YHQ/

def solution(A, B):
    N = len(A)
    # if size of A and B = 0
    if N == 0:
        return 0
    else:
        cnt = 1
        pre_end = B[0]
        for idx in range(1, N):
            # current start point
            cur_sta = A[idx]
            # if current start point is bigger than previous end point, then non overlapping
            if cur_sta > pre_end:
                cnt += 1
                # update end point
                pre_end = B[idx]
            else:
                pass
    return cnt

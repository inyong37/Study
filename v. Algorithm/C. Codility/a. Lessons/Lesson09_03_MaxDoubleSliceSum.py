# 100% https://app.codility.com/demo/results/trainingYZAM28-SXK/

def solution(A):
    # init varialbes
    N = len(A)
    starts = [0] * N
    ends = [0] * N
    # i = Y
    for i in range(1, N - 1):
        # A[X + 1] + ~ + A[Y - 1]
        left = i
        starts[left] = max(starts[left - 1] + A[left], 0)
        # A[Y + 1] + ~ + A[Z - 1]
        right = N - i - 1
        ends[right] = max(ends[right + 1] + A[right], 0)
    return max(starts[i - 1] + ends[i + 1] for i in range(1, N - 1))

# 69% https://app.codility.com/demo/results/training7Y7CDZ-5W2/

def solution(A):
    results = []
    for p in range(0, len(A)):
        for q in range(p, len(A)):
            results.append(sum(A[p:q+1]))
    return max(results)

# 100% https://app.codility.com/demo/results/training2F34SU-CWE/

def solution(A):
    # init variables
    current_sum = total_sum = A[0]
    for i in range(1, len(A)):
        # choose bigger one between current_sum + A[i] and A[i]
        # if A[i] >= 0, pick current_sum + A[i]
        # if A[i] < 0, pick A[i]
        current_sum = max(current_sum + A[i], A[i])
        # choose bigger one between total_sum and current_sum
        # if pre sum is bigger, pick total_sum
        # if now sum is bigger, pick current_sum
        total_sum = max(total_sum, current_sum)
    return total_sum

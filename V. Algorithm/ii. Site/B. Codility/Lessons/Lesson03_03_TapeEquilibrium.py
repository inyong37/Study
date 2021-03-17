# 53% https://app.codility.com/demo/results/training4T8N3D-4NG/

def solution(A):
    result = []
    for p in range(1, len(A)):
        result.append(abs(sum(A[:p]) - sum(A[p:])))
    return min(result)

# 100% https://app.codility.com/demo/results/trainingZP4382-598/

def solution(A):
    front = 0
    rear = sum(A)
    result = None
    for p in range(1, len(A)):
        front += A[p-1]
        rear -= A[p-1]
        diff = abs(front - rear)
        
        if result == None:
            result = diff
        else:
            result = min(result, diff)
    
    return result

# 2021-03-17-Wed_38% https://app.codility.com/demo/results/trainingCQJEZU-AYA/ timeout error
def solution(A):
    diff = []
    for idx in range(len(A)):
        diff.append(abs(sum(A[:idx]) - sum(A[idx:])))
    return min(diff)

# 2021-03-17-Wed_84% https://app.codility.com/demo/results/trainingBAA2H4-WG8/ double, small elements
def solution(A):
    min_val = float('inf')
    sum1, sum2 = 0, sum(A)
    for val in A:
        sum1 += val
        sum2 -= val
        diff = abs(sum1 - sum2)
        if diff < min_val:
            min_val = diff
    return min_val

# 2021-03-17-Wed_84% https://app.codility.com/demo/results/trainingTCDM97-ZME/ double, small elements
def solution(A):
    result = float('inf')
    sum1, sum2 = 0, sum(A)
    for val in A:
        sum1 += val
        sum2 -= val
        result = min(result, abs(sum1 - sum2))
    return result

# 2021-03-17-Wed_84% https://app.codility.com/demo/results/trainingWZ3EZX-46S/ double, small elements
def solution(A):
    front, rear = 0, sum(A)
    result = None
    for val in A:
        front += val
        rear -= val
        if result == None:
            result = abs(front - rear)
        else:
            result = min(abs(front - rear), result)
    return result

# 20% 

def solution(A):
    P_index = [index for index, item in enumerate(A) if item == 0]
    result = 0
    for index, item in enumerate(P_index, 1):
        result += A[index:].count(1)
    
    if result > 1000000000:
        return -1
    
    return result

# 100% https://app.codility.com/demo/results/trainingT8VCR8-83U/

def solution(A):
    result = 0
    count = 0
    for i in A:
        if i == 1 and count == 0:
            continue
        elif i == 0:
            count += 1
        elif i == 1:
            result += count
    
    if result > 1000000000:
        return -1
    
    return result

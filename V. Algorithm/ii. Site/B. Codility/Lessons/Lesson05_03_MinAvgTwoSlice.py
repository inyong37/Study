# 50% https://app.codility.com/demo/results/trainingDQAK42-2JD/

import operator

def solution(A):
    value = []
    result = []
    for p in range(0, len(A)):
        for q in range(p+1, len(A)):
            # print(p, q, sum(A[p:q+1])/(q - p + 1))
            value.append(sum(A[p:q+1])/(q - p + 1))
            result.append(p)
    index, item = min(enumerate(value), key=operator.itemgetter(1))
    return result[index]

# 60% https://app.codility.com/demo/results/trainingX5UR8F-42V/ 

def solution(A):
    result = 0
    value = 100001
    
    for i in range(0, len(A)-1):
        if (A[i] + A[i+1])/2 < value:
            result = i
            value = (A[i] + A[i+1])/2

    for i in range(0, len(A)-2):
        if result < len(A)-2 and (A[i] + A[i+1] + A[i+2])/3 < value:
            result = i
            value = (A[i] + A[i+1] + A[i+2])/3 < value
    
    return result

# 2021-03-21-Sun_50% https://app.codility.com/demo/results/training4N92KD-ESA/ correctness 100%, performance 0%, timeout error
def solution(A):
    result = float('inf')
    idx = 0
    for p in range(len(A)):
        for q in range(p+1, len(A)):
            new = sum(A[p:q+1])/(q-p+1)
            if result > new:
                idx = p
                result = new
    return idx

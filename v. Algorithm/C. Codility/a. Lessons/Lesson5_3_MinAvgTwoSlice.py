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

# 100% https://app.codility.com/demo/results/trainingWU5RRV-JQK/

def solution(K, A):
    count = 0
    total = 0
    for item in A:
        total += item
        if total >= K:
            count += 1
            total = 0
    return count

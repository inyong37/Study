# 55% https://app.codility.com/demo/results/trainingBQQPZY-B57/

def solution(A):
    profits = []
    for i in range(0, len(A)-1):
        for j in range(i, len(A)):
            profits.append(A[j] - A[i])
    profit = max(profits) 
    if profit > 0:
        return profit
    else:
        return 0

# 66% https://app.codility.com/demo/results/trainingRJKAF2-ZRV/

def solution(A):
    if len(A) < 2:
        return 0
    else:
        profits = []
        for i in range(0, len(A)-1):
            for j in range(i, len(A)):
                profits.append(A[j] - A[i])
        profit = max(profits) 
        if profit > 0:
            return profit
        else:
            return 0

# 100% https://app.codility.com/demo/results/trainingCE9EP4-3BP/

def solution(A):
    if len(A) < 2:
        return 0
    else:
        after = A[-1]
        profit = 0
        for i in range(len(A)-2, -1, -1):
            before = A[i]
            profit = max(profit, after - before)
            after = max(before, after)
        return profit

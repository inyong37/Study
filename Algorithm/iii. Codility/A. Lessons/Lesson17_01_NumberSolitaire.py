# 50% https://app.codility.com/demo/results/trainingA9AUDM-J7W/

def solution(A):
    # dice = [1, 2, 3, 4, 5, 6]
    dice = 6
    # total = A[0] + A[-1]
    default = -10001
    solution = [default] * (len(A) + dice)
    solution[dice] = A[0]
    for i in range(dice + 1, len(A) + dice):
        previous = default
        for j in range(dice):
            previous = max(previous, solution[i-j-1])
        solution[i] = A[i-dice] + previous
    return solution[len(A) + dice - 1]

# 100% https://app.codility.com/demo/results/trainingMKPZ2Y-T3Z/

def solution(A):
    # dice = [1, 2, 3, 4, 5, 6]
    dice = 6
    # total = A[0] + A[-1]
    default = -10000000001
    solution = [default] * (len(A) + dice)
    solution[dice] = A[0]
    for i in range(dice + 1, len(A) + dice):
        previous = default
        for j in range(dice):
            previous = max(previous, solution[i-j-1])
        solution[i] = A[i-dice] + previous
    return solution[len(A) + dice - 1]

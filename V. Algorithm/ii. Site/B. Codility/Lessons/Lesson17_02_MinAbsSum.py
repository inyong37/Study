# 27% https://app.codility.com/demo/results/training27XR9Q-8A6/

def solution(A):
    N = len(A)
    val = 0
    #  pick smaller one
    for i in range(0, N):
        val = min(abs(val + A[i]), abs(val - A[i]))
    return val

# 36% https://app.codility.com/demo/results/training5ADC38-SG5/

def solution(A):
    # init variables
    N = len(A)
    val = 0
    A = sorted(A)
    for i in range(N - 1, 0 - 1, -1):
        val = min(abs(val + A[i]), abs(val - A[i]))
    return val
    
# 100% https://app.codility.com/demo/results/trainingFG696A-TWR/

def solution(A):
    # init vars
    N = len(A)
    A = [abs(a) for a in A]
    A = sorted(A)
    S = sum(A)
    # reference
    numbers = {}
    for item in A:
        numbers[item] = numbers.get(item, 0) + 1
    
    possible = [-1] * (S // 2 + 1)
    possible[0] = 0
    
    for number in numbers:
        for trying in range(S // 2 + 1):
            if possible[trying] >= 0:
                possible[trying] = numbers[number]
            elif trying >= number and possible[trying - number] > 0:
                possible[trying] = possible[trying - number] - 1
    
    for halfsum in range(S // 2, -1, -1):
        if possible[halfsum] >= 0:
            return S - halfsum - halfsum

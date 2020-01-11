# 40% https://app.codility.com/demo/results/trainingUNN9KG-CA7/

def solution(N):
    answer = []
    for i in range(1, int(N/2)+1):
        a, b = divmod(N, i)
        if b == 0:
            answer.append(2*(a+i))
    return min(answer)

# 50%  https://app.codility.com/demo/results/training763JYY-NQ8/

def solution(N):
    answer = 4 * N
    for i in range(1, int(N / 2) + 1):
        a, b = divmod(N, i)
        if b == 0:
            if 2 * (i + a) < answer:
                answer = 2 * (i + a)
    return answer

# 100% https://app.codility.com/demo/results/trainingHG4UJW-AZS/

from math import sqrt

def solution(N):
    for i in range(int(sqrt(N)), 0, -1):
        if N % i == 0:
            return int(2 * (N/i + i))
    

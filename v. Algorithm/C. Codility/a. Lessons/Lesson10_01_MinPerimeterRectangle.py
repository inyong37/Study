# 40% https://app.codility.com/demo/results/trainingUNN9KG-CA7/

def solution(N):
    answer = []
    for i in range(1, int(N/2)+1):
        a, b = divmod(N, i)
        if b == 0:
            answer.append(2*(a+i))
    return min(answer)

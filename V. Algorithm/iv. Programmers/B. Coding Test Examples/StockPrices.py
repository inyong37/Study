def solution(prices):
    answer = []
    for i in range(0, len(prices)):
        count = 0
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                count += 1
                break
            else:
                count += 1
        answer.append(count-1)
    return answer

# 100% https://app.codility.com/demo/results/trainingX4V7V5-DR6/

def solution(H):
    count = 0
    stack = []
    for height in H:
        while len(stack) != 0 and stack[-1] > height:
            stack.pop()
        
        if len(stack) != 0 and stack[-1] == height:
            pass
        else:
            count += 1
            stack.append(height)
    return count

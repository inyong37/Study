# 100% https://app.codility.com/demo/results/trainingK7WFRW-RHE/

def solution(A, B):
    fish = 0
    stack = []
    for i in range(0, len(A)):
        if B[i] == 0:
            while len(stack) != 0:
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
            else:
                fish += 1
        else:
            stack.append(A[i])
    fish += len(stack)
    return fish

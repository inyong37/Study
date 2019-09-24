# 54% https://app.codility.com/demo/results/trainingP7F727-5EB/

def solution(X, A):
    check = int(X*(X+1)/2)
    walk = []
    for index, item in enumerate(A):
        if item in walk:
            pass    
        else:
            walk.append(item)
            if sum(walk) == check:
                return index
            else:
                pass
    return -1

# 100% https://app.codility.com/demo/results/trainingYRFX8E-VJ9/

def solution(X, A):
    check = [0] * X
    count = 0
    for i in range(0, len(A)):
        if check[A[i]-1] == 0:
            check[A[i]-1] = 1
            count += 1
            if count == X:
                return i
    return -1

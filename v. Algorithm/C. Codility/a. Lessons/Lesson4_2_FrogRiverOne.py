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

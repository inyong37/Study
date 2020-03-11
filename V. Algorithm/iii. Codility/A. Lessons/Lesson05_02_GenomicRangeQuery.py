# 62% https://app.codility.com/demo/results/training9PPURU-5A5/

def solution(S, P, Q):
    result = []
    for i in range(0, len(P)):
        value = []
        string = [item for index, item in enumerate(S) if index >= P[i] and index <= Q[i]]
        for j in string:
            if j == 'A':
                value.append(1)
            elif j == 'C':
                value.append(2)
            elif j == 'G':
                value.append(3)
            else:
                value.append(4)
        result.append(min(value))
    return result

# 62% https://app.codility.com/demo/results/trainingD7MJSX-FCM/

def solution(S, P, Q):
    result = []
    for i in range(0, len(P)):
        value = []
        string = sorted(set([item for index, item in enumerate(S) if index >= P[i] and index <= Q[i]]))
        for j in string:
            if j == 'A':
                value.append(1)
                break
            elif j == 'C':
                value.append(2)
            elif j == 'G':
                value.append(3)
            else:
                value.append(4)
        result.append(min(value))
    return result

# 2020-03-30-Mon

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif i == len(arr):
            if arr[i] == arr[i-1]:
                pass
            else:
                answer.append(arr[i])
        else:
            if arr[i] == arr[i-1]:
                pass
            else:
                answer.append(arr[i])
    return answer

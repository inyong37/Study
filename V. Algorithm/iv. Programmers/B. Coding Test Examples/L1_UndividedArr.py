# 2020-04-03-Fri

def solution(arr, divisor):
    d = dict()
    answer = list()
    for index, item in enumerate(arr):
        value = item % divisor
        d[str(item)] = value
        if value == 0:
            answer.append(item)
        else:
            pass
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)

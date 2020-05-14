n = int(input())
cnt = 0
results = [n]


def dp(arr):
    result = []
    for itm in arr:
        result.append(itm-1)
        if itm % 3 == 0:
            result.append(itm/3)
        if itm % 2 == 0:
            result.append(itm/2)
    result = list(set(result))
    return result


while True:
    if n == 1:
        print(cnt)
        break
    tmp = results[:]
    results = dp(tmp)
    cnt += 1
    if min(results) == 1:
        print(cnt)
        break

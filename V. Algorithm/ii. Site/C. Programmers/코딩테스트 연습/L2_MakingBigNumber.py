# 2020-04-19-Sun


# Try 1

from itertools import permutations

def solution(number, k):
    permute = list(permutations(number, len(number) - k))
    answer = str(max(permute))
    return answer

# Try 2

def solution(number, k):
    ans = list()
    for idx, itm in enumerate(number):
        while ans and ans[-1] < itm and k > 0:
            ans.pop()
            k -= 1
        if k == 0:
            ans += number[idx:]
            break
        ans.append(itm)
    if k > 0:
        ans = ans[:-k]
    else:
        pass
    return ''.join(ans)

# Reference: https://gurumee92.tistory.com/162

# Try 1

def solution(n):
    notation = '412'
    def change(number, base):
        q, r = divmod(number, base)
        k = notation[r]
        return change(q, base) + k if q else k
    return change(n, 3)

# Try 2

def solution(n):
    answer = str()
    while n:
        n, a = divmod(n, 3)
        answer = '412'[a] + answer
        if not a:
            n -= 1
    return answer

# Reference: https://itholic.github.io/kata-124-world/

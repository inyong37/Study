# Try 1

def solution(n):
    notation = '412'
    def change(number, base):
        q, r = divmod(number, base)
        k = notation[r]
        return change(q, base) + k if q else k
    return change(n, 3)

# Try 2

# 2021-03-20-Sat_28% https://app.codility.com/demo/results/training8Z28XK-EGN/ wrong anwser, runtime error
def solution(s):
    if len(s) == 0 or len(s) == 1:
        return 0
    elif len(s) // 2 == 0: 
        return -1
    left = list(s[:len(s)//2])
    right = list(s[len(s)//2+1:])
    left.reverse()
    if left == right:
        return len(left)

# 2021-03-20-Sat_100% https://app.codility.com/demo/results/trainingHX5RRF-KRH/
def solution(S):
    if len(S) == 0:
        return -1
    elif len(S) == 1:
        return 0
    elif len(S) // 2 == 0:
        return -1
    idx = len(S)//2
    left = list(S[:idx])
    right = list(S[idx+1:])
    if left[::-1] == right:
        return len(S)//2
    return -1

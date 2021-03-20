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

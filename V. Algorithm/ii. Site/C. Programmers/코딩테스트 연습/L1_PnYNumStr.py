# 2020-04-03-Fri

def solution(s):
    p, y = 0, 0
    for c in s:
        if c is 'p' or c is 'P':
            p += 1
        elif c is 'y' or c is 'Y':
            y += 1
        else:
            pass
    if p != y:
        return False
    else:
        return True

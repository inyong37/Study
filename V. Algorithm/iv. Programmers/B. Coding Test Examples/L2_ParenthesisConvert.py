# 2020-04-18-Sat

# balanced string
def balance(string):
    cnt = 0
    tmp = list()
    for idx, item in enumerate(string):
        if item == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return idx
        else:
            pass


# righted string
def right(string):
    tmp = list()
    for cnt in string:
        if cnt == '(':
            tmp.append(cnt)
        else:
            if len(tmp) == 0:
                return False

            tmp.pop()
    if len(tmp) != 0:
        return False
    else:
        pass
    return True
    
# Recursive solution
def solution(p):
    if p == '':
        return p
    elif right(p):
        return p
    else:
        u, v = p[:balance(p)+1], p[balance(p)+1:]
        if right(u):
            string = solution(v)
            return u + string
        else:
            tmp = '('
            tmp += solution(v)
            tmp += ')'
            u = list(u[1:-1])
            for idx in range(len(u)):
                if u[idx] == '(':
                    u[idx] = ')'
                else:
                    u[idx] = '('
            tmp += ''.join(u)
            return tmp

# Reference: https://inspirit941.tistory.com/m/104

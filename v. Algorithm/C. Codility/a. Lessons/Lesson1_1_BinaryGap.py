def solution(N):
    
    N = bin(N)[2:]
    
    pos = []
    for idx, item in enumerate(N):
        if item is '1':
            pos.append(idx)
    
    cal = []
    for i in range(0, len(pos)-1):
        cal.append(pos[i+1] - pos[i] - 1)
    
    if len(cal) == 0:
        return 0
    else:
        return max(cal)

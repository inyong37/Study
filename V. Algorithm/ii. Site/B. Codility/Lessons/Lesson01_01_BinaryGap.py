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

# 2021-03-17-Wed_100%
def solution(N: int) -> int:
    num = list(map(int, format(N, 'b'))) # the binary number of N
    idx = [] # the positions of 1 in binary number of N
    for i in range(len(num)):
        if num[i] == 1:
            idx.append(i)
    results = [0] # the differences of positions
    for i in range(len(idx) - 1):
        results.append(idx[i + 1] - idx[i] - 1)
    return max(results)

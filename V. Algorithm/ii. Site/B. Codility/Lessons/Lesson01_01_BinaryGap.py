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

# 2021-03-17-Wed_100% https://app.codility.com/demo/results/trainingQSRZAS-JGP/
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

# 2021-10-02-Sat, 100%, https://app.codility.com/demo/results/trainingWR3MAQ-82R/

def solution(N):
    ans = 0
    num = str(bin(N)[3:])
    cnt = 0
    for ele in num:
        if ele == '1':
            ans = max(cnt, ans)
            cnt = 0
        else:
            cnt += 1
    return ans

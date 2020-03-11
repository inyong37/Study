# 30% https://app.codility.com/demo/results/trainingU2H33S-NQ2/

def solution(M, A):
    # init vars
    N = len(A)
    cnt = 0
    ele = 0
    slc = []
    
    for idx in range(0, N):
        if len(slc) == 0:
            slc.append(A[idx])
            cnt += 1
            ele += 1
            # print(slc, cnt, ele)
        else:
            if A[idx] not in slc:
                slc.append(A[idx])
                cnt += 1
                cnt += ele
                ele += 1
                # print(slc, cnt, ele)
            elif A[idx] in slc:
                cnt += 1
                ele = 1
                slc = []
                slc.append(A[idx])
                # print(slc, cnt, ele)
    return cnt

# 0% https://app.codility.com/demo/results/training6UX37J-DWB/

def solution(M, A):
    N = len(A)
    slc = []
    cnt = 1
    for idx in range(0, N):
        # start distinct slice
        if len(slc) == 0:
            slc.append(A[idx])
        else:
            if A[idx] in slc:
                # plus count
                plus = 1
                for i in range(1, len(slc)+1):
                    plus *= i
                cnt += plus
                # clean distinct slice
                slc = []
                slc.append(A[idx])
            else:
                slc.append(A[idx])
    
    # plus count
    plus = 1
    for i in range(1, len(slc)+1):
        plus *= i
    cnt += plus
        
    return cnt

# 100% https://app.codility.com/demo/results/trainingP8E4A5-CPC/

def solution(M, A):
    # init vars
    the_sum = 0
    front = 0
    back = 0
    # check seen
    seen = [False] * (M + 1)
    # check from front and back
    while (front < len(A) and back < len(A)):
        # front and unseen, check 
        while (front < len(A) and seen[A[front]] != True):
            the_sum += (front - back + 1)
            seen[A[front]] = True
            front += 1
        else:
            # make seen to unseen
            while (front < len(A) and back < len(A) and A[back] != A[front]):
                seen[A[back]] = False
                back += 1
            # make seen to unseen
            seen[A[back]] = False
            back += 1
    
    return min(the_sum, 10**9)

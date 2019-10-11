# 33% https://app.codility.com/demo/results/trainingPSEVQW-2HU/

def solution(A):
    result = 0
    for i in range(0, len(A)-1):
        left = A[0:i+1]
        right = A[i+1:]
        
        # get left leader
        l = ''
        cnt = 0
        for val in left:
            if l == '':
                l = val
                cnt = 1
            else:
                if val != l:
                    cnt -= 1
                    if cnt == 0:
                        l = ''
                else:
                    cnt += 1
        
        # get right leader  
        r = ''
        cnt = 0
        for val in right:
            if r == '':
                r = val
                cnt = 1
            else:
                if val != r:
                    cnt -= 1
                    if cnt == 0:
                        r = ''
                else:
                    cnt += 1
        
        
        if l == r:
            result += 1
        else:
            pass
    
    return result

# 100% https://app.codility.com/demo/results/training96ZPJ2-YVE/

def solution(A):
    # find leader
    ele = ''
    cnt = 0
    for val in A:
        # ele init
        if ele == '':
            ele = val
            cnt = 1
        else:
            if val != ele:
                cnt -= 1
                # ele init
                if cnt == 0:
                    ele = ''
            else:
                cnt += 1
    
    # if ele is none
    if cnt == 0:
        return 0
    
    # find i (last index)
    cnt = 0
    i = 0
    for idx, val in enumerate(A):
        if val == ele:
            cnt += 1
            i = idx
    
    # ?
    if cnt < len(A)//2:
        return 0
    
    result = 0
    left = 0
    for idx, val in enumerate(A):
        if val == ele:
            left += 1
        if left > (idx + 1)//2  and cnt - left > (len(A) - idx - 1)//2:
            result += 1
    
    return result


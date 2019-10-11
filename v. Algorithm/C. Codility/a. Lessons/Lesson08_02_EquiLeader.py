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


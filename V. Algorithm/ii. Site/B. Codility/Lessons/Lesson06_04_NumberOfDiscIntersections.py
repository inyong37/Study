# 100% https://app.codility.com/demo/results/trainingDWSUCS-N86/

def solution(A):
    large = []
    small = []
    for index, item in enumerate(A):
        large.append(index + item)
        small.append(index - item)
    
    large = sorted(large)
    small = sorted(small)
    
    i = 0
    count = 0
    for index, item in enumerate(large):
        while i < len(large) and item >= small[i]:
            count += i - index
            i += 1
        
        if count > 10**7:
            return -1
    
    return count
    '''
    count = 0
    for index, item in enumerate(large):
        for i in range(0, len(large)):
            if item >= small[i]:
                count += i - index
            else:
                pass
        if count > 10**7:
            return -1
    return count
    '''

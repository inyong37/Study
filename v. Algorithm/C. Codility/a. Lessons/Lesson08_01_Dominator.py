# 8% https://app.codility.com/demo/results/trainingBFQ3BM-FXW/

from collections import Counter

def solution(A):
    result = Counter(A)
    items = []
    counts = []
    for index, item in enumerate(result):
        items.append(item)
        counts.append(result[item])
    
    if max(counts) <= len(A)/2:
        return -1
    else:
        # indexes = []
        for index, item in enumerate(A):
            if item == items[0]:
                # indexes.append(index)
                return index
        # return indexes

# 100% https://app.codility.com/demo/results/trainingU9F45X-KWV/

def solution(A):
    ele = ''
    cnt = 0
    # pick ele
    for value in A:
        # ele init
        if ele == '':
            ele = value
            cnt = 1
        else:
            if value != ele:
                cnt -= 1
                # ele init
                if cnt == 0:
                    ele = ''
            else:
                cnt += 1
    if cnt == 0:
        return -1
    
    # collect idx
    cnt = 0
    idx = 0
    for i, value in enumerate(A):
        if value == ele:
            cnt += 1
            idx = i
    
    if cnt > len(A)//2:
        # print(idx)
        return idx
    
    return -1

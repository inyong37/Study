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


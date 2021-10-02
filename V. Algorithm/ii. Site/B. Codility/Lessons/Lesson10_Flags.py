# 2021-09-30-Thu, 20%, https://app.codility.com/demo/results/trainingM9VSF4-K9W/

def solution(A):
    # list of peaks.
    peaks = []
    val = 1
    for i in range(1, len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks.append(i)
    # if there is not peak as uphill or downhill.
    if not peaks:
        return 0
    # if number of peaks is 1, return 1 without checking K limitation.
    elif len(peaks) == 1:
        return 1
    # check for flags as number of peaks.
    for i in range(2, len(peaks)+1):
        cnt = 0
        for j in range(1, len(peaks)):
            # check distance is farther than number of flags: |P-Q| >= K.
            if peaks[j] - peaks[j-1] >= i:
                cnt += 1
        if cnt > val:
            val = cnt
    return val

# 2021-09-30-Thu, 26%, https://app.codility.com/demo/results/trainingBD285A-SW2/

def solution(A):
    peaks = []
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            peaks.append(i)
    if not peaks:
        return 0
    if len(peaks) == 1:
        return 1
    val = 1
    for i in range(2, len(peaks)+1):
        cnt = 0
        for j in range(0, len(peaks)-1):
            if abs(peaks[j] - peaks[j+1]) >= i:
                cnt += 1
            if cnt > i:
                break
        if cnt > val:
            val = cnt
    return val

# 2021-09-30-Thu, 6%, https://app.codility.com/demo/results/trainingWRA7DP-A22/

def solution(A):
    if len(A) < 3:
        return 0
    peaks = []
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            peaks.append(i)
    if len(peaks) == 1:
        return 1
    val = 1
    for k in range(2, len(peaks)+1):
        cnt = 0
        i = 0
        while i < len(peaks) - 1:
            for j in range(i, len(peaks)):
                if peaks[j] - peaks[i] >= k:
                    cnt += 1
                    i = j
                    break
        if cnt > val:
            val = cnt
        if cnt < val:
            return  val
    return val

# 2021-09-30-Thu, 66%, https://app.codility.com/demo/results/training76Q28Q-U9G/

def solution(A):
    # list of peaks.
    peaks = []
    for i in range(1, len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks.append(i)
    # if there is not peak as uphill or downhill.
    if not peaks:
        return 0
    # if number of peaks is 1, return 1 without checking K limitation.
    elif len(peaks) == 1:
        return 1
    val = 1
    for k in range(2, len(peaks)+1):
        p = 0
        q = 1
        # initiated with first peak flag.
        flag = 1
        while p < len(peaks) - 1:
            if peaks[q] - peaks[p] >= k:
                flag += 1
                p = q
                q += 1
            else:
                q += 1
            if q == len(peaks) or flag == k:
                break
        if flag < val:
            return val
        val = max(flag, val)
    return val

# 2021-09-30-Thu, 66%, https://app.codility.com/demo/results/trainingVN3PAX-2VB/

import math

def solution(A):
    # list of peaks.
    peaks = []
    for i in range(1, len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks.append(i)
    # if there is not peak as uphill or downhill.
    if not peaks:
        return 0
    # if number of peaks is 1, return 1 without checking K limitation.
    elif len(peaks) == 1:
        return 1
    val = 1
    k_max = int((math.sqrt(4*(peaks[-1] - peaks[0]) + 1) + 1) / 2) + 1
    for k in range(2, k_max):
        p = 0
        q = 1
        # initiated with first peak flag.
        flag = 1
        while p < len(peaks) - 1:
            if peaks[q] - peaks[p] >= k:
                flag += 1
                p = q
                q += 1
            else:
                q += 1
            if q == len(peaks) or flag == k:
                break
        if flag < val:
            return val
        val = max(flag, val)
    return val

# 2021-10-02-Sat, 40%, https://app.codility.com/demo/results/trainingA35YEG-H8K/

from math import sqrt

def solution(A):
    if len(A) <= 2:
        return 0
    
    peaks = []
    for i in range(1, len(A)):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            peaks.append(i)
    
    if not peaks:
        return 0
    
    if len(peaks) <= 2:
        return 2
    
    max_flags = int(sqrt(peaks[-1] - peaks[0])) + 1

    for i in range(max_flags, 0, -1):
        cnt = 1
        cur = peaks[0]
        for j in range(1, len(peaks)):
            if cur + i <= peaks[j]:
                cur = peaks[j]
                cnt += 1
        if cnt >= i:
            return i
    return 2

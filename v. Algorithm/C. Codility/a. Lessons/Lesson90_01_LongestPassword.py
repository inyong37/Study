# 100% https://app.codility.com/demo/results/trainingCHD63V-BTF/

def solution(S):
    strings = S.split(' ')
    words = []
    lengths = []
    for string in strings:
        if string.isalnum():
            a = 0
            b = 0
            for i in string:
                if i.isalpha():
                    a += 1
                elif i.isdigit():
                    b += 1
            if a % 2 == 0 and b % 2 == 1:
                words.append(string)
                lengths.append(len(string))
    if lengths:
        return max(lengths)
    else:
        return -1
        

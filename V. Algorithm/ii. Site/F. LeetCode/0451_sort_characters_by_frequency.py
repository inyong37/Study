from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        cnts = Counter(s)
        # for order
        l = len(cnts)
        cnts = cnts.most_common(l)
        # sorted string
        s = str()
        for (key, val) in cnts:
            s += str(key)*val
        return s

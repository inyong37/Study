# 2020-04-07-Tue
# Combination nCr = n!/((n-r)!*r!)

def Combination(array, r):
    array = sorted(array)
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return
        start = array.index(chosen[-1]) + 1 if chosen else 0
        for next in range(start, len(array)):
            chosen.append(array[next])
            generate(chosen)
            chosen.pop()
    generate([])

# Reference: https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations

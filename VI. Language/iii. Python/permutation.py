# 2020-04-07-Tue
# Permutation: nPr = n!/(n-r)!

def Permutation(array, r):
    array = sorted(array)
    used = [0 for _ in range(len(array))]
    def generate(chosen, used):
    if len(chosen) == r:
        print(chosen)
        return
        for i in range(len(arr)):
            if not used[i]:
            chosen.append(arr[i])
            used[i] = 1
            generate(chosen, used)
            used[i] = 0
            chosen.pop()
    generate([], used)

#  Reference: https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations

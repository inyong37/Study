n = int(input())
arr = [0, 1, 3]

for i in range(3, n + 1):
    arr.append(2 * arr[i-2] + arr[i-1])
print(arr[n] % 10007)
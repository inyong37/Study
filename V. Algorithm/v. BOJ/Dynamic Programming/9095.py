arr = [1, 2, 4]
for i in range(3, 11):
    arr.append(arr[i-3] + arr[i-2] + arr[i-1])

t = int(input())
for i in range(t):
    k = int(input())
    print(arr[k-1])

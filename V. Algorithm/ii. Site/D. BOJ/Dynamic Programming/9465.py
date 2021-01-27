n = int(input())
for i in range(n):
    s = []
    n = int(input())
    for k in range(2):
        s.append(list(map(int, input().split())))
    s[0][1] += s[1][0]
    s[1][1] += s[0][0]
    for j in range(2, n):
        s[0][j] += max(s[1][j-1], s[1][j-2])
        s[1][j] += max(s[0][j-1], s[0][j-2])
    print(max(s[0][n-1], s[1][n-1]))

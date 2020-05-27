# n = 0: cnt = 0
# n = 1: 1 cnt = 1
# n = 2: 10 cnt = 1
# n = 3: 100, 101 cnt = 2
# n = 4: 1010, 1001, 1000 cnt =3
# n = 5: 10000, 10001, 10010, 10101, 10100 cnt =5
n = int(input())
dp = [0, 1, 1]
for i in range(3, n+1):
    dp.append(dp[i-2] + dp[i-1])
print(dp[n])

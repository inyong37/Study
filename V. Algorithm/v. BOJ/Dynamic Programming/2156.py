n = int(input())
amount = [int(input()) for _ in range(n)]
dp = list()
dp.append(0)
dp.append(amount[0])
if n > 1:
    dp.append(amount[0] + amount[1])

for i in range(3, n + 1):
    case_1 = amount[i-1] + dp[i-2]
    case_2 = amount[i-1] + amount[i-2] + dp[i-3]
    case_3 = dp[i-1]
    dp.append(max(case_1, case_2, case_3))

print(dp[n])

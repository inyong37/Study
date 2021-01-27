board1 = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board2 = [[0,0,1,1],[1,1,1,1]]


def solution4(board):
    row = len(board)
    col = len(board[0])
    dp = [[0 for i in range(col + 1)] for j in range(row + 1)]
    ans = 0
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if board[i-1][j-1] != 0:
                dp[i][j] = min(dp[i-1][j], min(dp[i][j-1], dp[i-1][j-1])) + 1
                ans = max(ans, dp[i][j])
    return ans * ans


land1 = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]


def solution5(land):
    dp = [[0 for i in range(4)] for j in range(len(land) + 1)]
    for i in range(0, 4):
        dp[0][i] = land[0][i]

    for i in range(1, len(land)):
        for j in range(0, 4):
            for k in range(0, 4):
                if j != k:
                    dp[i][j] = max(dp[i][j], land[i][j] + dp[i-1][k])
    ans = 0
    for i in range(0, 4):
        ans = max(ans, dp[len(land)-1][i])
    return ans


sticker1 = [14, 6, 5, 11, 3, 9, 2, 10]
stikcer2 = [1, 3, 2, 5, 4]


def solution6(sticker):
    dp1 = [0 for i in range(len(sticker) + 1)] # 첫 번째 스티커를 뜯은 경우
    dp2 = [0 for i in range(len(sticker) + 1)] # 첫 번쨰 스티커를 뜯지 않은 경우
    n = len(sticker)
    if n == 1:
        return sticker[0]
    # 첫 번째 스티커를 뜯은 경우
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    for i in range(2, len(sticker) -1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    # 첫 번째 스티커를 뜯지 않은 경우
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    return max(dp1[n-2], dp2[n-1])


import math

str1 = ['ba','na','n','a']
t1 = 'banana'
str2 = ['app','ap','p','l','e','ple','pp']
t2 = 'apple'
str3 = ['ba','an','nan','ban','n']
t3 = 'banana'

def solution7(strs, t):
    dp = [987654321] * 20002
    dp[len(t)] = 0
    for i in range((len(t) - 1), 0):
        tmp = ''
        j = 0
        while j < 5 and i + j < len(t):
            tmp += t[i+j]
            if strs.index(tmp) != strs[-1] and dp[i + j + 1] != 987654321:
                dp[i] = min(dp[i], dp[i + j + 1] + 1)
            j += 1

    if dp[0] == 987654321:
        return -1
    return dp[0]

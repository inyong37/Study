def solution(m, n, puddles):
    table = [[1 if i == 1 else 0 for i in range(m + 1)] if j != 1 else [1 for _ in range(m + 1)] for j in range(n + 1)]
    table[1][0] = 0
    table[0][1] = 0
    for [i, j] in puddles:
        table[i][j] = -1
    for i in range(2, n + 1):
        for j in range(2, m + 1):
            if table[i][j] == -1:
                table[i][j] = 0
            elif table[i][j-1] == -1:
                table[i][j] = table[i-1][j]
            elif table[i-1][j] == -1:
                table[i][j] = table[i][j-1]
            else:
                table[i][j] = table[i-1][j] + table[i][j-1]
    return table[n][m]

def solution(m, n, puddles):
    table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    table[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                table[i][j] = 0
            else:
                table[i][j] = table[i-1][j] + table[i][j-1]
    return table[n][m] % 1000000007

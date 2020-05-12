n = int(input())
for i in range(0, n-1):
    print(' ' * i + '*' * (2 * (n - i) - 1))
for i in range(n, 0, -1):
    print(' ' * (i - 1) + '*' * (2 * (n - i) + 1))
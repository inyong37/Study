day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
x, y = map(int, input().split())
days = int()
d31 = [1, 3, 5, 7, 8, 10, 12]
d30 = [4, 6, 9, 11]
d28 = [2]
for i in range(x):
    if i in d31:
        days += 31
    elif i in d30:
        days += 30
    else:
        days += 28
days += y
print(day[(days % 7) - 1])
# 2020-04-01-Wed

def solution(a, b):
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = {'1': 31, '2': 29, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    totalDays = b
    for i in range(a-1):
        totalDays += months[str(i+1)]
        # print(months[str(i+1)])
    # print(totalDays)
    answer = days[(totalDays%7)-1]
    return answer

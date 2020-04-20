# 2020-04-20-Mon

def solution(people, limit):
    people.sort() # sort small > big
    cnt = 0
    ldx = 0 # light index
    hdx = len(people) - 1 # heavy index
    while ldx < hdx:
        if people[ldx] + people[hdx] <= limit:
            cnt += 1
            ldx += 1
            hdx -= 1
        else:
            hdx -= 1
    return len(people) - cnt

# Reference: https://codedrive.tistory.com/46

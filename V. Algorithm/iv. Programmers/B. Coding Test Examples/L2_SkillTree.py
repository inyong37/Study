# 2020-04-16-Thu

# Try 1-28.6 / 100.0

def solution(s, sts):
    # input  : s (skill), sts (skill_trees)
    # output : cnt (correct skill_trees)
    cnt = 0
    for i in sts:
        cmp = ''
        for idx, item in enumerate(i):
            
            if item not in s:
                pass
            else:
                cmp += item
        for j in range(len(cmp)):
            if cmp[j] == s[j]:
                # print('==', j, cmp[j], s[j])
                pass
            else:
                # print('!=', j, cmp[j], s[j])
                break
            if j == len(cmp)-1:
                cnt += 1
            print(cnt)
    return cnt

# Try 2

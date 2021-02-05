# 2020-04-16-Thu

# Try 1

from string import ascii_uppercase

def solution(nam):
    # input  : nam (name)
    # output : cnt (count to make name)
    alp = list(ascii_uppercase) # alphabet list
    now = alp[0]                # now alphabet
    idx = 0                     # now index
    cnt = 0
    lng = 25                    # length of alphabet list
    haf = 13                    # half length
    for c in nam:
        nxt = alp.index(c)      # next index
        if  abs(nxt - idx) > haf:
            cnt += idx + lng - nxt
            print('big', idx + lng - nxt, cnt)
        else:
            cnt += abs(nxt - idx)
            print('small', nxt - idx, cnt)
        idx = nxt  
        now = alp[idx]
        print(cnt, now)
        cnt += 1
    return cnt

# Try 2

from string import ascii_uppercase

def solution(nam):
    # input  : nam (name)
    # output : cnt (count to make name)
    alp = list(ascii_uppercase) # alphabet list
    nam = list(nam)
    now = alp[0] * len(nam)     # now alphabet
    cnt = 0
    idx = 0
    lng = 26                    # length of alphabet
    haf = 13                    # half length
    while True:
        
        if nam[idx] != alp[0]:
            if idx > 13:
                cnt += 26 - idx
            else:
                cnt += idx
            nam[idx] = 'A'
        
        ridx = 1
        lidx = 1
        
        if now == nam:
            break
        else:
            for i in range(1, len(nam)):
                if nam[idx+1] == 'A':
                    ridx += 1
                else:
                    break
                if nam[idx-1] == 'A':
                    lidx += 1
                else:
                    break
            if ridx > lidx:
                cnt += lidx
                idx -= ridx
            else:
                cnt += ridx
                idx == ridx
    return cnt

# Try 3

def solution(name):
    answer = 0
    name=list(name)
    index=0
    while(True):
        right=1
        left=1
        if name[index] != 'A': 
            updown = min(ord(name[index])-ord('A'),(ord('Z')-ord(name[index])+1))
            answer += updown
        name[index] = 'A'
        if name == ["A"]*len(name): break
        for i in range(1,len(name)):
            if name[index+i]=="A": right+=1
            else: break
        for i in range(1,len(name)):
            if name[index-i]=="A": left+=1
            else: break
        if right>left:
            answer+=left
            index-=left
        else:
            answer+=right
            index+=right
    return answer

# Reference: http://blog.naver.com/PostView.nhn?blogId=jaeyoon_95&logNo=221740770765&categoryNo=74&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView

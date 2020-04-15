# 2020-04-15-Wed

# Try 1

def solution(bl, w, tws):
    # input  = bl (bridge_length), w (weight), tws (truck_weights)
    # output = t  (time)
    t = 0
    on = dict() # ln bridge truck
    while tws:
        print(sum(on.keys()))
        if sum((on.keys())) < w:
            key =  tws.pop()
            value = bl
            on[key] = int(value)
            print('under', key, value, on)
        else:
            for key in on.keys():
                if on[key] < bl:
                    on[key] -= 1
                else:
                    pass
            print('over')
        t += 1
    return t

# Try 2-92.9/100.0 case 5: time out

def solution(bl, w, tws):
    # input  = bl (bridge_length), w (weight), tws (truck_weights)
    # output = t  (time)
    t = 0
    on = [0] * bl # bridge
    while on:
        on.pop(0) # out
        if tws: # truck remain 
            if sum(on) + tws[0] <= w:
                on.append(tws.pop(0)) # truck in
            else:
                on.append(0) # nothing in
        t += 1
    return t

# Reference: https://mentha2.tistory.com/16

#  Try 3-92.9/100.0 case 5: time out

def solution(bl, w, tws):
    # input  = bl (bridge_length), w (weight), tws (truck_weights)
    # output = t  (time)
    tws = tws[::-1]
    t = 0
    on = [0] * bl # bridge
    while on:
        on.pop(0) # out
        if tws: # truck remain 
            if sum(on) + tws[-1] <= w:
                on.append(tws.pop()) # truck in
            else:
                on.append(0) # nothing in
        t += 1
    return t

# Try 4-92.9/100.0 case 5: time out

from collections import deque

def solution(bl, w, tws):
    # input  = bl (bridge_length), w (weight), tws (truck_weights)
    # output = t  (time)
    tws = tws[::-1]
    t = 0
    on = deque([0] * bl) # bridge
    while on:
        on.popleft() # out
        if tws: # truck remain 
            if sum(on) + tws[-1] <= w:
                on.append(tws.pop()) # truck in
            else:
                on.append(0) # nothing in
        t += 1
    return t

# Try 5-92.9/100.0 case 5: time out

from collections import deque

def solution(bl, w, tws):
    # input  = bl (bridge_length), w (weight), tws (truck_weights)
    # output = t  (time)
    tws = tws[::-1]
    t = 0
    on = deque([0] * bl) # bridge
    while on:
        on.pop() # out
        if tws: # truck remain 
            if sum(on) + tws[-1] <= w:
                on.appendleft(tws.pop()) # truck in
            else:
                on.appendleft(0) # nothing in
        t += 1
    return t

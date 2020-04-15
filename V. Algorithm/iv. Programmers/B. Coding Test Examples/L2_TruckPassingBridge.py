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

# Try 2

def solution(bl, w, tws):
    # input  = bl (bridge_length), w (weight), tws (truck_weights)
    # output = t  (time)
    t = 0
    on = [0] * bl
    while on:
        on.pop(0)
        if tws:
            if sum(on) + tws[0] <= w:
                on.append(tws.pop(0))
            else:
                on.append(0)
        t += 1
    return t

# Reference: https://mentha2.tistory.com/16

def solution(routes):
    routes.sort()
    pos = routes[0][1]
    camera_cnt = 1
    for i in range(len(routes)-1):
        if routes[i][1] < pos:
            pos = routes[i][1]
        if pos < routes[i+1][0]:
            pos = routes[i+1][1]
            camera_cnt += 1
    return camera_cnt

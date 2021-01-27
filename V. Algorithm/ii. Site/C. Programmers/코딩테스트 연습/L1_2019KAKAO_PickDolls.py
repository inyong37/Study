# 2020-03-31-Tue
# Try 1 90/100

import numpy as np

def solution(board, moves):
    # 파=1, 노=2, 초=3, 핑=4, 갈=5
    # [1,5,3,5,1,2,1,4] = 핑, 초, 파, 파, 초, 노, 0, 핑 = 4, 3, 1, 1, 3, 2, 0, 4
    game = np.array(board).T
    picks = list()
    answer = 0
    for i, move in enumerate(moves):
        pick = 0
        for k, j in enumerate(game[move-1]):
            # pick 
            if pick == 0:
                if j != 0:
                    pick = j
                    game[move-1][k] = 0
                else:
                    pass
            else:
                pass
        # picks
        if i == 0:
            picks.append(pick)            
        else:
            if pick == 0:
                pass
            elif pick == picks[-1]:
                answer += 2
                picks.pop()
            else:
                picks.append(pick)
    return answer

# 2020-04-01-Wed
# Try 2 100%
import numpy as np

def solution(board, moves):
    # 파=1, 노=2, 초=3, 핑=4, 갈=5
    # [1,5,3,5,1,2,1,4] = 핑, 초, 파, 파, 초, 노, 0, 핑 = 4, 3, 1, 1, 3, 2, 0, 4
    game = np.array(board).T
    picks = list()
    answer = 0
    for i, move in enumerate(moves):
        pick = 0
        for k, j in enumerate(game[move-1]):
            # pick 
            if pick == 0:
                if j != 0:
                    pick = j
                    game[move-1][k] = 0
                else:
                    pass
            else:
                pass
        # picks
        if len(picks) == 0:
            if pick == 0:
                pass
            else:
                picks.append(pick)
        else:
            if pick == 0:
                pass
            elif pick == picks[-1]:
                answer += 2
                picks.pop()
            else:
                picks.append(pick)
    return answer

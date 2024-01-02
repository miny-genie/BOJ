# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def Processing(GOAL):
    init = 123456780
    Q = deque([[init, 8, 0]])   # state, hashtag_loc, move_count

    while Q:
        state, loc, cnt = Q.popleft()
        
        if state == GOAL:
            return cnt
        
        if state in all_case: continue
        all_case[state] = cnt
        
        for m in can_move[loc]:
            Q.append((
                # swap 'loc' and 'm' digit
                state + (state // digit[m] % 10 * (digit[loc] - digit[m])),
                m,
                cnt + 1
            ))
            
    return -1

# ---------- Main ----------
all_case = {}
digit = [10**(8-i) for i in range(9)]

can_move = [
    [1,3],   [0,2,4],   [1,5],
    [0,4,6], [1,3,5,7], [2,4,8],
    [3,7],   [4,6,8],   [5,7]
]

# 2D list change to one-line int
line = 0

for i in range(3):
    row = list(map(int, input().split()))
    
    for j, v in enumerate(row):
        if v: line += digit[i*3+j] * v
            
answer = Processing(line)
print(answer)

# ---------- Comment ----------
# 백준 11112번과 같은 매커니즘
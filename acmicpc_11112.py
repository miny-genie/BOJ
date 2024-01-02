# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def Preprocessing():
    init = 123456780
    Q = deque([[init, 8, 0]])   # state, hashtag_loc, move_count

    while Q:
        state, loc, cnt = Q.popleft()
        
        if state in all_case: continue
        all_case[state] = cnt
        
        for m in can_move[loc]:
            Q.append((
                # swap 'loc' and 'm' digit
                state + (state // digit[m] % 10 * (digit[loc] - digit[m])),
                m,
                cnt + 1
            ))
    return

# ---------- Main ----------
all_case = {}
digit = [10**(8-i) for i in range(9)]

can_move = [
    [1,3],   [0,2,4],   [1,5],
    [0,4,6], [1,3,5,7], [2,4,8],
    [3,7],   [4,6,8],   [5,7]
]

Preprocessing()

for _ in range(int(input())):
    _ = input()
    
    # 2D list change to one-line int
    line = 0
    
    for i in range(3):
        row = input().rstrip()
        
        for j, v in enumerate(row):
            if v != '#':
                line += digit[i*3+j] * int(v)
                
    if line in all_case: print(all_case[line])
    else: print("impossible")

# ---------- Comment ----------
# https://oculis.tistory.com/181 , oculis
# 백준 1525번과 같은 매커니즘
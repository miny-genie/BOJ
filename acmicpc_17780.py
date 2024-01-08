# ---------- Import ----------
from collections import defaultdict
import sys
input = sys.stdin.readline

# STOP, RGT, LFT, UP, DN
dr = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

# ---------- Function ----------
def OUT_OF_BOUND(x, y):
    if 0 <= x < size and 0 <= y < size: return False
    else: return True


def Action_by_Color(color, x, y, nx, ny):
    if color == 0: step = 1
    else: step = -1

    cur_loc_chess = loc_2_cur[(x, y)]    # current location chess info

    for c in cur_loc_chess: num_2_loc[c] = (nx, ny)    # all chess move
    loc_2_cur[(nx, ny)] = loc_2_cur[(nx, ny)] + cur_loc_chess[::step]    # stack
    loc_2_cur[(x, y)] = []    # current location is empty
    
    return len(loc_2_cur[(nx, ny)])    # how many chess stack
            
            
def MyTurn():
    for chess in range(1, piece_count + 1):
        loc = num_2_loc[chess]
        dir = num_2_dir[chess]
        
        cur = loc_2_cur[loc]
        idx = cur.index(chess)
        
        # Not bottom-most
        if idx: continue
        
        x, y = loc
        dx, dy = dir
        nx, ny = dx + x, dy + y
        
        # Checking chess-board color
        if OUT_OF_BOUND(nx, ny): state = 2
        else: state = chess_board[nx][ny]
                    
        # Color is blue or out of bound
        if state == 2:
            rx, ry = -dx + x, -dy + y 
            num_2_dir[chess] = (-dx, -dy)
            
            # Checking chess-board color
            if OUT_OF_BOUND(rx, ry): state = 2
            else: state = chess_board[rx][ry]
                        
            # Reverse is blue, then nothing action
            if not (state == 2):
                stack = Action_by_Color(state, x, y, rx, ry)
                if stack >= 4: return "END"
        
        # Color is white or red
        else:
            stack = Action_by_Color(state, x, y, nx, ny)
            if stack >= 4: return "END"
    
    return "CONTINUE"

# ---------- Main ----------
size, piece_count = map(int, input().split())
chess_board = [list(map(int, input().split())) for _ in range(size)]

# declaration
num_2_loc = dict()
num_2_dir = dict()
loc_2_cur = defaultdict(list)

# init
for i in range(piece_count):
    row, col, direction = map(int, input().split())
    
    num_2_loc[i+1] = (row-1, col-1)
    num_2_dir[i+1] = dr[direction]
    loc_2_cur[(row-1, col-1)].append(i+1)

# game set condition: turn ＜ 1000
for turn in range(1, 1000 + 1):    
    state = MyTurn()

    if state == "END":
        print(turn)
        break

# more than or equal to 1000
else:
    print(-1)
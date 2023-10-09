# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def FILL(length):
    # DN, RGT, UP, LFT
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction = -1

    # Init
    board = [[0] * length for _ in range(length)]
    x, y = 0, 0

    board[x][y] = length ** 2
    current = length ** 2 - 1

    # Fill
    while current > 0:
        direction = (direction + 1) % 4
        dx = dxy[direction][0]
        dy = dxy[direction][1]
        
        while (0<=x+dx<length) and (0<=y+dy<length) and (board[x+dx][y+dy] == 0):
            x += dx
            y += dy
            board[x][y] = current
            current -= 1
            
    return board
    
# ---------- Main ----------
length = int(input())
whereIs = int(input())
coord = []

# Filling the board
board = FILL(length)

# Answer board
for idx, line in enumerate(board, 1):
    print(*line)
    if whereIs in line:
        coord = [idx, line.index(whereIs)+1]
        
# Answer coordinate
print(*coord)
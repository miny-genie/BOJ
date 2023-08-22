# ---------- Import ----------
from copy import deepcopy as dcopy
import sys
input = sys.stdin.readline

# ---------- Function ----------
def fill(board, way, x, y):
    for i in way:
        nx, ny = x, y   # setup
        while True:
            nx += dx[i] # Continuous add
            ny += dy[i] # Continuous add
            
            if 0 <= nx < row and 0 <= ny < col: # can move
                if board[nx][ny] == 6:      # wall
                    break
                elif board[nx][ny] == 0:    # not wall 
                    board[nx][ny] = 7
            else:   # out of wall
                break
    return


def DFS(arr, depth):
    global min_area

    if depth == len(CCTV):
        area = 0    # init
        for line in arr: area += line.count(0)  # how many zero
        min_area = min(min_area, area)  # comapre which is minimum
        return
    
    temp = dcopy(arr)           # not editing origin
    cctv, x, y = CCTV[depth]    # cctv type, x and y coordinate
    
    for d in direction[cctv]:
        fill(temp, d, x, y)     # fill cctv area
        DFS(temp, depth + 1)    # go deep
        temp = dcopy(arr)       # backtracking

    return

# ---------- Main ----------
row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]

# Find CCTV location
CCTV = [
    (graph[x][y], x, y) for x in range(row) for y in range(col)
    if graph[x][y] and graph[x][y] != 6
]

# UP, RGT, DN, LFT
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# Setup direction, by index
direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
    [[0, 1, 2, 3]] 
]

# Init min var
min_area = 1e9

DFS(graph, 0)
print(min_area)
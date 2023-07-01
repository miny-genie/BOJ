# -------------------- Case 1 --------------------
# ---------- Import ----------
from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(row: int, col: int, lab: list) -> int:
    result = 0
    FLAG = 0
    
    # UP, DN, LFT, RHT
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # Checking empty(0) area that can be build a wall
    empty_space = [(x, y) for x in range(row) for y in range(col) if lab[x][y] == 0]
    for empty in combinations(empty_space, 3):
        graph = copy.deepcopy(lab)
        
        # Build a wall using combinations
        for wallX, wallY in empty:
            graph[wallX][wallY] = 1

        # Checking virus(2) area    
        queue = deque([(x, y) for x in range(row) for y in range(col) if graph[x][y] == 2])
        # queue = deque((x, y) for x in range(row) for y in range(col) if graph[x][y] == 2)
             
        # Starting BFS   
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<row and 0<=ny<col and graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append((nx, ny))
                    
        # Checking safe(0) area
        cnt = 0
        for line in graph:
            cnt += line.count(0)
        
        result = max(cnt, result)        
        
    return result

# ---------- Main ----------
row, col = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(row)]

result = BFS(row, col, lab)
print(result)


# -------------------- Case 2: TLE (Pypy3: AC) --------------------
# ---------- Import ----------
from collections import deque
import copy
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS():    
    queue = deque()
    graph = copy.deepcopy(lab)
    
    # Checking virus location
    for r in range(row):
        for c in range(col):
            if graph[r][c] == 2:
                queue.append([r, c])
    
    # BFS calculating
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= row or ny >= col: continue
            if graph[nx][ny] == 1 or graph[nx][ny] == 2: continue
            
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append([nx, ny])
    
    # Count '0' area
    global result
    
    cnt = 0
    for r in range(row):
        for c in range(col):
            if graph[r][c] == 0:
                cnt += 1
    
    result = max(result, cnt)
    return 


def makeWall(cnt: int):
    # Wall is 3, then BFS
    if cnt == 3:
        BFS()
        return
    
    # Making wall using backtracking
    for r in range(row):
        for c in range(col):
            if lab[r][c] == 0:
                lab[r][c] = 1
                makeWall(cnt + 1)
                lab[r][c] = 0
                
    return


# ---------- Main ----------
row, col = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(row)]

# UP, DN, LFT, RGT
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
makeWall(0)
print(result)
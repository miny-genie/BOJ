# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def isZeroExist(lst):
    return not all(v for box in lst for line in box for v in line)


def BFS(graph):
    # Select '1' location
    queue = deque([
        (z, x, y)\
        for z in range(floor) for x in range(row) for y in range(col)\
        if graph[z][x][y] == 1
    ])
    
    # Init 3 dimenstion 'visited' list
    visited = [[[0 for _ in range(col)] for _ in range(row)] for _ in range(floor)]
    
    # visited 'tomato' location setup '1'
    for z, x, y in queue:
        visited[z][x][y] = 1

    # Do BFS
    while queue:
        z, x, y = queue.popleft()
        
        # Find 6 way
        for dz, dx, dy in dxyz:
            nz = z + dz
            nx = x + dx
            ny = y + dy
            
            # Inbound range, not yet visited, tomato is exist
            if 0 <= nz < floor and 0 <= nx < row and 0 <= ny < col\
            and graph[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                
                queue.append((nz, nx, ny))
                visited[nz][nx][ny] = visited[z][x][y] + 1
                graph[nz][nx][ny] = 1

    # Using another function 'isZeroExist'
    if isZeroExist(graph): print(-1)    
    else: print(visited[z][x][y] - 1)
    
    return

# ---------- Main ----------
col, row, floor = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(row)] for _ in range(floor)]

# (z, x, y): UP, DN, LFT, RGT, FRT, BCK
dxyz = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)]

if isZeroExist(graph): BFS(graph)
else: print(0)
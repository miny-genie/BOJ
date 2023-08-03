# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(row, col, graph, visited):
    # UP, DN, LFT, RGT
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(x, y) for x in range(row) for y in range(col) if graph[x][y] == 2])
    visited[queue[0][0]][queue[0][1]] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<row and 0<=ny<col and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 0
                
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return visited

# ---------- Main ----------
row, col = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(row)]

visited = [[-1] * col for _ in range(row)]
visited = BFS(row, col, map_, visited)

for r in range(row):
    for c in range(col):
        if not map_[r][c]: print(0, end=" ")
        else: print(visited[r][c], end=" ")
    print()
    
# ---------- Comment ----------
# Counter Example
# 2 3
# 2 0 0
# 0 1 0

# 5 5
# 2 0 0 0 0
# 0 1 1 1 0
# 0 1 0 1 0
# 0 1 1 1 0
# 0 0 0 0 0
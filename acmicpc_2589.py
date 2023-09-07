# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(x, y):
    visited = [[0] * col for _ in range(row)]
    queue = deque([(x, y)])
    visited[x][y] = 1
    
    m_value = 0
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < row and 0 <= ny < col\
                and visited[nx][ny] == 0 and graph[nx][ny] == "L":
                queue.append((nx, ny))
                m_value = max(m_value, visited[x][y])
                visited[nx][ny] = visited[x][y] + 1
    
    return m_value

# ---------- Main ----------
row, col = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(row)]

# UP, DN, LFT, RGT
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

max_dist = 0

for r in range(row):
    for c in range(col):
        if graph[r][c] == "L":
            max_dist = max(max_dist, BFS(r, c))
            
print(max_dist)

# ---------- Comment ----------
# 5 7
# WLLWWWL
# LLLWLLL
# LWLWLWW
# LWLWLLL
# WLLWLWW
# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(x, y):
    global graph
    
    queue = deque([(x, y)])
    graph[x][y] = 0
    count = 1
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            
            if 0<=nx<row and 0<=ny<col and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    
    return count

# ---------- Main ----------
row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]

count = 0
max_area = 0

for r in range(row):
    for c in range(col):
        if graph[r][c] == 1:
            count += 1
            max_area = max(max_area, BFS(r, c))
            
print(count)
print(max_area)
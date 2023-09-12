# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

NOT_YET_BREAK = 1
ALREADY_BREAK = 0

# ---------- Function ----------
def BFS(x, y):
    queue = deque([(x, y, 1)])
    visited[x][y][NOT_YET_BREAK] = 1
    
    while queue:
        x, y, break_count = queue.popleft()
        
        # Arrived destination
        if x == row-1 and y == col-1:
            return max(visited[row-1][col-1])
                        
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            # Outbound
            if nx < 0 or ny < 0 or nx >= row or ny >= col:
                continue
            
            # Break the wall
            if graph[nx][ny] == 1 and break_count == 1:
                visited[nx][ny][ALREADY_BREAK] = visited[x][y][break_count] + 1
                queue.append((nx, ny, 0))
            
            # Not break the wall
            if graph[nx][ny] == 0 and visited[nx][ny][break_count] == 0:
                visited[nx][ny][break_count] = visited[x][y][break_count] + 1
                queue.append((nx, ny, break_count))
    
    return -1

# ---------- Main ----------
row, col = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(row)]

# [already_break, not_yet_break]
visited = [[[0] * 2 for _ in range(col)] for _ in range(row)]

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = BFS(0, 0)
print(answer)
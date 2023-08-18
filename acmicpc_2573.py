# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(r, c, visited):    
    queue = deque([(r, c)])
    visited[r][c] = 1
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1
    
    return 1

# ---------- Main ----------
row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]

year = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    if not sum(map(sum, graph)):
        print(0); break
        
    # Year is on the rise
    year += 1
        
    # How many melt
    melt = []
    for x in range(row):
        for y in range(col):
            count = 0
            
            if graph[x][y] > 0:
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < row and 0 <= ny < col and graph[nx][ny] == 0:
                        count += 1
                        
            melt.append((x, y, count))
            
    # Melting down ice
    for x, y, count in melt:
        graph[x][y] = max(0, graph[x][y] - count)
        
    # How many ice fraction
    ice_count = 0
    visited = [[0]*col for _ in range(row)]
    
    for r in range(row):
        for c in range(col):
            if graph[r][c] and visited[r][c] == 0:
                ice_count += BFS(r, c, visited)       
    
    # End condition
    if ice_count >= 2:
        print(year); break
  
# ---------- Comment ----------
# L13 move to L18: then solved MLE


# --------------------------------------------------
# from collections import deque

# N, M = list(map(int, input().split()))

# ice = [list(map(int, input().split())) for _ in range(N)]

# move = [[0, 1], [1, 0], [-1, 0], [0, -1]]

# q = deque()


# def bfs(x, y):
#     q.append((x, y))

#     while q:
#         x, y = q.popleft()
#         for mx, my in move:
#             nx, ny = mx+x, my+y
#             if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
#                 if ice[nx][ny] == 0 and ice[x][y] > 0:
#                     ice[x][y] -= 1
#                 elif ice[nx][ny] != 0:
#                     visited[nx][ny] = True
#                     q.append((nx, ny))
#     return 1


# time = 0
# while ice:
#     cnt = 0
#     visited = [[False]*M for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             if ice[i][j] != 0 and not visited[i][j]:
#                 visited[i][j] = True
#                 cnt += bfs(i, j)

#     if cnt >= 2:
#         print(time)
#         break
#     elif cnt == 0:
#         print(0)
#         break
#     time += 1

# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS():
    global queue

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= row or ny >= col: continue
            if graph[nx][ny] != 0: continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return max(map(max, graph)) - 1

# ---------- Main ----------
col, row = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]

# UP, DN, LFT, RGT
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
for r in range(row):
    for c in range(col):
        if graph[r][c] == 1:
            queue.append([r, c])

result = BFS()
print(-1) if any(0 in i for i in graph) else print(result)
# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= row or ny >= col: continue
            if graph[nx][ny] == 0: continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[row-1][col-1]

# ---------- Main ----------
row, col = map(int, input().split())
graph = []

# UP, DN, LFT, RGT
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(row):
    graph.append(list(map(int, input().rstrip())))

print(BFS(0, 0))
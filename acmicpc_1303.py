from collections import deque
from sys import stdin
input = stdin.readline


def bfs(r: int, c: int) -> tuple[int, str]:
    count = 1
    queue = deque([(r, c)])
    visited[r][c] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = dx + x
            ny = dy + y
            if 0<=nx<row and 0<=ny<col and not visited[nx][ny] and grid[nx][ny] == grid[x][y]:
                count += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    return count * count, grid[x][y]


col, row = map(int, input().split())
grid = [list(input().strip()) for _ in range(row)]
visited = [[False] * col for _ in range(row)]

w, b = 0, 0
for r in range(row):
    for c in range(col):
        if not visited[r][c]:
            score, state = bfs(r, c)
            if state == "W": w += score
            else: b += score            
        
print(w, b)


# 2026.01.09 해결
# Diamond Ⅴ 2213 > 2213
# 승급까지 87 > 87

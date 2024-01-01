# ---------- Import ----------
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(ways, cow, visited):
    Q = deque([cow])
    connect = 0
    while Q:
        x, y = Q.popleft()
        
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx = dx + x
            ny = dy + y
            
            if (x, y, nx, ny) in ways or (nx, ny, x, y) in ways:
                continue
            
            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            
            if visited[nx][ny] == 7:
                connect += 1
                visited[nx][ny] = 1
                Q.append((nx, ny))
            
            elif not visited[nx][ny]:
                visited[nx][ny] = 1
                Q.append((nx, ny))
                
    return len(cows) - connect - 1

# ---------- Main ----------
size, cow, way = map(int, input().split())
ways = {tuple(map(lambda x: int(x)-1, input().split())):1 for _ in range(way)}
cows = [list(map(lambda x: int(x)-1, input().split())) for _ in range(cow)]

preset = [[0] * size for _ in range(size)]
for x, y in cows:
    preset[x][y] = 7

answer = 0
for cow in cows:
    visited = deepcopy(preset)
    visited[cow[0]][cow[1]] = 1
    answer += BFS(ways, cow, visited)
print(answer // 2)
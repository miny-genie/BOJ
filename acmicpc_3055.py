# ---------- Import ---------
from collections import deque
from sys import stdin
input = stdin.readline

# ---------- Functino ----------
def bfs(
    graph:list[list],
    goal: tuple,
    start: tuple,
    obstacle: tuple
) -> int | str:
    
    water = deque()
    if obstacle: water = deque(obstacle)
    character = deque([(start[0], start[1], 0)])
    
    while character:
        for _ in range(len(water)):
            x, y = water.popleft()
            
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx = x + dx
                ny = y + dy

                if 0<=nx<row and 0<=ny<col and graph[nx][ny] == ".":
                    graph[nx][ny] = "*"
                    water.append((nx, ny))
                    
        for _ in range(len(character)):
            x, y, move = character.popleft()
            
            if (x, y) == goal:
                return move
            
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx = x + dx
                ny = y + dy
                
                if 0<=nx<row and 0<=ny<col and\
                (graph[nx][ny] == "." or graph[nx][ny] == "D"):
                    graph[nx][ny] = "S"
                    character.append((nx, ny, move+1))
    
    return "KAKTUS"

# ---------- Main ----------
row, col = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(row)]

D, S, water = tuple(), tuple(), list()
for r, line in enumerate(graph):
    for c, data in enumerate(line):
        if data == "D":
            D = (r, c)
            
        elif data == "S":
            S = (r, c)
            
        elif data == "*":
            water.append((r, c))

answer = bfs(graph, D, S, water)
print(answer)
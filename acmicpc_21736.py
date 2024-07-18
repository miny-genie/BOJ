from collections import deque
from sys import stdin
input = stdin.readline


def bfs(campus: list, row: int, col: int) -> int|str:
    visited = [[False] * col for _ in range(row)]
    
    for x in range(row):
        for y in range(col):
            if campus[x][y] == "I":
                own = [(x, y)]
                visited[x][y] = True 
    queue = deque(own)
    
    people = 0
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = dx + x
            ny = dy + y
            
            if 0<=nx<row and 0<=ny<col and not visited[nx][ny] and campus[nx][ny] != "X":
                if campus[nx][ny] == "P":
                    people += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return people


row, col = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(row)]
answer = bfs(campus, row, col)
print(answer if answer else "TT")
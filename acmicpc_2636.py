from collections import deque
from sys import stdin
input = stdin.readline


def find_outline(graph: list) -> set:
    visited = [[0]*col for _ in range(row)]
    visited[0][0] = 1
    
    outline = set()
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = dx + x, dy + y
            
            if 0<=nx<row and 0<=ny<col and not visited[nx][ny]:
                visited[nx][ny] = 1
                if graph[nx][ny]:
                    outline.add((nx, ny))
                else:
                    queue.append((nx, ny))
    
    return outline


def remove_cheese(graph: list, outline: set) -> list:
    for x, y in outline:
        graph[x][y] = 0
    return graph


row, col = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(row)]
area = sum(map(sum, cheese))
time, bef = 0, area

while area:
    outline = find_outline(cheese)
    remove = len(outline)
    bef = area
    area -= remove
    cheese = remove_cheese(cheese, outline)
    time += 1
    
print(time, bef, sep="\n")
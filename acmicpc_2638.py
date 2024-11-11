from collections import deque
from sys import stdin
input = stdin.readline


def find_outer_cheeze(row: int, col: int, paper: list) -> list:
    visited = [[False] * col for _ in range(row)]
    visited[0][0] = True
    
    queue = deque()
    queue.append((0, 0))
    paper[0][0] = 9
    
    outer_cheeze = []
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = dx + x
            ny = dy + y
            
            # out of bound
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                if paper[nx][ny] == 1:
                    outer_cheeze.append((nx, ny))
                    continue
                queue.append((nx, ny))
                paper[nx][ny] = 9
              
    return outer_cheeze


def filter_melt_cheeze(paper: list, outer_cheeze: list) -> list:
    outer_melt_cheeze = []
    
    for x, y in outer_cheeze:
        air = sum(
            1
            for nx, ny in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
            if paper[nx][ny] == 9
        )
        if air >= 2:
            outer_melt_cheeze.append((x, y))
            
    return outer_melt_cheeze


def melt_cheeze(paper: list, outer_cheeze: list) -> None:
    for x, y in outer_cheeze:
        paper[x][y] = 0
    return


def remain_cheeze(paper: list) -> bool:
    return any(
        True
        for line in paper
        for space in line
        if space == 1
    )


row, col = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(row)]

time = 0
while True:
    outer_cheeze = find_outer_cheeze(row, col, paper)
    outer_cheeze = filter_melt_cheeze(paper, outer_cheeze)
    melt_cheeze(paper, outer_cheeze)
    time += 1
    if not remain_cheeze(paper):
        break

print(time)
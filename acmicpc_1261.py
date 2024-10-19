from collections import deque
from sys import stdin
input = stdin.readline

WALL = 1


def bfs(row: int, col: int, maze: list) -> int:
    def out_of_bound(x: int, y: int, row: int, col: int) -> bool:
        return x < 0 or y < 0 or x >= row or y >= col
    
    distance = [[float('inf')] * col for _ in range(row)]
    distance[0][0] = 0
    
    queue = deque([(0, 0, 0)])
    while queue:
        break_time, x, y = queue.popleft()
        if distance[x][y] < break_time:
            continue
        
        for nx, ny in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
            if out_of_bound(nx, ny, row, col):
                continue
            
            if maze[nx][ny] == WALL:
                if distance[nx][ny] > break_time + 1:
                    distance[nx][ny] = break_time + 1
                    queue.append((break_time + 1, nx, ny))
            else:
                if distance[nx][ny] > break_time:
                    distance[nx][ny] = break_time
                    queue.appendleft((break_time, nx, ny))
    
    return distance[-1][-1]


col, row = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(row)]
print(bfs(row, col, maze))

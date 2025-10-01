from collections import deque
from sys import stdin
input = stdin.readline


# is this area trash
def isvalid(x: int, y: int) -> bool:
    return grid[x][y]


# calculate trash area
def find_area_size(x: int, y: int) -> int:
    def isin(x: int, y: int) -> bool:
        return 0 <= x < row and 0 <= y < col
    
    queue = deque([(x, y)])
    area = 1
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = dx + x
            ny = dy + y
            if isin(nx, ny) and isvalid(nx, ny) and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                area += 1

    return area


# init var
row, col, trash_count = map(int, input().split())
grid = [[False] * col for _ in range(row)]
visited = [[False] * col for _ in range(row)]

# init trash loc
for _ in range(trash_count):
    x, y = map(lambda x: int(x) - 1, input().split())
    grid[x][y] = True

# find biggest area for bfs
biggest_size = 0
for x in range(row):
    for y in range(col):
        
        # already visited
        if visited[x][y]:
            continue
        
        # not yet visited
        visited[x][y] = True
        
        # this area is trash
        if isvalid(x, y):
            size = find_area_size(x, y)
            biggest_size = max(biggest_size, size)

print(biggest_size)

# 분명히 플레티넘 95 포인트였는데
# 상당히 오랜만에 다시 와서 실버 1 이 문제를 제출해보니
# 다이아 5 2213점이 되어있음
# 다이아 4 승급까지 87 포인트
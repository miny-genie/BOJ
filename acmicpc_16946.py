from collections import deque
from sys import stdin
input = stdin.readline

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
MOD = 10


def in_bound(x: int, y: int) -> bool:
    return 0 <= x < row and 0 <= y < col


def connect_space(grid: list) -> dict:
    connected = {1:0}
    block_id = 100

    for row, line in enumerate(grid):
        for col, value in enumerate(line):
            if value:
                continue
            
            # init
            block_count = 1
            queue = deque([(row, col)])
            grid[row][col] = block_id
            
            # bfs
            while queue:
                x, y = queue.popleft()
                
                for dx, dy in DIRECTIONS:
                    nx = dx + x
                    ny = dy + y
                    
                    if in_bound(nx, ny) and grid[nx][ny] == 0:
                        block_count += 1
                        queue.append((nx, ny))
                        grid[nx][ny] = block_id
            
            # info update
            connected[block_id] = block_count % MOD
            block_id += 1
    
    return connected


row, col = map(int, input().split())
grid = [list(map(int, list(input().rstrip()))) for _ in range(row)]
connected = connect_space(grid)

# print
for x, line in enumerate(grid):
    for y, value in enumerate(line):
        
        # tear down the wall
        if value == 1:
            
            # comprehension ver
            block_type = {
                grid[nx][ny]
                for dx, dy in DIRECTIONS
                if in_bound((nx := dx + x), (ny := dy + y))\
                and grid[nx][ny] != 1
            }
            
            # # standard ver
            # block_type = set()
            # for dx, dy in DIRECTIONS:
            #     nx = dx + x
            #     ny = dy + y
            #     if in_bound(nx, ny) and grid[nx][ny] != 1:
            #         block_type.add(nx, ny)
            
            num = (1 + sum(connected[block_id] for block_id in block_type)) % MOD
            print(num, end="")
        
        # not wall
        else:
            print(0, end="")
    
    # line break
    print()

# 24.12.25
# Platinum 1: 2151 > 2151 (+0pts)
# 승급까지 -49 > -49
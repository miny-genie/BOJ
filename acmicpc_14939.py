from copy import deepcopy
from sys import stdin
input = stdin.readline


def out_of_bound(x, y):
    return x < 0 or x > 9 or y < 0 or y > 9


def toggle_cross(grid: list, x: int, y: int):
    for dx, dy in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x+dx, y+dy
        if not out_of_bound(nx, ny):
            grid[nx][ny] = not grid[nx][ny]


# declaration
answer = float('inf')
bulb_grid = [[False for _ in range(10)] for _ in range(10)]

# input data and init
for i in range(10):
    input_line = input().rstrip()
    for j, char in enumerate(input_line):
        if char == "O":
            bulb_grid[i][j] = True

# brute force
for first_line in range(1 << 10):
    temp_grid = deepcopy(bulb_grid)
    toggle_count = 0
    
    # all possible cases of the first line
    for col in range(10):
        if first_line & (1 << col):
            toggle_count += 1
            toggle_cross(temp_grid, 0, col)
            
    # follow up each line and turn off the upper line
    for row in range(1, 10):
        for col in range(10):
            if temp_grid[row-1][col]:
                toggle_count += 1
                toggle_cross(temp_grid, row, col)
                
    # the last line is all off
    if not any(temp_grid[-1]):
        answer = min(answer, toggle_count)

print(-1) if answer == float('inf') else print(answer)
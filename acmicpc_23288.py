# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def check_range():
    global cur_dir, x, y

    if x < 0 or x >= row:
        cur_dir = (cur_dir + 2) % 4
        x += dx[cur_dir] * 2

    if y < 0 or y >= col:
        cur_dir = (cur_dir + 2) % 4
        y += dy[cur_dir] * 2


def roll_dice(dir: int) -> list:
    new_map = [0] * 6

    if dir == 0:
        new_map[0] = dice_map[2]; new_map[1] = dice_map[1]; new_map[2] = dice_map[4]
        new_map[3] = dice_map[3]; new_map[4] = dice_map[5]; new_map[5] = dice_map[0]
        return new_map

    elif dir == 1:
        new_map[0] = dice_map[0]; new_map[1] = dice_map[5]; new_map[2] = dice_map[1]
        new_map[3] = dice_map[2]; new_map[4] = dice_map[4]; new_map[5] = dice_map[3]
        return new_map

    elif dir == 2:
        new_map[0] = dice_map[5]; new_map[1] = dice_map[1]; new_map[2] = dice_map[0]
        new_map[3] = dice_map[3]; new_map[4] = dice_map[2]; new_map[5] = dice_map[4]
        return new_map

    else:
        new_map[0] = dice_map[0]; new_map[1] = dice_map[2]; new_map[2] = dice_map[3]
        new_map[3] = dice_map[5]; new_map[4] = dice_map[4]; new_map[5] = dice_map[1]
        return new_map


def change_direction(dir: int, dice_num: int, map_num: int) -> int:
    if dice_num == map_num:
        return dir

    elif dice_num > map_num:
        dir += 1; dir %= 4
        return dir

    else:
        dir -= 1; dir %= 4
        return dir


def BFS(x: int, y: int, value: int) -> int:
    total = value
    visited = [[0] * col for _ in range(row)]

    queue = deque([(x, y)])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col\
                and visited[nx][ny] == 0 and graph[nx][ny] == value:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    total += value

    return total

# ---------- Main ----------
# UP, RGT, DN, LFT
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
    
# UP, RGT, DN, LFT, dir = [0, 1, 2, 3]
cur_dir = 1

answer = 0
x, y = 0, 0
dice_map = [2, 4, 1, 3, 5, 6]

row, col, move = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]

for _ in range(move):    
    # Move
    x += dx[cur_dir]
    y += dy[cur_dir]
    
    # Check bound of range
    check_range()
    
    # Rolling dice
    dice_map = roll_dice(cur_dir)
    
    # Add score
    answer += BFS(x, y, graph[x][y])
    
    # Check direction change
    cur_dir = change_direction(cur_dir, dice_map[-1], graph[x][y])
    
print(answer)
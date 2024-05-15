from collections import defaultdict, deque
from sys import stdin
input = stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def fishing_shark(col: int, depth_limit: int, sharks: dict) -> tuple|None:
    for row in range(depth_limit):
        if sharks[(row, col)]:
            return (row, col)
    return None


def sharks_move(sharks: dict, grid_row: int, grid_col: int) -> dict:
    new_shark = defaultdict(deque)
    for key, value in sharks.items():
        if not value:
            continue
        
        x, y = key
        speed, degree, size = value.popleft()
        for _ in range(speed):
            if 0<=x+dx[degree]<grid_row and 0<=y+dy[degree]<grid_col:
                x += dx[degree]
                y += dy[degree]
            
            else:
                degree ^= 1
                x += dx[degree]
                y += dy[degree]
                
        new_shark[(x, y)].append((speed, degree, size))
        
    return new_shark


def cannibalism(sharks: dict) -> dict:
    for key, value in sharks.items():
        if len(value) >= 2:
            temp_speed, temp_degree, top_size = 0, 0, 0
            
            for speed, degree, size in sharks[key]:
                if size > top_size:
                    temp_speed = speed
                    temp_degree = degree
                    top_size = size
                    
            value = deque([(temp_speed, temp_degree, top_size)])
            sharks[key] = value
            
    return sharks


def clean_dict(dict_):
    del_list = [key for key, value in dict_.items() if not value]
    for del_key in del_list:
        del(dict_[del_key])
    return dict_


grid_row, grid_col, shark_count = map(int, input().split())

sharks = defaultdict(deque)
for _ in range(shark_count):
    row, col, speed, degree, size = map(int, input().split())
    key = (row-1, col-1)
    sharks[key].append((speed, degree-1, size))
    
total_fishing = 0
for angler_pos in range(grid_col):
    shark_pos = fishing_shark(angler_pos, grid_row, sharks)
    if shark_pos is not None:
        size = sharks[shark_pos].pop()[2]
        total_fishing += size
        
    sharks = sharks_move(sharks, grid_row, grid_col)
    sharks = cannibalism(sharks)
    sharks = clean_dict(sharks)
    
print(total_fishing)
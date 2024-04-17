from collections import deque
from sys import stdin
input = stdin.readline


def transposition(matrix: tuple) -> tuple:
    return tuple(zip(*matrix))


def flip_vertical(matrix: tuple) -> tuple:
    return matrix[::-1]


def flip_horizontal(matrix: tuple) -> tuple:
    return tuple(row[::-1] for row in matrix)


def generate_all_combinations():
    bases = [
        ((0, 0, 1, 1, 1), (1, 1, 1, 0, 0)),
        ((1, 0, 0, 0), (1, 1, 1, 1), (1, 0, 0, 0)),
        ((0, 1, 0, 0), (1, 1, 1, 1), (1, 0, 0, 0)),
        ((0, 0, 1, 0), (1, 1, 1, 1), (1, 0, 0, 0)),
        ((0, 0, 0, 1), (1, 1, 1, 1), (1, 0, 0, 0)),
        ((0, 1, 0, 0), (1, 1, 1, 1), (0, 1, 0, 0)),
        ((0, 0, 1, 0), (1, 1, 1, 1), (0, 1, 0, 0)),
        ((0, 0, 1, 1), (0, 1, 1, 0), (1, 1, 0, 0)),
        ((0, 0, 1, 1), (1, 1, 1, 0), (1, 0, 0, 0)), 
        ((1, 1, 0, 0), (0, 1, 1, 1), (0, 1, 0, 0)), 
        ((0, 1, 0, 0), (1, 1, 1, 0), (0, 0, 1, 1)) 
    ]
    
    cache = dict()
    for base in bases:
        cache[base] = True
        cache[flip_vertical(base)] = True
        base = flip_horizontal(base)
        cache[base] = True
        cache[flip_vertical(base)] = True
        
        base = transposition(base)
        cache[base] = True
        cache[flip_vertical(base)] = True
        base = flip_horizontal(base)
        cache[base] = True
        cache[flip_vertical(base)] = True
    
    return cache


def extract_submatrix(matrix: list) -> tuple:
    min_row, max_row = 7, -1
    min_col, max_col = 7, -1
    
    for r, row in enumerate(matrix):
        for c, value in enumerate(row):
            if value:
                if r < min_row: min_row = r
                if r > max_row: max_row = r
                if c < min_col: min_col = c
                if c > max_col: max_col = c
    
    return tuple(
        tuple(row[min_col:max_col+1])
        for row in matrix[min_row:max_row+1]
    )


def replace_numbers(matrix: tuple) -> tuple:
    new_matrix = list()
    for row in matrix:
        new_row = list()
        for num in row:
            if 2 <= num <= 6: new_row.append(1)
            else: new_row.append(num)
        new_matrix.append(tuple(new_row))
        
    return tuple(new_matrix)


def find_opposite(matrix: tuple) -> int:
    row, col = len(matrix), len(matrix[0])
    visited = [[0] * col for _ in range(row)]
    
    for x in range(row):
        for y in range(col):
            if matrix[x][y] == 1:
                move_cnt = {"U":0, "D":0, "L":0, "R":0}
                Q = deque([(1, x, y, "", move_cnt, [])])
                visited[x][y] = 1
                
    while Q:
        value, x, y, direction, move_cnt, possible = Q.popleft()
        
        if direction in possible and move_cnt[direction] == 2:
            return value
        
        for dx, dy, dr in [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]:
            nx = dx + x
            ny = dy + y
            
            if 0<=nx<row and 0<=ny<col and not visited[nx][ny] and matrix[nx][ny]:
                if value == 1:
                    possible.append(dr)
                
                visited[nx][ny] = 1
                move_cnt[dr] += 1
                Q.append((matrix[nx][ny], nx, ny, dr, move_cnt, possible))


all_combinations = generate_all_combinations()

matrix = [list(map(int, input().split())) for _ in range(6)]
submatrix = extract_submatrix(matrix)

if replace_numbers(submatrix) in all_combinations:
    ans = find_opposite(submatrix)
    print(ans)
    
else:
    print(0)
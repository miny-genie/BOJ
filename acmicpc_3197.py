from collections import deque
from sys import stdin
input = stdin.readline

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def to_index(x, y):
    return x * col + y


def melt(water: deque):
    next_water = deque()
    flag = False
    
    while water:
        x, y = water.popleft()
        for dx, dy in directions:
            nx = dx + x
            ny = dy + y
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            
            if lake[nx][ny] == "X":
                lake[nx][ny] = "."
                next_water.append((nx, ny))
                uf.union(to_index(x, y), to_index(nx, ny))
                flag = True
            
            elif lake[nx][ny] == ".":
                uf.union(to_index(x, y), to_index(nx, ny))
            
    return next_water, flag


row, col = map(int, input().split())
lake = [list(input().rstrip()) for _ in range(row)]

swans = []
water = deque()
for r, line in enumerate(lake):
    for c, value in enumerate(line):
        if value == "L":
            swans.append((r, c))
            lake[r][c] = "."
            water.append((r, c))
        elif value == ".":
            water.append((r, c))

uf = UnionFind(row * col)
for x, y in water:
    for dx, dy in directions:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < row and 0 <= ny < col and lake[nx][ny] == ".":
            uf.union(to_index(x, y), to_index(nx, ny))

days = 0
while True:    
    if uf.find(to_index(*swans[0])) == uf.find(to_index(*swans[1])):
        break
    
    water, flag = melt(water)
    if flag:
        days += 1

print(days)

# 24.12.06
# Platinum 1: 2118 > 2119 (+1pts)
# 승급까지 -82 > -81
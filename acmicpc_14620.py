# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def check(x, y, visited):
    for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if (nx, ny) in visited:
            return False
    return True


def DFS(seed, total_cost):
    if seed == 3:
        global min_cost
        min_cost = min(min_cost, total_cost)
        return
    
    for x in range(1, N-1):
        for y in range(1, N-1):
            if check(x, y, visited):
                cost = 0
                for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    point = (nx, ny)
                    cur_cost = ground[nx][ny]
                    
                    cost += cur_cost
                    visited[point] = 1
                
                DFS(seed + 1, total_cost + cost)
                
                for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    point = (nx, ny)
                    del visited[point]
    return 

# ---------- Main ----------
N = int(input())
ground = [list(map(int, input().split())) for _ in range(N)]

min_cost = 3000
visited = dict()

DFS(0, 0)
print(min_cost)
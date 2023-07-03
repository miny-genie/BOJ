# ---------- Import ----------
import sys
input = sys.stdin.readline
sys.setrecursionlimit(30_000)

# ---------- Function ----------
def DFS(x: int, y: int, value: str) -> int:
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    
    if graph[x][y] == value and visited[x][y] == 0:
        visited[x][y] = 1
        DFS(x+1, y, value)
        DFS(x-1, y, value)
        DFS(x, y+1, value)
        DFS(x, y-1, value)
        
        return True    
    return False

# ---------- Main ----------
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

# Counting normal color
normal = 0

for row in range(N):
    for col in range(N):
        v = graph[row][col]
        if DFS(row, col, v):
            normal += 1

# Initializaion
visited = [[0]*N for _ in range(N)]
for row in range(N):
    for col in range(N):
        if graph[row][col] == "R":
            graph[row][col] = "G"
        
# Counting blind color
blind = 0

for row in range(N):
    for col in range(N):
        v = graph[row][col]
        if DFS(row, col, v):
            blind += 1
            
# Result
print(normal, blind)
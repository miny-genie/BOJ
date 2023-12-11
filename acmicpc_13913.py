# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Functoin ----------
def BFS(start, end):
    Q = deque([(start, 0)])
    
    while Q:
        x, move = Q.popleft()
        
        if x == end:
            return move, x
        
        for nx in [x+x, x+1, x-1]:
            if 0 <= nx <= 100_000 and not visited[nx]:
                Q.append((nx, move+1))
                visited[nx] = (nx, x)
    return

# ---------- Main ----------
start, end = map(int, input().split())
visited = [0] * 100_001
queue = list()

answer, goal = BFS(start, end)
print(answer)

while goal != start:
    queue.append(goal)
    goal = visited[goal][1]
queue.append(start)

print(*queue[::-1])
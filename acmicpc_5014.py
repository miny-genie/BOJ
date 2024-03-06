# ---------- Import ----------
from collections import deque
from sys import stdin
input = stdin.readline

# ---------- Function ----------
def bfs(visited, start, goal) -> int:
    Q = deque([(start, 0)])
    visited[start] = 1
    
    while Q:
        floor, move = Q.popleft()
        
        if floor == goal:
            return move
        
        for weight in (up, -down):
            next_floor = floor + weight
            
            if 0 < next_floor <= top and not visited[next_floor]:
                visited[next_floor] = 1
                Q.append((next_floor, move+1))
    
    return "use the stairs"

# ---------- Main ----------
top, cur, end, up, down = map(int, input().split())

visited = [0] * (top+1)
answer = bfs(visited, cur, end)
print(answer)
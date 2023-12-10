# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(start: int, end: int):
    visited = [0] * 100_001
    
    min_time = float('inf')
    catch = 0
    
    Q = deque([(start, 0)])
    while Q:
        x, time = Q.popleft()
        visited[x] = 1
        
        if x == end:
            min_time = min(min_time, time)
            
            if min_time == time:
                catch += 1
                
        if time > min_time:
            return min_time, catch

        for dx in [x, 1, -1]:
            nx = x + dx
            
            if nx < 0 or nx > 100_000:
                continue
            
            if not visited[nx]:
                Q.append((nx, time+1))
            
    return "NotFound", "NotFound"

# ---------- Main ----------
start, end = map(int, input().split())

if start < end:
    fastest_time, case = BFS(start, end)
    print(fastest_time, case, sep="\n")
    
else:
    print(start - end, 1, sep="\n")
# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Funtion ----------
def BFS(current: int, move: int) -> int:
    Q = deque([(current, move)])
    visited = [0] * (100 + 1)
    visited[1] = 1
    
    while Q:
        cur_num, move = Q.popleft()
        
        if cur_num == 100:
            return move
        
        for dice in [1, 2, 3, 4, 5, 6]:
            next_num = cur_num + dice
            
            if next_num in teleport:
                next_num = teleport[next_num]
            
            if next_num <= 100 and not visited[next_num]:
                Q.append((next_num, move+1))
                visited[next_num] = 1       
    
    return "IMPOSSIBLE"

# ---------- Main ----------
ladder_count, snake_count = map(int, input().split())

teleport = dict()
for _ in range(ladder_count + snake_count):
    key, value = map(int, input().split())
    teleport[key] = value
    
min_move = BFS(1, 0)
print(min_move)
from collections import deque
import sys
input = sys.stdin.readline

MAX = 500_000
INIT, EVEN = -1, 0


def bfs(start: int) -> list:
    visited = [[INIT, INIT] for _ in range(MAX+1)]
    visited[start][EVEN] = 0
    
    Q = deque([(start, 0)])
    while Q:
        cur_x, sec = Q.popleft()
        
        for dx in [1, -1, cur_x]:
            nx = cur_x + dx
            
            # out of bound or already visited
            if nx < 0 or nx > MAX or visited[nx][(sec+1) % 2] != INIT:
                continue
            
            Q.append((nx, sec+1))
            visited[nx][(sec+1) % 2] = sec + 1
    
    return visited


old, young = map(int, input().split())
visited = bfs(old)

answer = -1
for second, i in enumerate(range(MAX+1)):
    young += i
    
    # end condition, out of bound
    if young > MAX:
        break
    
    # end condition, find out
    if visited[young][second % 2] <= second:
        answer = second
        break
    
print(answer)
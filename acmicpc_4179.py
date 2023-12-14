# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(maze, visited, person, fire_location):
    Q = deque([person, *fire_location])
    
    while Q:
        x, y, state, move = Q.popleft()
        
        # fire catch up the person
        if state == "J" and visited[x][y] == "F":
            continue
        
        # RGT, LFT, DN, UP
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            
            # out of range
            if nx < 0 or ny < 0 or nx >= row or ny >= col:
                
                # person can escape
                if state == "J":
                    return move + 1
                    
                # otherwise, out of range
                continue
                
            # person move
            if maze[nx][ny] == "." and not visited[nx][ny]:
                Q.append((nx, ny, state, move+1))
                visited[nx][ny] = "J"
                
            # person move first, but fire can also move
            if state == "F" and visited[nx][ny] == "J" and not maze[nx][ny] == "#":
                Q.append((nx, ny, state, move+1))
                visited[nx][ny] = "F"
    
    return "IMPOSSIBLE"

# ---------- Main ----------
row, col = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(row)]

# define global var
visited = [[] for _ in range(row)]
fire_location = []
person = 0

# Init
for r in range(row):
    for c in range(col):
        
        # can move
        if maze[r][c] == ".":
            visited[r].append(0)
            continue
        
        # can not move
        visited[r].append(1)
        
        # person location
        if maze[r][c] == "J":
            person = (r, c, "J", 0)
            continue
        
        # fire location
        # there is no condition: fire is only one
        if maze[r][c] == "F":
            fire_location.append((r, c, "F", 0))
            
answer = BFS(maze, visited, person, fire_location)
print(answer)
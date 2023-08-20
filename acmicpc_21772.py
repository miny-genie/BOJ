# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def DFS(x, y, move, eat_count):
    global max_answer
    
    if time == move:
        max_answer = max(max_answer, eat_count)
        return
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < row and 0 <= ny < col:
            if graph[nx][ny] == "#":
                continue
            
            elif graph[nx][ny] == ".":
                DFS(nx, ny, move + 1, eat_count)
            
            elif graph[nx][ny] == "S":
                graph[nx][ny] = "."
                DFS(nx, ny, move + 1, eat_count + 1)
                graph[nx][ny] = "S"


# ---------- Main ----------
row, col, time = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(row)]
G = [(x, y) for x in range(row) for y in range(col) if graph[x][y] == "G"]

max_answer = 0
graph[G[0][0]][G[0][1]] = "."

DFS(G[0][0], G[0][1], 0, 0)
print(max_answer)

# ---------- Comment ----------
# Add condition: (dx, dy) - (0, 0)
# L39 add: graph[G[0][0]][G[0][1]] = "#"
# L22, L24 remove: can go where 'G' went
# L39 remove: graph[G[0][0]][G[0][1]] = "#"
# Remove condition: (dx, dy) - (0, 0)
# L42 add: 'G' location can move
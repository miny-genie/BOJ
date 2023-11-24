# ---------- Import ----------
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# ---------- Function ----------
def DFS(x, y, dist):
    global max_move
    max_move = max(max_move, dist)
    
    move = int(graph[x][y])

    for nx, ny in [(x+move, y), (x-move, y), (x, y+move), (x, y-move)]:
        if 0 <= nx < row and 0 <= ny < col and\
        graph[nx][ny] != "H" and dist + 1 > dp[nx][ny]:
        
            if visited[nx][ny] == False:
                dp[nx][ny] = dist + 1
                visited[nx][ny] = True
                DFS(nx, ny, dist + 1)
                visited[nx][ny] = False
                
            else:
                print(-1)
                exit()
            
# ---------- Main ----------
row, col = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(row)]

visited = [[False] * col for _ in range(row)]
dp = [[0] * col for _ in range(row)]
visited[0][0] = True
dp[0][0] = 1

max_move = -1
DFS(0, 0, 1)
print(max_move)
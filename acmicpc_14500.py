# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def doMakeTetromino(visited: list, x: int, y: int, blockCnt: int, totalValue: int) -> int:
    global result
    
    # End condition 1) sum of all elements(for MAX) is smaller than result
    if result >= totalValue + MAX * (4-blockCnt):
        return 
    
    # End condition 2) success tetromino
    if blockCnt == 4:
        result = max(result, totalValue)
        return
    
    # Checking 4 directions by backtracking
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        
        # Whether include, and not visited
        if 0<=nx<row and 0<=ny<col and visited[nx][ny]==0:
            
            # Shape ㅗ, ㅜ, ㅓ, ㅏ
            if blockCnt == 2:
                visited[nx][ny] = 1
                doMakeTetromino(visited,x, y, blockCnt+1, totalValue+INPUT[nx][ny])
                visited[nx][ny] = 0
                
            # Other shapes
            visited[nx][ny] = 1
            doMakeTetromino(visited, nx, ny, blockCnt+1, totalValue+INPUT[nx][ny])
            visited[nx][ny] = 0


# ---------- Main ----------
row, col = map(int, input().split())
INPUT = [list(map(int, input().split())) for _ in range(row)]

# UP, DN, LFT, RGT
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0 for _ in range(col)] for _ in range(row)]
result = 0
MAX = max(map(max, INPUT))

for r in range(row):
    for c in range(col):
        visited[r][c] = 1
        doMakeTetromino(visited, r, c, 1, INPUT[r][c])
        visited[r][c] = 0
        
print(result)
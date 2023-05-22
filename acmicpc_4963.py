# ---------- Import ----------
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# ---------- Function ----------
def DFS(X, Y):
    if X < 0 or X >= row or Y < 0 or Y >= col:
        return False
    
    if paper[X][Y] == 1:
        paper[X][Y] = 0
        DFS(X-1, Y)     # U
        DFS(X+1, Y)     # D
        DFS(X, Y-1)     # L
        DFS(X, Y+1)     # R
        
        DFS(X-1, Y-1)   # UL
        DFS(X-1, Y+1)   # UR
        DFS(X+1, Y-1)   # DL
        DFS(X+1, Y+1)   # DR
        
        return True      
        
    return False

# ---------- Main ----------
while True:
    col, row = map(int, input().split())
    
    if row == 0 and col == 0:
        break
    
    paper = [list(map(int, input().split())) for _ in range(row)]
    
    cntLand = 0
    for x in range(row):
        for y in range(col):
            if DFS(x, y):
                cntLand += 1
                
    print(cntLand)
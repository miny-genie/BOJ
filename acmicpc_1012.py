# ---------- Import ----------
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# ---------- Function ----------
def DFS(x, y):
    if x < 0 or y < 0 or x >= row or y >= col:
        return False
    
    if graph[x][y]:
        graph[x][y] = 0
        DFS(x+1, y)
        DFS(x-1, y)
        DFS(x, y+1)
        DFS(x, y-1)
        
        return True
    
    return False

# ---------- Main ----------
caseT = int(input())

for _ in range(caseT):
    col, row, cabbage = map(int, input().split())
    graph = [[0] * col for _ in range(row)]
    
    for _ in range(cabbage):
        Y, X = map(int, input().split())
        graph[X][Y] = 1

    cnt = 0
    for r in range(row):
        for c in range(col):
            if DFS(r, c):
                cnt += 1
                
    print(cnt)
# ---------- Import ----------
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)    # max is 100 * 100

# ---------- Function ----------
def DFS(x, y):
    global cnt
    
    if 0<=x<row and 0<=y<col and graph[x][y] == 0:
        cnt += 1
        graph[x][y] = 1
        DFS(x-1, y)
        DFS(x+1, y)
        DFS(x, y-1)
        DFS(x, y+1)
        
        return True    
    return False

# ---------- Main ----------
row, col, caseT = map(int, input().split())
graph = [[0]*col for _ in range(row)]

# Input case
for _ in range(caseT):
    startY, startX, endY, endX = map(int, input().split())

    # Initialization graph
    for r in range(startX, endX):
        for c in range(startY, endY):
            graph[r][c] = 1

# Checking all graph by DFS
result = []

for x in range(row):
    for y in range(col):
        cnt = 0
        if DFS(x, y): result.append(cnt)
        
# Printing Answer
result.sort()
print(len(result))
print(*result)
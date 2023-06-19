# ---------- Import ----------
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# ---------- Function ----------
def DFS(x, y, h):    
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    
    if height[x][y] > h and isSink[x][y] == 0:
        isSink[x][y] = 1
        DFS(x, y+1, h)
        DFS(x, y-1, h)
        DFS(x+1, y, h)
        DFS(x-1, y, h)
        
        return True
    
    return False

# ---------- Main ----------
N = int(input())
height = [list(map(int, input().split())) for _ in range(N)]
MAX = max(map(max, height))

result = 1
for level in range(1, MAX):
    isSink = [[0]*N for _ in range(N)]   
     
    cnt = 0
    for row in range(N):
        for col in range(N):
            if height[row][col] > level and not isSink[row][col]:
                cnt += 1
                DFS(row, col, level)
                        
    result = max(result, cnt)
    
print(result)

# ---------- Comment ----------
# 백준 4963번 섬의 개수 문제 참고
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def prefixsum(arr2d, row, col):
    dp = [[0]*(col+1) for _ in range(row+1)]
    
    for r in range(row):
        for c in range(col):
            dp[r+1][c+1] = arr2d[r][c] + dp[r][c+1] + dp[r+1][c] - dp[r][c]
            
    return dp    

# ---------- Main ----------
row, col = map(int, input().split())
arr2d = [list(map(int, input().split())) for _ in range(row)]

arr2d = prefixsum(arr2d, row, col)

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1; y1 -= 1
    
    print(arr2d[x2][y2] - arr2d[x1][y2] - arr2d[x2][y1] + arr2d[x1][y1])
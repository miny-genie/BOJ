# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
row, col = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(row)]
dp = [[0 for _ in range(col+1)] for _ in range(row+1)]

for r in range(1, row+1):
    for c in range(1, col+1):
        
        max_dp = max(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
        
        dp[r][c] += max_dp + maze[r-1][c-1]
        
print(dp[row][col])
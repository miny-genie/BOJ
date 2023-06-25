# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
caseT = int(input())

for _ in range(caseT):
    col = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    
    dp = [[0] * (col+2) for _ in range(2)]
    for c in range(col):
        for r in range(2):
            if r == 0:
                dp[r][c+2] = sticker[r][c] + max(dp[1][c], dp[1][c+1])
                
            else:
                dp[r][c+2] = sticker[r][c] + max(dp[0][c], dp[0][c+1])
                
    print(max(map(max, dp)))
    
# ---------- Comment ----------
# 아이디어 참고
# https://chanhuiseok.github.io/posts/baek-9/
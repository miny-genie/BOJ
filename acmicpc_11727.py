# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def func(N):
    dp = [0] * (N+1)
    
    if N == 1: return 1
    
    dp[0], dp[1] = 1, 1
    for i in range(2, N+1):    
        dp[i] = dp[i-1] + 2*dp[i-2]
        
    return dp[N] % 10007

# ---------- Main ----------
N = int(input())
result = func(N)
print(result)
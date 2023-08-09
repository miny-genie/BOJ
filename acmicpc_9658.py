# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
dp = [0, 1, 0, 1]

if N <= 4:
    print("SK") if dp[N-1] else print("CY")
    
else:
    dp += [0] * (N-4)
    
    for i in range(4, N):
        if 0 in (dp[i-4], dp[i-3], dp[i-1]):
            dp[i] = 1
        
    print("SK") if dp[-1] else print("CY")

# ---------- Comment ----------
# L07: [1, 0, 1, 1] -> [0, 1, 0, 1]
# L19: print(dp[-1]) -> print("SK") if dp[-1] else print("CY")
# L09: N <= 4 -> N < 4
# L13: [0] * (N-4) -> [0] * (N-3)
# L09: ROLLBACK, L13: ROLLBACK
# L19: Indentation
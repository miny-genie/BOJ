# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def pinary(INPUT: int) -> int:
    dp = [0] * (N+1)

    dp[1] = 1
    if INPUT > 1: dp[2] = 1

    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[INPUT]


# ---------- Main ----------
N = int(input())
print(pinary(N))
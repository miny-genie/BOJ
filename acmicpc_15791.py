# ---------- Import ----------
from sys import stdin
input = stdin.readline

MOD = 1_000_000_007

# ---------- Function ----------
def power(base: int, exp: int) -> int:
    if exp == 1: return base
    
    tmp = power(base, exp // 2) % MOD
    
    if exp % 2: return tmp * tmp * base % MOD
    else: return tmp * tmp % MOD


def factorial(goal: int) -> list:
    dp = [0] * (goal+1)
    dp[1] = 1
    
    for i in range(2, goal+1):
        dp[i] = i * dp[i-1] % MOD
    
    return dp

# ---------- Main ----------
N, K = map(int, input().split())
dp = factorial(max(N, K))

UP = dp[N]
DN = dp[N-K] * dp[K] % MOD

print(UP * power(DN, MOD-2) % MOD)

# ---------- Comment ----------
# 11401번, 13977번, 15791번, 16134번 문제와 동일하다.
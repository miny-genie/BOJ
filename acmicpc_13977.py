# ---------- Import ----------
import sys
input = sys.stdin.readline

MOD = 1_000_000_007

# ---------- Function ----------
def power(a: int, n: int) -> int:
    if n == 0: return 1
    
    tmp = power(a, n//2)
    
    if n % 2: return tmp * tmp * a % MOD
    else: return tmp * tmp % MOD

# ---------- Main ----------
factorial = [1] * (4_000_000 + 1)
for i in range(2, 4_000_000 + 1):
    factorial[i] = factorial[i-1] * i % MOD
    
for _ in range(int(input())):
    N, K = map(int, input().split())

    UP = factorial[N]
    DN = factorial[N-K] * factorial[K] % MOD

    print(UP * power(DN, MOD-2) % MOD)

# ---------- Comment ----------
# 11401번, 16134번 문제와 동일하다.
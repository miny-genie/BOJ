# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def factorial(n: int) -> int:
    global dp
    
    if n == 0 or n == 1:
        return 1
    
    if dp[n]:
        return dp[n]
    else:
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = i * dp[i-1] % MOD
            
    return dp[n]


def power(a: int, n: int) -> int:
    if n == 0:
        return 1
    
    tmp = power(a, n//2)
    
    if n % 2 == 0:
        return tmp * tmp % MOD
    else:
        return tmp * tmp * a % MOD

# ---------- Main ----------
N, K = map(int, input().split())
MOD = 1000000007
dp = [0] * (N+1)    # 팩토리얼 계산용 dynamic programming 리스트

numerator = factorial(N)    # 분자
denominator = factorial(N-K) * factorial(K) % MOD   # 분모

# 페르마의 소정리 이용
print(numerator * power(denominator, MOD-2) % MOD)

# ---------- Comment ----------
# 11401번, 13977번, 15791번, 16134번 문제와 동일하다.

# 페르마의 소정리 : 정수 a와 P가 있을 때, 다음을 만족한다.
# a^P ≡ a mod P
# a^(P-1) ≡ 1 mod P
# a^(P-2) ≡ a^(-1) mod P

# 이항 계수 (N, K) : 정수 N과 K가 있을 때, 다음을 만족한다.
# N! / (N-K)! * K!
# N! * ((N-K)! * K!)^(-1)

# 우리는 이항 계수의 값을 MOD = 1,000,000,007로 나눈 나머지를 구해야 한다.
# 즉 ((N-K)! * K!) 부분을 a라고 할 때, a^(P-2) ≡ a^(-1) mod P에 따라서
# (N-K)! * K!) ^ (MOD - 2)를 구하면 된다. (이후 분자 N!를 곱해야 한다.)
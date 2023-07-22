# -------------------- Case 1 --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def DP(N):
	if N == 1:
		return 10
		
	else:
		dp = [1 for _ in range(10)]
		
		for _ in range(2, N+1):
			for i in range(1, 10):
				dp[i] += dp[i-1]
				
		return sum(dp)

# ---------- Main ----------
N = int(input())
result = DP(N)
print(result % 10007)


# -------------------- Case 2 --------------------
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
N = int(input()) + 9
K = 9
MOD = 10_007
dp = [0] * (N+1)    # 팩토리얼 계산용 dynamic programming 리스트

numerator = factorial(N)    # 분자
denominator = factorial(N-K) * factorial(K) % MOD   # 분모

# 페르마의 소정리 이용
print(numerator * power(denominator, MOD-2) % MOD)
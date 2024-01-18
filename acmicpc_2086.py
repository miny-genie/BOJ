# ---------- Import ----------
from sys import stdin
input = stdin.readline


# ---------- Function ----------
def mulMatrix(A: list, B: list) -> list:
    N = 2
    result = [[0]*N for _ in range(N)]
    
    for m in range(N):
        for n in range(N):
            for k in range(N):
                result[m][n] += A[m][k] * B[k][n]
            result[m][n] %= MOD
                
    return result


def power(base, exponent):
    if exponent == 1:
        return base
    
    tmp = power(base, exponent // 2)
    
    if exponent % 2:
        return mulMatrix(mulMatrix(tmp, tmp), base)
    else:
        return mulMatrix(tmp, tmp)


def fibonacci(N):
    result = power([[1, 1], [1, 0]], N)
    return mulMatrix(result, [[1, 0],[0, 0]])[1][0] % MOD


# ---------- Main ----------
small, big = map(int, input().split())
MOD = 1_000_000_000

big = fibonacci(big+2)
small = fibonacci(small+1)
print((big - small) % MOD)

# ---------- Comment ----------
# big = fibonacci(big+2) - 1
# small = fibonacci(small+1) - 1
# big - small   = fibonacci(big+2) - 1 - (fibonacci(small+1) - 1)
#               = fibonacci(big+2) - fibonacci(small+1)
# so can skip intercept
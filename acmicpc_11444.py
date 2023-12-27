# ---------- Import ----------
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

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


# ---------- Main ----------
N = int(input())
oneMatrix, MOD = [[1, 1], [1, 0]], 1000000007

tmpResult = power(oneMatrix, N)
result = mulMatrix(tmpResult, [[1, 0],[0, 0]])

print(result[1][0])

# ---------- Comment ----------
# 1160번, 2749번, 11444번, 15712번의 매커니즘은 동일하다.
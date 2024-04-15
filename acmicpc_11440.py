from sys import stdin
input = stdin.readline

MOD = 1_000_000_007


def mul_matrix(A: list, B: list) -> list:
    N = 2
    result = [[0]*N for _ in range(N)]
    
    for m in range(N):
        for n in range(N):
            for k in range(N):
                result[m][n] += A[m][k] * B[k][n]
            result [m][n] %= MOD
    
    return result


def matrix_power(base: list, exp: int) -> list:
    if exp == 1: return base
    
    tmp = matrix_power(base, exp // 2)
    
    if exp % 2:
        return mul_matrix(mul_matrix(tmp, tmp), base)
    else:
        return mul_matrix(tmp, tmp)


fibo = int(input())
ans = matrix_power([[1, 1], [1, 0]], fibo)
print(ans[0][0] * ans[1][0] % MOD)
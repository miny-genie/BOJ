# ---------- Import ----------
import sys
input = sys.stdin.readline


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
MOD, coef, intercept, first, nth, FINAL = map(int, input().split())

first  = [[first, 1], [0, 0]]
matrix = [[coef, 0], [intercept, 1]]

answer = mulMatrix(first, power(matrix, nth))
print(answer[0][0] % FINAL)

# ---------- Comment ----------
# 1160번, 2749번, 11444번, 15712번의 매커니즘은 동일하다.
# https://memoacmicpc.tistory.com/entry/%EB%B0%B1%EC%A4%80-1160%EB%B2%88-Random-Number-Generator
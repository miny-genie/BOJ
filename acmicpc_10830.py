# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def multiplyMatrix(A: list, B: list) -> list:
    N = len(A)
    result = [[0]*N for _ in range(N)]
    
    for m in range(N):
        for n in range(N):
            for k in range(N):
                result[m][n] += A[m][k] * B[k][n]
            result[m][n] %= MOD
                
    return result
    
    
def power(base, exponent):
    if exponent == 1:
        for row in range(len(base)):
            for col in range(len(base)):
                base[row][col] %= 1000  
        return base
    
    tmp = power(base, exponent // 2)
    
    if exponent % 2:
        return multiplyMatrix(multiplyMatrix(tmp, tmp), base)
    else:
        return multiplyMatrix(tmp, tmp)


# ---------- Main ----------
N, POW = map(int, input().split())
MOD = 1000
matrix = [list(map(int, input().split())) for _ in range(N)]

result = power(matrix, POW)
for v in result:
    print(*v)
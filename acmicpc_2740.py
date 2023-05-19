# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N, M = map(int, input().split())
matrixA = []
for _ in range(N):
    matrixA.append(list(map(int, input().split())))

M, K = map(int, input().split())
matrixB = []
for _ in range(M):
    matrixB.append(list(map(int, input().split())))
    
matrixSum = [[0]*K for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            matrixSum[n][k] += matrixA[n][m] * matrixB[m][k]
        
for row in matrixSum:
    for col in row:
        print(col, end=" ")
    print()
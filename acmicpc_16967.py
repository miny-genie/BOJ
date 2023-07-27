# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H + X)]
A = [B[i][:W] for i in range(H)]

for i in range(H):
    for j in range(W):
        if i >= X and j >= Y:
            A[i][j] -= A[i-X][j-Y]

for i in A: print(*i)
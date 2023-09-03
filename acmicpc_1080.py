# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def reverse_matrix(r, c):
    global A
    
    for x in range(r, r+3):
        for y in range(c, c+3):
            A[x][y] ^= 1

# ---------- Main ----------
row, col = map(int, input().split())
A = [list(map(int, list(input().rstrip()))) for _ in range(row)]
B = [list(map(int, list(input().rstrip()))) for _ in range(row)]

count = 0

for r in range(row - 3 + 1):
    for c in range(col - 3 + 1):
        if A[r][c] != B[r][c]:
            reverse_matrix(r, c)
            count += 1
            
print(count) if A == B else print(-1)
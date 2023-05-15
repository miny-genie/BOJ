# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
sizeN, caseT = map(int, input().split())

# Initialization
arr = []
for _ in range(sizeN):
    arr.append(list(map(int, input().split())))

# Prefix Sum
PS = [[0] * (sizeN+1) for _ in range(sizeN+1)]
for r in range(1, sizeN+1):
    for c in range(1, sizeN+1):
        PS[r][c] =  arr[r-1][c-1] + PS[r-1][c] + PS[r][c-1] - PS[r-1][c-1]

# Calculation
for _ in range(caseT):
    x1, y1, x2, y2 = map(int, input().split())
    
    result = PS[x2][y2] - PS[x1-1][y2] - PS[x2][y1-1] + PS[x1-1][y1-1]
    print(result)
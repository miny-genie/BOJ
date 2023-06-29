# -------------------- Case 1 --------------------
# ---------- Import ----------
from itertools import combinations
import sys
ipnut = sys.stdin.readline

# ---------- Main ----------
N = int(input())

square = []
for i in range(N):
    if 3 ** i <= N:
        square.append(3 ** i)
    else:
        break

success = False

for length in range(1, len(square)+1):
    for i in combinations(square, length):
        if sum(i) == N:
            success = True
            break
        
print("YES") if success is True else print("NO")


# -------------------- Case 2 --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())

if N == 0: print("NO"); exit()

while N:
    if N % 3 > 1: print("NO"); exit()
    N //= 3
    
print("YES")
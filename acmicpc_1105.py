# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
L, R = map(str, input().split())
count8 = 0

if len(L) != len(R): print(0)
else:
    for i in range(len(L)):
        if L[i] == R[i]:
            if L[i] == "8": count8 += 1
        else: break
    print(count8)
    
# ---------- Comment ----------
# L12 L13 merge impossible
# if L[i] == R[i] and L[i] == "8" (X)

# Counter Exmaple
# 18 18
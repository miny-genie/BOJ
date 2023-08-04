# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
caseT = int(input())

for _ in range(caseT):
    N = int(input())
    
    result, squ5 = 0, 5
    while squ5 <= N:
        result += N // squ5
        squ5 *= 5
        
    print(result)
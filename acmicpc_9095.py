# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def sum123(num):
    if num == 1:
        return 1
    
    if num == 2:
        return 2
    
    if num ==3:
        return 4
    
    return sum123(num-1) + sum123(num-2) + sum123(num-3)
    
# ---------- Main ----------
T = int(input())

for _ in range(T):
    print(sum123(int(input())))
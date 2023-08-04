# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def Z(length, x, y, total):
    mid = int(length / 2)
    value = mid ** 2
    
    if length <= 1:             # End Condition
        return total
    
    if x < mid and y < mid:     # Quadrant 1
        total = Z(mid, x, y, total)
        
    elif x < mid and y >= mid:  # Quadrant 2
        total = Z(mid, x, y - mid, total + (value * 1))
        
    elif x >= mid and y < mid:  # Quadrant 3
        total = Z(mid, x - mid, y, total + (value * 2))
        
    else:                       # Quadrant 4
        total = Z(mid, x - mid, y - mid, total + (value * 3))
        
    return total
        
# ---------- Main ----------
N, row, col = map(int, input().split())
result = Z(2**N, row, col, 0)
print(result)
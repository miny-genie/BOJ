# ---------- Import ----------
import sys
#import time
input = sys.stdin.readline

# ---------- Function ---------
def POW(A, B, C):
    if B == 1:
        return A % C
    
    tmp = POW(A, B//2, C)
    if B % 2 == 0:
        return (tmp * tmp % C)
    else:
        return (tmp * tmp * A % C)

# ---------- Main ----------
A, B, C = map(int, input().split())

# s = time.perf_counter()
result = POW(A, B, C)
# e = time.perf_counter()
print(result)
#print(e-s)
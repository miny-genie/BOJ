# ---------- Import ----------
from cmath import exp, pi
import sys

input = sys.stdin.readline
POWER_TWO = 131_072

# ---------- Function ----------
def FFT(a: list, inverse: int) -> list:
    N = len(a)
    if N == 1: return a
    
    even = FFT(a[0::2], inverse)
    odd  = FFT(a[1::2], inverse)

    w_N = [exp(inverse*2j*pi*n/N) for n in range(N//2)]
        
    frt = [even[i] + w_N[i] * odd[i] for i in range(N//2)]
    bck = [even[i] - w_N[i] * odd[i] for i in range(N//2)]
    return frt + bck

# ---------- Main ----------
UP  = int(input())
UP_holes  = list(map(lambda x: int(x)+30_000, input().split()))

UP_plynm = [0] * POWER_TWO
for i in UP_holes:
    UP_plynm[i] = 1
UP_plynm = FFT(UP_plynm, 1)

MID = int(input())
MID_holes = list(map(lambda x: int(x)+30_000, input().split()))

DN  = int(input())
DN_holes  = list(map(lambda x: int(x)+30_000, input().split()))

DN_plynm = [0] * POWER_TWO
for i in DN_holes:
    DN_plynm[i] = 1
DN_plynm = FFT(DN_plynm, 1)

mul  = [UP_plynm[i]*DN_plynm[i] for i in range(POWER_TWO)]
IFFT = FFT(mul, -1)

count = 0
for isExist in MID_holes:
    value = round(IFFT[isExist*2].real)//(POWER_TWO)
    if value:
        count += value
print(count)

# ---------- Comment ----------
# https://suhwanc.tistory.com/163
# https://koosaga.com/263
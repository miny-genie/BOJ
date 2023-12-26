# https://blog.naver.com/PostView.naver?blogId=kks227&logNo=221633584963&proxyReferer=https:%2F%2Fwelog.tistory.com%2F
# https://tistory.joonhyung.xyz/6
from cmath import exp, pi
import sys

input = sys.stdin.readline
POWER_TWO = 524_288


def FFT(a: list, inverse: int) -> list:
    N = len(a)
    if N == 1: return a
    
    even = FFT(a[0::2], inverse)
    odd  = FFT(a[1::2], inverse)

    w_N = [exp(inverse*2j*pi*n/N) for n in range(N//2)]
        
    frt = [even[i] + w_N[i] * odd[i] for i in range(N//2)]
    bck = [even[i] - w_N[i] * odd[i] for i in range(N//2)]
    return frt + bck


# Init
polynomial = [0] * POWER_TWO

# Input N: Bot's distances
polynomial[0] = 1
for _ in range(int(input())):
    polynomial[int(input())] = 1
    
# FFT
polynomial = FFT(polynomial, 1)

# Convolution: square each elements that after fft
for i in range(POWER_TWO):
    polynomial[i] *= polynomial[i]
    
# IFFT
polynomial = FFT(polynomial, -1)
        
# If value is not 0, that can be shoot
count = 0
for _ in range(int(input())):
    if round(polynomial[int(input())].real):
        count += 1
        
print(count)
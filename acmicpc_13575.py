# ---------- Import ----------
from cmath import exp, pi
import sys
input = sys.stdin.readline

# ---------- Function ----------
def FFT(nums, inverse):
    N = len(nums)
    if N == 1: return nums
    
    even = FFT(nums[0::2], inverse)
    odd  = FFT(nums[1::2], inverse)
        
    w_N = [exp(inverse*2j*pi*i/N) for i in range(N//2)]
    
    frt = [even[i] + w_N[i] * odd[i] for i in range(N//2)]
    bck = [even[i] - w_N[i] * odd[i] for i in range(N//2)]
    return frt + bck


def Multiply(A, B):
    return [A[i] * B[i] for i in range(len(A))]


def Divide_n_Conquer(base, exp):
    if exp == 1:
        return base
    
    tmp = Divide_n_Conquer(base, exp // 2)
    
    if exp % 2:
        return Multiply(Multiply(tmp, tmp), base)
    else:
        return Multiply(tmp, tmp)
    

# ---------- Main ----------
nums = list(map(int, input().split()))

length = 1 << (max(nums).bit_length()+3)
degree = [0] * length

for num in nums:
    degree[num] = 1    
    
fft = FFT(degree, 1)
pow10 = Divide_n_Conquer(fft, 100)

ifft = FFT(pow10, -1)
answer = [i for i, v in enumerate(ifft) if round(v.real)]

print(*answer)
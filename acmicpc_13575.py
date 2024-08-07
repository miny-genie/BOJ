# ---------- Import ----------
from cmath import exp, pi
import sys

input = sys.stdin.readline
POWER_TWO = 1_048_576


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
    # return [1 if round((A[i] * B[i]).real) else 0 for i in range(len(A))]
    return [A[i]*B[i] for i in range(len(A))]


def Divide_n_Conquer(base, exp):
    if exp == 1:
        return base
    
    tmp = Divide_n_Conquer(base, exp // 2)
    
    if exp % 2:
        return Multiply(Multiply(tmp, tmp), base)
    else:
        return Multiply(tmp, tmp)
    

# ---------- Main ----------
_, power = map(int, input().split())
nums = list(map(int, input().split()))

# nums = "293 943 561 845 735 631 849 809 233 505 276 697 590 227 179 479 45 74 988 897 207 521 99 852 718 493 403 153 265 548 158 298 738 865 562 966 142 145 415 540 126 992 161 249 82 404 586 501 678 286 757 165 629 242 770 610 842 316 820 101 649 181 39 341 647 498 623 22 444 626 466 555 266 80 616 970 841 65 863 565 968 122 850 531 363 231 366 451 511 934 994 927 259 797 509 385 313 545 783 361 585 371 750 987 325 599 753 211 198 570 21 806 971 353 59 283 864 281 119 985 536 432 972 879 734 596 294 23 438 112 117 766 258 815 144 28 808 452 267 378 188 984 634 859 930 932 800 442 729 373 306 640 358 908 979 898 417 525 296 191 986 311 299 441 133 423 553 961 477 963 472 847 641 723 871 976 474 681 722 885 632 430 922 608 251 381 967 571 512 657 253 427 57 535 1000 141 811 896 11 225 990 182 523 791 309 906 268 271 819 891 152 329 450 802 907 413 78 776 567 947 345 128 285 192 367 194 202 212 237 464 989 515 91 478 219 398 503 97 627 280 924 248 284 420 376 804 431 911 14 159 495 121 177 263 969 394 746 20 315 484 686 557 54 149 866 774 899 125 240 944 749"
# nums = list(map(int, nums.split(" ")))

degree = [0] * POWER_TWO
for num in nums:
    degree[num] = 1
    
fft = FFT(degree, 1)
powN = Divide_n_Conquer(fft, power)

ifft = FFT(powN, -1)
print(ifft)
answer = [i for i, v in enumerate(ifft) if round(v.real)]

print(*answer)
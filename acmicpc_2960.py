# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N, K = map(int, input().split())
nums = [i for i in range(2, N+1)]

cnt = 0
using = [0 for _ in range(2, N+1)]

while True:
    # Condition No.2
    for i, v in enumerate(using):
        if v == 0:
            num = nums[i]
            break
        
    for i, v in enumerate(nums):
        # Condition No.3
        if v % num == 0:
            if using[i] == 0:
                using[i] = 1
                cnt += 1
                
            # cnt is same K, then print and exit
            if cnt == K:
                print(v)
                exit()
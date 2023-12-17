# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
nums = list(map(int, input().split()))
X = int(input())

nums_dict = {num:i for i, num in enumerate(nums)}

count = 0
for i, num in enumerate(nums):
    if X-num in nums_dict and i < nums_dict[X-num]:
        count += 1
        
print(count)
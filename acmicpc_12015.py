# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def find_index(num: int, LIS: list) -> int:
    left = 0
    right = len(LIS)

    while left <= right:
        mid = (left + right) // 2

        if LIS[mid] == num: return mid
        elif LIS[mid] < num: left = mid + 1
        else: right = mid - 1

    return left

# ---------- Main ----------
N = int(input())
nums = list(map(int, input().split()))

LIS = [0]
for num in nums:
    if LIS[-1] < num:
        LIS.append(num)
    else:
        idx = find_index(num, LIS)
        LIS[idx] = num
        
print(len(LIS) - 1)
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def TwoPointers(length: int, nums: list) -> int:
    check = set()
    count, ep = 0, 1
        
    for sp in range(length):
        while (ep < length) and (nums[ep] not in check):
            check.add(nums[ep])
            count += ep - sp + 1
            ep += 1
        
        check.remove(nums[sp])
        sp += 1
        
    return count

# ---------- Main ----------
length = int(input())
nums = list(map(int, input().split()))

answer = TwoPointers(length, nums)
print(answer)
# ---------- Import ----------
from sys import stdin
input = stdin.readline

# ---------- Function ----------
def solution(nums: list, GOAL: int) -> int:
    shortest = 100_001
    total, count = 0, 0
    
    end = 0
    for start in range(len(nums)):
        while end < len(nums) and total < GOAL:
            total += nums[end]
            count += 1
            end += 1
            
        if total >= GOAL:
            shortest = min(shortest, count)
            
        total -= nums[start]
        count -= 1
    
    if shortest == 100_001: shortest = 0
    return shortest

# ---------- Main ----------
_, length = map(int, input().split())
nums = list(map(int, input().split()))

answer = solution(nums, length)
print(answer)
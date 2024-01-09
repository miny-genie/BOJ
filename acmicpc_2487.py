import sys
input = sys.stdin.readline

stage = int(input())
nums = [int(input()) for _ in range(stage)]

minus = 0
goal = nums[-1] - 1

for i in range(stage-2, -1, -1):    
    if goal < nums[i]:
        minus += nums[i] - goal
        
    goal = min(nums[i] - 1, goal - 1)
    
print(minus)
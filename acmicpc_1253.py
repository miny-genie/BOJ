from sys import stdin
input = stdin.readline


def find_pair(goal: int, nums: list[int]) -> bool:
    lft, rgt = 0, len(nums)-1
    
    while lft < rgt:
        cur_sum = nums[lft] + nums[rgt]
        if cur_sum == goal: return True
        elif cur_sum < goal: lft += 1
        else: rgt -= 1
        
    return False


_ = int(input())
nums = sorted(map(int, input().split()))
answer = sum(
    find_pair(num, nums[:idx] + nums[idx+1:])
    for idx, num in enumerate(nums)
)
print(answer)
from sys import stdin
input = stdin.readline


def find_pH7(nums: list) -> tuple:
    pH_scale = float('inf')
    pH_pair = []
    
    left, right = 0, len(nums)-1
    while left < right:
        cur_pH_scale = nums[left] + nums[right]
        if abs(cur_pH_scale) < abs(pH_scale):
            pH_scale = cur_pH_scale
            pH_pair = [nums[left], nums[right]]
        
        if cur_pH_scale < 0:
            left += 1
        elif cur_pH_scale > 0:
            right -= 1
        else:
            return pH_pair
        
    return pH_pair


_ = int(input())
nums = list(map(int, input().split()))
pH7 = find_pH7(nums)
print(*pH7)
from sys import stdin
input = stdin.readline


def max_con_sum(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp_removed = [0] * len(nums)
    
    dp[0] = result = nums[0]
    dp_removed[0] = float('-inf')
    
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        dp_removed[i] = max(dp_removed[i-1] + nums[i], dp[i-1])
        result = max(result, dp[i], dp_removed[i])
    
    return result


_ = int(input())
nums = list(map(int, input().split()))

con_sum = max_con_sum(nums)
print(con_sum)

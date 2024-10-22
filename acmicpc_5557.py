from sys import stdin
input = stdin.readline


def count_valid_equations(num_count: int, nums: list[int]) -> int:
    dp = [[0] * 21 for _ in range(num_count - 1)]
    dp[0][nums[0]] = 1
    
    for cur_idx, cur_num in enumerate(nums[1:num_count-1], 1):
        bef_idx = cur_idx - 1
        for bef_num in range(21):
            if dp[bef_idx][bef_num]:
                if bef_num - cur_num >= 0:
                    dp[cur_idx][bef_num - cur_num] += dp[bef_idx][bef_num]
                if bef_num + cur_num <= 20:
                    dp[cur_idx][bef_num + cur_num] += dp[bef_idx][bef_num]
    
    return dp[-1][nums[-1]]


num_count = int(input())
nums = list(map(int, input().split()))
valid_equations = count_valid_equations(num_count, nums)
print(valid_equations)

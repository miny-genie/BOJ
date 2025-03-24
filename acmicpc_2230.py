from sys import stdin
input = stdin.readline


def get_min_diff(nums: list) -> int:
    left = 0
    min_diff = float('inf')
    
    for right in range(n):
        while left < n and (diff := nums[right] - nums[left]) >= k:
            min_diff = min(min_diff, diff)
            left += 1
    
    return min_diff


n, k = map(int, input().split())
nums = sorted(int(input()) for _ in range(n))

min_diff = get_min_diff(nums)
print(min_diff)

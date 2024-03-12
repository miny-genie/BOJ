from itertools import permutations


def formula(nums: list, limit: int) -> int:
    return sum(abs(nums[i] - nums[i+1]) for i in range(limit))


length = int(input())
nums = list(map(int, input().split()))

max_ans = float('-inf')
for perm in permutations(nums, length):
    max_ans = max(max_ans, formula(perm, length-1))
    
print(max_ans)
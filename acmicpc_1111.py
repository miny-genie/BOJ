from sys import stdin
input = stdin.readline


def is_valid(a: int, b: int, nums: list[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] * a + b != nums[i + 1]:
            return False
    return True


def find_next_num(num_count: int, nums: list[int]) -> str|int:
    if num_count == 1:
        return "A"
    
    if num_count == 2:
        if nums[0] == nums[1]:
            return nums[0]
        else:
            return "A"
    
    x0, x1, x2, *_ = nums
    if x1 - x0 == 0:
        a = 0
        b = x1
    
    else:
        if (x2 - x1) % (x1 - x0):
            return "B"
        else:
            a = (x2 - x1) // (x1 - x0)
            b = x1 - x0 * a
        
    if is_valid(a, b, nums):
        return nums[-1] * a + b
    else:
        return "B"


num_count = int(input())
nums = list(map(int, input().split()))

next_num = find_next_num(num_count, nums)
print(next_num)

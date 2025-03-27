from sys import stdin
input = stdin.readline


def find(length: int, nums: list[int|str]):
    max_sum = window_sum = sum(nums[:length])
    count = 1
    
    for in_idx in range(length, len(nums)):
        out_idx = in_idx - length
        window_sum = window_sum + nums[in_idx] - nums[out_idx]
        
        if window_sum == max_sum:
            count += 1
        
        elif window_sum > max_sum:
            max_sum = window_sum
            count = 1
       
    if max_sum == 0:
        return ["SAD"]
    else:
        return max_sum, count


_, length = map(int, input().split())
nums = list(map(int, input().split()))

ans = find(length, nums)
print(*ans, sep='\n')

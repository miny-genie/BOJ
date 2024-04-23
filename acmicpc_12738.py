from sys import stdin
input = stdin.readline


def find_lis(nums: list) -> int:
    from bisect import bisect_left
    
    n = len(nums)
    tails = []
    subseq = [-1] * n
    
    for i in range(n):
        index = bisect_left(tails, nums[i])
        if index == len(tails): tails.append(nums[i])            
        else: tails[index] = nums[i]
        subseq[index] = i
    
    return len(tails)


_ = int(input())
nums = list(map(int, input().split()))
answer = find_lis(nums)
print(answer)
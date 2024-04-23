from sys import stdin
input = stdin.readline


def find_lis(nums: list) -> tuple[int, list]:
    from bisect import bisect_left
    
    n = len(nums)
    tails = list()
    prev = [-1] * n
    subseq = [-1] * n
        
    for i in range(n):
        index = bisect_left(tails, nums[i])
        if index == len(tails):
            tails.append(nums[i])
        else:
            tails[index] = nums[i]
            
        if index:
            prev[i] = subseq[index - 1]
        subseq[index] = i
            
    k = subseq[len(tails) - 1]
    lis = list()
    while k != -1:
        lis.append(nums[k])
        k = prev[k]
    lis.reverse()
    
    return len(tails), lis

_ = int(input())
nums = list(map(int, input().split()))

length, lis = find_lis(nums)
print(length)
print(*lis)
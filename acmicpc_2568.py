from bisect import bisect_left
from sys import stdin
input = stdin.readline


def find_lis(nums: list) -> list:
    length = len(nums)
    tails = []
    prev = [-1] * length
    subseq = [-1] * length
    
    for i, num in enumerate(nums):
        index = bisect_left(tails, num)
        if index == len(tails):
            tails.append(num)
        else:
            tails[index] = num
            
        if index:
            prev[i] = subseq[index - 1]
        subseq[index] = i
    
    k = subseq[len(tails) - 1]
    lis = []
    while k != -1:
        lis.append(nums[k])
        k = prev[k]
    
    return lis[::-1]


nums = [list(map(int, input().split())) for _ in range(int(input()))]
pillar_A = [k1 for k1, _ in sorted(nums, key=lambda x: x[1])]
lis = find_lis(pillar_A)
answer = sorted(set(pillar_A) - set(lis))
print(len(answer), *answer, sep="\n")
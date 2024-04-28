from collections import defaultdict
from sys import stdin
input = stdin.readline


def calculate_all_subsequence(seq: list) -> dict:
    sums = defaultdict(int)
    length = len(seq)
    
    for subseq_digit in range(1, 2**length):
        total = 0
        for idx in range(length):
            if subseq_digit & (1 << idx):
                total += seq[idx]
        sums[total] += 1
    
    return sums


def solutions(goal: int, nums: list) -> int:
    if len(nums) == 1:
        return int(nums[0] == goal)

    half = len(nums) // 2
    total = 0
    
    fir_nums = nums[:half]
    fir_subseq = calculate_all_subsequence(fir_nums)
    if goal in fir_subseq:
        total += fir_subseq[goal]
    
    sec_nums = nums[half:]
    sec_subseq = calculate_all_subsequence(sec_nums)
    if goal in sec_subseq:
        total += sec_subseq[goal]
 
    for num, count in fir_subseq.items():
        check = goal - num
        if check in sec_subseq:
            total += count * sec_subseq[check]
        
    return total


_, goal  = map(int, input().split())
nums = list(map(int, input().split()))

answer = solutions(goal, nums)
print(answer)
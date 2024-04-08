from sys import stdin
input = stdin.readline


def next_perm(n: int, nums: list) -> list:
    # end condition 1) final permutation
    if nums[::-1] == [i for i in range(1, n+1)]:
        return [-1]
    
    # end condition 2) first permutation
    # 95% example
    elif nums == [i for i in range(1, n+1)]:
        return nums[:-2] + [nums[-1]] + [nums[-2]]
    
    # other permutations
    for idx in range(n-1, -1, -1):
        frt = nums[idx-1]
        cur = nums[idx]
        
        if frt < cur:
            for jdx in range(n-1, -1, -1):
                cur = nums[jdx]
                
                if frt < cur:
                    nums[idx-1], nums[jdx] = nums[jdx], nums[idx-1]
                    nums = nums[:idx] + sorted(nums[idx:])
                    return nums


n = int(input())
nums = list(map(int, input().split()))
ans = next_perm(n, nums)
print(*ans)
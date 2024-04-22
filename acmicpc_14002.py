from sys import stdin
input = stdin.readline


def find_lis(arr: list) -> tuple[int, list]:
    n = len(arr)
    dp = [1] * n
    parent = [-1] * n
    
    # store LIS length and preIndex
    for cur in range(1, n):
        for pre in range(cur):
            if arr[pre] < arr[cur] and dp[cur] < dp[pre] + 1:
                dp[cur] = dp[pre] + 1
                parent[cur] = pre
    
    #  find LIS length and start point
    lis_length = max(dp)
    lis_start = dp.index(lis_length)
    
    # tracking LIS
    lis = list()
    current = lis_start
    while current != -1:
        lis.append(arr[current])
        current = parent[current]
    lis.reverse()
        
    return lis_length, lis


_ = int(input())
nums = list(map(int, input().split()))
length, lis = find_lis(nums)
print(length)
print(*lis)
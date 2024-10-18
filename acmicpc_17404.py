from sys import stdin
input = stdin.readline


def compute_min_cost(house_count: int, rgb_info: list[list[int]]) -> int:
    dp = [[0] * 3 for _ in range(2)]
    min_cost = float('inf')
    
    for rgb in range(3):
        dp[0][0] = dp[0][1] = dp[0][2] = float('inf')
        dp[0][rgb] = rgb_info[0][rgb]
        
        for i in range(1, house_count):
            dp[1][0] = min(dp[0][1], dp[0][2]) + rgb_info[i][0]
            dp[1][1] = min(dp[0][0], dp[0][2]) + rgb_info[i][1]
            dp[1][2] = min(dp[0][0], dp[0][1]) + rgb_info[i][2]
            
            dp[0][0], dp[0][1], dp[0][2] = dp[1][0], dp[1][1], dp[1][2]
        
        min_cost = min(min_cost, dp[0][(rgb + 1) % 3], dp[0][(rgb + 2) % 3])
    
    return min_cost


house_count = int(input())
rgb_info = [list(map(int, input().split())) for _ in range(house_count)]
min_cost = compute_min_cost(house_count, rgb_info)
print(min_cost)

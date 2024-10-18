from sys import stdin
input = stdin.readline


def generate_count_ways() -> list:
    # dp[num][last_digit] = count
    num = 100_000
    dp = [[0] * 4 for _ in range(num+1)]
    
    # Initialization
    dp[1][0] = dp[1][1] = 1
    dp[2][0] = dp[2][2] = 1
    dp[3][1] = dp[3][2] = dp[3][3] = 1
    dp[3][0] = 3
    
    # dp
    mod = 1_000_000_009
    for i in range(4, num+1):
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % mod
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % mod
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % mod
        dp[i][0] = sum(dp[i]) % mod
    return dp


count_ways = generate_count_ways()
for _ in range(test_case := int(input())):
    num = int(input())
    print(count_ways[num][0])
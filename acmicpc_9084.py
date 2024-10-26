from sys import stdin
input = stdin.readline


def compute_all_case(n: int, coins: list[int], goal: int) -> int:
    dp = [0] * (goal + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, goal + 1):
            dp[i] += dp[i - coin]
    
    return dp[-1]


test_case = int(input())
for _ in range(test_case):
    n = int(input())
    coins = list(map(int, input().split()))
    goal = int(input())
    
    all_case = compute_all_case(n, coins, goal)
    print(all_case)
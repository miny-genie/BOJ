from sys import stdin
input = stdin.readline


def generate_case() -> list[int]:
    dp = [1] * (10000 + 1)
    for coin in [2, 3]:
        for i in range(coin, 10000 + 1):
            dp[i] += dp[i - coin]
    return dp


dp = generate_case()
for _ in range(int(input())):
    idx = int(input())
    print(dp[idx])

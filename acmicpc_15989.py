from sys import stdin
input = stdin.readline


def generate_case() -> list[int]:
    dp = [1] * 10001
    for coin in [2, 3]:
        for i in range(coin, 10001):
            dp[i] += dp[i - coin]
    return dp


nums = [int(input()) for _ in range(int(input()))]
dp = generate_case()

print(*[dp[num] for num in nums], sep='\n')


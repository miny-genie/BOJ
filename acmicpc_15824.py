from sys import stdin
input = stdin.readline

MOD = 1_000_000_007


def calculate_pain_sum(nums: list) -> int:
    return sum(
        (pow(2, i, MOD) - pow(2, len(nums)-1-i, MOD)) * num % MOD
        for i, num in enumerate(nums)
    ) % MOD


_ = int(input())
scovilles = sorted(map(int, input().split()))
pain_sum = calculate_pain_sum(scovilles)
print(pain_sum)
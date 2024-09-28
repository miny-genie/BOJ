from sys import stdin
input = stdin.readline


def generate_sum_comb() -> list:
    dp = [0, 1, 2, 4]
    for i in range(4, 1_000_000+1):
        ith_num = (dp[i-1] + dp[i-2] + dp[i-3]) % 1_000_000_009
        dp.append(ith_num)
    return dp


dp = generate_sum_comb()
for _ in range(test_case := int(input())):
    n = int(input())
    print(dp[n])
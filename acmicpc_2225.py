from sys import stdin
input = stdin.readline

MOD = 1_000_000_000

N, K = map(int, input().split())

# 0부터 N까지 숫자를 K개 사용하여, N을 만들 수 있는 가짓수
dp = [[0] * (K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(0, N+1):
    for j in range(1, K+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD

print(dp[-1][-1])
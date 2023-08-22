# # -------------------- Case 1: MLE --------------------
# # ---------- Import ----------
# import sys
# input = sys.stdin.readline

# # ---------- Main ----------
# N, K = map(int, input().split())
# coins = [int(input()) for _ in range(N)]

# dp = [[0] * (K+1) for _ in range(N+1)]

# for i in range(1, N+1): dp[i][0] = 1

# for i, coin in enumerate(coins, 1):
#     for k in range(1, K+1):
#         dp[i][k] += dp[i-1][k] + dp[i][k-coin]
        
# for line in dp:
#     print(line)

# # # print(sys.getsizeof(dp))


# -------------------- Case 2: AC --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

dp = [0] * (K+1)
dp[0] = 1

for coin in coins:
    for k in range(coin, K+1):
        dp[k] += dp[k-coin]

print(dp[-1])
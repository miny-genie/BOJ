from sys import stdin
input = stdin.readline

# input
count, K = map(int, input().split())
    
# init
dp = [float('inf')] * (K+1)
coins = []

# preprocess
for _ in range(count):
    coin = int(input())
    if coin > K: continue
    
    dp[coin] = 1
    coins.append(coin)
    
# dp
for idx in range(1, K+1):
    for coin in coins:
        if idx - coin > 0:
            dp[idx] = min(dp[idx], dp[idx-coin]+1)
    
print(dp[-1]) if isinstance(dp[-1], int) else print(-1)

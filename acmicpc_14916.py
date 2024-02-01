dp = [-1, -1, 1, -1, 2, 1]

n = int(input())

if n <= 5:
    print(dp[n])
    
else:
    dp += [-1] * (n-5)
    
    for i in range(6, n+1):
        if dp[i-2] != -1:
            dp[i] = dp[i-2] + 1
            
        if dp[i-5] != -1:
            dp[i] = dp[i-5] + 1
            
    print(dp[-1])
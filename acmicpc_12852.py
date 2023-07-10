# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def DP(N):
    dp = [i for i in range(N+1)]
    linkedList = [i for i in range(N+1)]
    
    dp[1], linkedList[1] = 0, 0
    
    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1
        linkedList[i] = i - 1
        
        if i % 2 == 0 and dp[i] > dp[i//2] + 1:
            dp[i] = min(dp[i], dp[i//2] + 1)
            linkedList[i] = i // 2            
            
        if i % 3 == 0 and dp[i] > dp[i//3] + 1:
            dp[i] = dp[i//3] + 1
            linkedList[i] = i // 3
    
    return dp[N], linkedList

# ---------- Main ----------
N = int(input())

dpResult, linkedList = DP(N)
print(dpResult)

print(N, end=" ")
while linkedList[N] != 0:
    print(linkedList[N], end=" "); N = linkedList[N]
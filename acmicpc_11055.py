# ---------- Main ----------
length = int(input())
nums = list(map(int, input().split()))

dp = [0] * length
isMax = [0] * length

for fir in range(length):
    for sec in range(fir):
        
        if nums[fir] > nums[sec] and dp[fir] < dp[sec]:
            dp[fir] = dp[sec]
            isMax[fir] = max(isMax[fir], isMax[sec])
            
    dp[fir] += 1
    isMax[fir] += nums[fir]
    
print(max(isMax))
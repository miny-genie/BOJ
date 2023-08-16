# ---------- Import ---------- 
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
if N == 1: print(0); exit()

dp = [0] * (N+1)
dp[2] = 1

for i in range(3, N+1):
    dp[i] = dp[i-1] + (dp[i-2] * 2)
    
print(dp[N] % 1000000007)

# ---------- Comment ----------
# count = 0
# N = int(input())
# for i in range(2**N):
#     isMul15 = int(str(bin(i)[2:].zfill(N)).replace("0", "5"))
#     if isMul15 % 15 == 0: count += 1
    
# print(count % 1000000007)
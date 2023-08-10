# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
length = int(input())
nums = list(map(int, input().split()))
caseT = int(input())

dp = [[0]*length for _ in range(length)]

# DP
for l in range(length):
    for start in range(length-l):
        end = start + l
        
        # str length is 1, than palidrome
        if start == end:
            dp[start][end] = 1
        
        # str length is longer than 1   
        elif nums[start] == nums[end]:
            
            # str length is 2, than palidrome
            if end - start == 1: dp[start][end] = 1
            
            # checking isPalidrome, out of side 2 str 
            elif dp[start+1][end-1]: dp[start][end] = 1        

# Answer
for _ in range(caseT):
    startIdx, endIdx = map(int, input().split())
    print(dp[startIdx-1][endIdx-1])
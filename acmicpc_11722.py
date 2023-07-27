# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
length = int(input())
lst = list(map(int, input().split()))
dp = [0 for _ in range(length)]

for each in range(length):
    for i in range(each):
        if lst[i] > lst[each] and dp[i] > dp[each]:
            dp[each] = dp[i]

    dp[each] += 1

print(max(dp))

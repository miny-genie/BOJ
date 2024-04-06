from sys import stdin
input = stdin.readline


def locate_lion(n: int) -> int:
    if n == 1: return 3
    dp = [1] + [0]*n
    dp[1] = 3
    
    for i in range(1, n):
        dp[i+1] = (dp[i] * 2 + dp[i-1]) % 9901
    
    return dp[-1]


n = int(input())
ans = locate_lion(n)
print(ans)
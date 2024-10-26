from sys import stdin
input = stdin.readline


def get_max_money(schedules: list[list[int]]) -> int:
    n = len(schedules)
    dp = [0] * (n + 1)
    
    for i, (time, pay) in enumerate(schedules):
        if i + time <= n:
            dp[i + time] = max(dp[i + time], dp[i] + pay)
            
        dp[i + 1] = max(dp[i + 1], dp[i])
    
    return dp[-1]
        

schedules = [list(map(int, input().split())) for _ in range(int(input()))]
max_money = get_max_money(schedules)
print(max_money)

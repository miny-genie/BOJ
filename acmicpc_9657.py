from sys import stdin
input = stdin.readline


def who_win(stones: int) -> str:
    dp = ["", "SK", "CY", "SK", "SK"]
    if stones <= 4:
        return dp[stones]
    
    for _ in range(stones - 4):
        if any(map(lambda x: dp[x] == "CY", [-1, -3, -4])):
            dp.append("SK")
        else:
            dp.append("CY")
    
    return dp[-1]


print(who_win(int(input())))

# ---------- Import ----------
import sys
input = sys.stdin.readline


# ---------- Function ----------
def Knapsack(kinds, money, calories, prices):
    dp = [0] * (money + 1)
    
    for max_money in range(1, money + 1):
        for i in range(kinds):
            cur_cal = calories[i]
            cur_pri = prices[i]

            if max_money >= cur_pri:
                compare1 = dp[max_money]
                compare2 = dp[max_money - cur_pri] + cur_cal
                dp[max_money] = max(compare1, compare2)
    
    return dp[-1]


# ---------- Main ----------
while True:
    kinds, money = map(float, input().split())
    if not (kinds + money): break
    
    kinds = int(kinds)
    money = int(money * 100 + 0.5)
    
    calories = []
    prices = []
    
    for _ in range(kinds):
        calorie, price = map(float, input().split())
        calories.append(int(calorie))
        prices.append(int(price * 100 + 0.5))
        
    answer = Knapsack(kinds, money, calories, prices)
    print(answer)
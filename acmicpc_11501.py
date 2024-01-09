import sys
input = sys.stdin.readline


def HTS(prices: list) -> int:
    money = 0
    top = prices[0]
    
    for price in prices:
        if top < price:
            top = price
            continue
        
        money += top - price   
    
    return money


for _ in range(int(input())):
    _ = int(input())
    prices = list(map(int, input().split()))
    prices.reverse()
    
    answer = HTS(prices)
    print(answer)
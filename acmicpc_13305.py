# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
cities = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
prices.pop()

current_price = 1e9

sum = 0
for i, v in enumerate(prices):    
    if current_price > v:
        current_price = v
    
    sum += distances[i] * current_price
    
print(sum)
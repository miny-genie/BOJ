# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
T = int(input())

for _ in range(T):
    money = int(input())
    
    Quarter, money = money // 25, money % 25
    Dime, money = money // 10, money % 10
    Nickel, money = money // 5, money % 5
    Penny = money
    
    print(Quarter, Dime, Nickel, Penny)
    
# ---------- Comment ----------
# Quarter   $0.25
# Dime      $0.10
# Nickel    $0.05
# Penny     $0.01
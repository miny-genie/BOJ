# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
YY = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MM, DD = map(int, input().split())

ans = 0
for index in range(MM - 1):
    ans += YY[index]
    
ans += DD
ans %= 7

print(day[ans])
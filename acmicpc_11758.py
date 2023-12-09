# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

angle = ((x2 - x1) * (y3 - y1)) - ((x3 - x1) * (y2 - y1))

if not angle: print(0)
elif angle > 0: print(1)
else: print(-1)

# ---------- Comment ----------
# https://snowfleur.tistory.com/98
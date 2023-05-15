# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
lst = [ input().rstrip() for _ in range(5) ]

for column in range(15):
    for row in range(5):
        if column < len(lst[row]):
            print(lst[row][column], end="")
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
count = 0

for row in range(8):
    for value in list(map(str, input().split())):
        for col, v in enumerate(value):
            if (row+col) % 2 == 0 and v == "F":
                count += 1
    
print(count)
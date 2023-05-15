# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
angle = []
for _ in range(3):
    angle.append(int(input()))

if not sum(angle) == 180:
    print("Error")
elif len(s := set(angle)) == 1:
    print("Equilateral")
elif len(set(angle)) == 2:
    print("Isosceles")
elif len(set(angle)) == 3:
    print("Scalene")

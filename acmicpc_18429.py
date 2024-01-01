# ---------- Import ----------
from itertools import permutations
import sys
input = sys.stdin.readline

# ---------- Main ----------
routine, muscle_loss = map(int, input().split())
muslce_gain = list(map(int, input().split()))

current_muscle = 500
safe = 0

print(list(permutations(muslce_gain, routine)))

for exercise in permutations(muslce_gain, routine):
    for gain in exercise:
        current_muscle = current_muscle + gain - muscle_loss
        if current_muscle < 500: break

    else:
        safe += 1
        
print(safe)
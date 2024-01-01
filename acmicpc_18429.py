# ---------- Import ----------
from itertools import permutations
import sys
input = sys.stdin.readline

# ---------- Main ----------
routine, muscle_loss = map(int, input().split())
muslce_gain = list(map(int, input().split()))

safe = 0

for exercise in permutations(muslce_gain, routine):
    current_muscle = 500
    for gain in exercise:
        current_muscle = current_muscle + gain - muscle_loss
        if current_muscle < 500: break

    else:
        safe += 1
        
print(safe)
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
how_many, how_long = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()

std = holes[0]
plug = [std]

for hole in holes:
    if hole >= std + how_long:
        plug.append(hole)
        std = hole
        
print(len(plug))
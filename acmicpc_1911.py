# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
caseT, woodLength = map(int, input().split())
water = [list(map(int, input().split())) for _ in range(caseT)]

water.sort(key = lambda x: x[0])
count = 0

currentIndex = 0
for start, end in water:
    if currentIndex <= start:
        currentIndex = start
    else:
        if currentIndex >= end: continue
    
    #print(currentIndex, start, end, count, end= " ")
    remainWater = end - currentIndex
    div, mod = divmod(remainWater, woodLength)
    #print(f'div {div} mod {mod}')
    
    count += div
    currentIndex += woodLength * div
    
    if mod: count += 1; currentIndex += woodLength
        
print(count)
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
while True:
    line = list(map(int, input().split()))
    line.sort()
    short, middle, long = line[0], line[1], line[2]
    
    if short == middle == long == 0:    break
    
    if long >= short + middle:
        print("Invalid")
        continue
    
    if len(set(line)) == 1:
        print("Equilateral")
        continue
        
    if len(set(line)) == 2:
        print("Isosceles")
        continue
        
    if len(set(line)) == 3:
        print("Scalene")
        continue
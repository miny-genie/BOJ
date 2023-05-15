# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
people = {"ChongChong" : True}

for _ in range(N):
    personA, personB = input().split()

    if personA in people:
        people[personB] = True
    
    if personB in people:
        people[personA] = True

print(len(people))
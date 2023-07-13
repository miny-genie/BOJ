# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
off = []
on = []

for _ in range(4):
    a, b = map(int, input().split())
    off.append(a)
    on.append(b)
    
current = on[0]
people = [on[0]]
for i in range(1, 4):
    current = current - off[i] + on[i]
    people.append(current)
    
print(max(people))
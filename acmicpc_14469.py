# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
times = [list(map(int, input().split())) for _ in range(int(input()))]
times.sort(key=lambda x: (x[0], x[1]))

time = 0
for arrive, spend in times:
    if time <= arrive: time = arrive + spend
    else: time += spend        
        
print(time)
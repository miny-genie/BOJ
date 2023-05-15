# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main ----------
caseT = int(input())
time = []

for _ in range(caseT):
    time.append(list(map(int, input().split())))

time.sort(key = lambda x: (x[1], x[0]))

cnt, last_time = 0, 0
for start, end in time:
    if start >= last_time:
        cnt += 1
        last_time = end

print(cnt)
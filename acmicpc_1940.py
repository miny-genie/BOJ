# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Main -----------
length = int(input())
GOAL = int(input())
nums = sorted(list(map(int, input().split())))

count = 0
fir, sec = 0, length-1

while fir < sec:
    if nums[fir] + nums[sec] < GOAL:
        fir += 1
        
    elif nums[fir] + nums[sec] > GOAL:
        sec -= 1
        
    else:
        count += 1
        fir += 1; sec -= 1

print(count)
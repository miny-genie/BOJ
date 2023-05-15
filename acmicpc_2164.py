# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Main ----------
queue = deque()
N = int(input())

for index in range(1, N + 1):
    queue.append(index)

while len(queue) != 1:
    queue.popleft()
    queue.rotate(-1)
    
print(queue[0])
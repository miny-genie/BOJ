# ---------- Import ----------
from collections import deque
queue = deque()
import sys
input = sys.stdin.readline

# ---------- Main ----------
T = int(input())

for _ in range(T):
    cmd = list(map(str, input().split()))

    if cmd[0] == "push":   # push X
        queue.append(cmd[1])

    if cmd[0] == "pop":
        print(queue.popleft()) if queue else print(-1)

    if cmd[0] == "size":
        print(len(queue))

    if cmd[0] == "empty":
        print(0) if len(queue) else print(1)

    if cmd[0] == "front":
        print(queue[0]) if queue else print(-1)

    if cmd[0] == "back":
        print(queue[-1]) if queue else print(-1)
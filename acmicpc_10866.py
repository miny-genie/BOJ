# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
queue = deque()

for _ in range(N):
    cmd = input().split()

    if cmd[0] == "push_front":
        queue.appendleft(cmd[1])

    if cmd[0] == "push_back":
        queue.append(cmd[1])

    if cmd[0] == "pop_front":
        print(queue.popleft()) if queue else print(-1)

    if cmd[0] == "pop_back":
        print(queue.pop()) if queue else print(-1)

    if cmd[0] == "size":
        print(len(queue))

    if cmd[0] == "empty":
        print(0) if queue else print(1)

    if cmd[0] == "front":
        print(queue[0]) if queue else print(-1)

    if cmd[0] == "back":
        print(queue[-1]) if queue else print(-1)
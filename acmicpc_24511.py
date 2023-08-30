# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Main ----------
N = int(input())
is_queue_or_stack = list(map(int, input().split()))
init_num = list(map(int, input().split()))

length = int(input())
append_num = list(map(int, input().split()))

# Stack can be ignore
queue = deque()
for i in range(N):
    if is_queue_or_stack[i] == 0:
        queue.append(init_num[i])
       
# Each queue can deal with ont big queue
for v in append_num:
    queue.appendleft(v)
    print(queue.pop(), end=" ")
# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Main ----------
length, cnt = map(int, input().split())
number = list(map(int, input().split()))
queue = deque(i for i in range(1, length+1))

cnt = 0
for i in number:
    length = len(queue)
    index = queue.index(i)
    left_side = index - 0
    right_side = length - index

    if left_side <= right_side:
        queue.rotate(-left_side)
        cnt += left_side
        queue.popleft()

    else:
        queue.rotate(right_side)
        cnt += right_side
        queue.popleft()
        
print(cnt)
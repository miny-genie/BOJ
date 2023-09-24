# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Main ----------
length = int(input())
queue = deque(list(map(int, input().split())))
index = deque([i for i in range(1, length+1)])

while index:
    move = queue.popleft()
    print(index.popleft(), end=" ")
    
    if move > 0: move -= 1
    
    queue.rotate(-move)
    index.rotate(-move)
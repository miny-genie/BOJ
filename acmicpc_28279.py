# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Main ----------
dequeue = deque()

for _ in range(int(input())):
    cmd = list(map(str, input().split()))
    
    if cmd[0] == "1":
        dequeue.appendleft(int(cmd[1]))
        
    elif cmd[0] == "2":
        dequeue.append(int(cmd[1]))
        
    elif cmd[0] == "3":
        print(dequeue.popleft()) if dequeue else print(-1)
        
    elif cmd[0] == "4":
        print(dequeue.pop()) if dequeue else print(-1)
        
    elif cmd[0] == "5":
        print(len(dequeue))
        
    elif cmd[0] == "6":
        print(1) if not len(dequeue) else print(0)
        
    elif cmd[0] == "7":
        print(dequeue[0]) if dequeue else print(-1)
        
    else:
        print(dequeue[-1]) if dequeue else print(-1)
from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
cmds = list(map(int, input().split()))

origin = deque()
for card, cmd in enumerate(cmds[::-1], 1):    
    if cmd == 1:
        origin.appendleft(card)
            
    elif cmd == 2:
        tmp = origin.popleft()
        origin.appendleft(card)
        origin.appendleft(tmp)
        
    else:
        origin.append(card)
        
print(*origin)
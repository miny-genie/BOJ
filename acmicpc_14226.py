from collections import deque
from sys import stdin
input = stdin.readline


def get_min_time(goal: int) -> int:
    visited = {(1, 0): True}
    queue = deque([(1, 0, 0)])
    
    while queue:
        cur_emoticone, clipboard, time = queue.popleft()
        if cur_emoticone == goal:
            return time
        
        # cmd 1
        queue.append((cur_emoticone, cur_emoticone, time + 1))
        
        # cmd 2
        if (pair := (cur_emoticone + clipboard, clipboard)) not in visited:
            queue.append((cur_emoticone + clipboard, clipboard, time + 1))
            visited[pair] = True
        
        # cmd 3
        if (pair := (cur_emoticone - 1, clipboard)) not in visited:
            queue.append((cur_emoticone - 1, clipboard, time + 1))
            visited[pair] = True


n = int(input())
min_time = get_min_time(n)
print(min_time)

# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(old, young):
    queue = deque([(old, young, 1)])
    visited = [[0] * 500_001 for _ in range(3)]
    
    while queue:
        o, y, dist = queue.popleft()

        if y > 500_000:
            return -1

        if o == y:
            return dist - 1

        for i, next_old in enumerate([o*2, o+1, o-1]):
            if 0 <= next_old <= 500_000 and visited[i][next_old] == 0:
                queue.append((next_old, y+dist, dist+1))
                visited[i][next_old] = 1

    return -1

# ---------- Main ----------
old, young = map(int, input().split())
answer = BFS(old, young)
print(answer)
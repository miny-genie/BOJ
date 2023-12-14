# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(graph):
    max_friends = 0
    
    # Brute force: checking all person
    for person in range(length):
        visited = [0] * length
        visited[person] = 1
        
        # do BFS
        Q = deque([(person, 0)])
        while Q:
            cur_person, bridge = Q.popleft()
            
            # End condition
            if bridge == 2:
                continue
            
            for friend in graph[cur_person]:
                if not visited[friend]:
                    visited[friend] = 1
                    Q.append((friend, bridge+1))
                    
        # max condition
        max_friends = max(max_friends, sum(visited))
    
    # A <-> A is not friend
    return max_friends - 1

# ---------- Main ----------
length = int(input())

# Init
graph = [[] for _ in range(length)]
for x in range(length):
    for y, char in enumerate(input().rstrip()):
        if char == "Y":
            graph[x].append(y)
            
# Do bfs
answer = BFS(graph)
print(answer)
# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def BFS(start: int, minimum: int) -> int:
    Q = deque([(start, float('inf'))])
    
    count = 0
    while Q:
        node, check = Q.popleft()
        
        for next_node, next_weight in graph[node]:
            if next_weight < minimum:
                continue
            
            if minimum <= next_weight and not visited[next_node]:
                count += 1
                Q.append((next_node, min(check, next_weight)))
                visited[next_node] = 1
                
    return count

# ---------- Import ----------
node, question = map(int, input().split())
graph = [[] for _ in range(node+1)]

for _ in range(node-1):
    a, b, weight = map(int, input().split())
    graph[a].append((b, weight))
    graph[b].append((a, weight))
    
for _ in range(question):
    minimum, start = map(int, input().split())
    
    visited = [0] * (node+1)
    visited[start] = 1
    
    answer = BFS(start, minimum)
    print(answer)
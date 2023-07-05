# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Main ----------
students, compareCounts = map(int, input().split())

graph = [[] for _ in range(students+1)]
inDegree = [0 for _ in range(students+1)]

queue = deque()
result = []

# Topology sort initialization
for _ in range(compareCounts):
    A, B = map(int, input().split())
    graph[A].append(B)
    inDegree[B] += 1
    
# Starting queue initialization
for i in range(1, students+1):
    if inDegree[i] == 0:
        queue.append(i)
        
# Doing topology sort
while queue:
    value = queue.popleft()
    result.append(value)
    
    for i in graph[value]:
        inDegree[i] -= 1
        
        if inDegree[i] == 0:
            queue.append(i)
            
print(*result)
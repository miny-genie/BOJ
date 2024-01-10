from collections import deque
import sys
input = sys.stdin.readline


def BFS(node):
    global depth
    Q = deque([node])
    
    visited[node] = depth
    depth += 1
    
    while Q:
        node = Q.popleft()
        
        for i in graph[node]:
            if not visited[i]:
                Q.append(i)
                visited[i] = depth
                depth += 1
    return


# Declaration
node, edge, start = map(int, input().split())
graph = [[]*(node+1) for _ in range(node+1)]
visited = [0] * (node+1)

# Init
for _ in range(edge):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# DESC
for line in graph:
    line.sort(reverse=True)
    
# DFS
depth = 1
BFS(start)

print(*visited[1:], sep="\n")
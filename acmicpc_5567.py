from collections import deque
from sys import stdin
input = stdin.readline


def bfs(graph: list, node_count: int) -> int:
    visited = [False] * (node_count + 1)
    visited[1] = True
    
    queue = deque([(1, 0)])
    while queue:
        node, bridge = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor] and bridge + 1 <= 2:
                visited[neighbor] = True
                queue.append((neighbor, bridge + 1))
    
    return sum(visited) - 1


node_count = int(input())
edge_count = int(input())
graph = [[] for _ in range(node_count + 1)]

for _ in range(edge_count):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

connect = bfs(graph, node_count)
print(connect)
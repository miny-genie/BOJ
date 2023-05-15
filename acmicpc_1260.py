# ---------- Import ----------
from collections import deque
import sys
input = sys.stdin.readline

# ---------- Function ----------
def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in range(1, node+1):
        if not visited[i] and graph[v][i]:
            DFS(graph, i, visited)


def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in range(1, node+1):
            if not visited[i] and graph[v][i]:
                queue.append(i)
                visited[i] = True

# ---------- Main ----------
node, edge, start = map(int, input().split())

graph =[[False]*(node+1) for _ in range(node+1)]
DFS_visited = [False] * (node+1)
BFS_visited = [False] * (node+1)

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

DFS(graph, start, DFS_visited)
print()
BFS(graph, start, BFS_visited)
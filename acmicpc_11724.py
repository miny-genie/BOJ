# ---------- Import ----------
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# ---------- Function ----------
def DFS(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

# ---------- Main ----------
N, M = map(int, input().split())
graph = [[] for _ in range(N+1) ]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for node in range(1, N+1):
    if not visited[node]:
        DFS(graph, node, visited)
        cnt += 1

print(cnt)
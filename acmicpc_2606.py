# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def DFS(graph, v, visited):
    global dfs

    visited[v] = True
    dfs.append(v)

    for i in range(1, node+1):
        if graph[v][i] and not visited[i]:
            DFS(graph, i, visited)


# ---------- Main ----------
node = int(input())
edge = int(input())

dfs = []
DFS_visited = [False] * (node+1)
graph = [[False] * (node+1) for _ in range(node+1)]

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

DFS(graph, 1, DFS_visited)
print(len(dfs) - 1)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(200_000)


def DFS(node):
    global depth
    visited[node] = depth
    depth += 1
    
    for i in graph[node]:
        if not visited[i]:
            DFS(i)
    
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

# ASC
for line in graph:
    line.sort()
    
# DFS
depth = 1
DFS(start)

print(*visited[1:], sep="\n")
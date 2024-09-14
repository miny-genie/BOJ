from sys import stdin
input = stdin.readline


def edges_to_graph(edges: list, vertex_count: int) -> list:
    graph = [[] for _ in range(vertex_count)]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    return graph


def dfs(node: int, graph: list, visited: list, depth: int) -> None:
    if depth == 5:
        print(1)
        exit()
    
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, graph, visited, depth+1)
            visited[next_node] = False
    return


vertex_count, edge_count = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(edge_count)]
graph = edges_to_graph(edges, vertex_count)
depth_more_than_five = False

for start_node in range(vertex_count):
    visited = [False] * vertex_count
    visited[start_node] = True
    dfs(start_node, graph, visited, 1)
print(0)
from collections import deque
from sys import stdin
input = stdin.readline


def graphify(node_count: int, edges: list) -> list:
    graph = [[] for _ in  range(node_count)]
    for u, v, cost in edges:
        graph[u].append((v, cost))
    return graph


def get_max_profit(node_count, start_city, end_city, edges, profits) -> str|int:
    dist = [-float('inf')] * node_count
    dist[start_city] = profits[start_city]
    
    # Bellman-Ford Algorithm
    for _ in range(node_count - 1):
        for u, v, cost in edges:
            if dist[v] < dist[u] - cost + profits[v]:
                dist[v] = dist[u] - cost + profits[v]
    
    # Detect Positive Cycle
    pos_cycle = [False] * node_count
    for u, v, cost in edges:
        if dist[v] < dist[u] - cost + profits[v]:
            pos_cycle[u] = True
            pos_cycle[v] = True
    
    # Check node that connect positive cycle
    queue = deque()
    connect = [False] * node_count
    
    for idx, isin in enumerate(pos_cycle):
        if isin:
            queue.append(idx)
            connect[idx] = True
    
    graph = graphify(node_count, edges)
    while queue:
        cur = queue.popleft()
        for neighbor, _ in graph[cur]:
            if not connect[neighbor]:
                connect[neighbor] = True
                queue.append(neighbor)
    
    # Positive cycle affects the end node
    if connect[end_city]:
        return "Gee"
    
    # End node is unreachable
    elif isinstance(dist[end_city], float):
        return "gg"
    
    return dist[end_city]


node_count, start_city, end_city, edge_count = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(edge_count)]
profits = list(map(int, input().split()))

max_profit = get_max_profit(node_count, start_city, end_city, edges, profits)
print(max_profit)

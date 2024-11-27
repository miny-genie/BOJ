from heapq import heappop, heappush
from sys import stdin
input = stdin.readline


def djikstra(graph: list, start: int):
    distances = [float('inf')] * (node_count + 1)
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        cur_dist, cur_node = heappop(queue)
        
        if cur_dist > distances[cur_node]:
            continue
        
        for neighbor, weight in graph[cur_node]:
            new_dist = cur_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heappush(queue, (new_dist, neighbor))
        
    return distances[1:]


# Base Info Input
node_count, limit, edge_count = map(int, input().split())
items = list(map(int, input().split()))

# Graph Init
graph = [[] for _ in range(node_count + 1)]
for _ in range(edge_count):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))

# Compute max items by djikstra algorithm
max_items = 0
for start in range(1, node_count + 1):
    distances = djikstra(graph, start)
    
    total_items = sum(
        item
        for item, dist in zip(items, distances)
        if dist <= limit
    )    
    max_items = max(max_items, total_items)

print(max_items)
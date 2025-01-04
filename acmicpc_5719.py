from collections import deque
from heapq import heappop, heappush
from sys import stdin
input = stdin.readline


def dijkstra(graph: list, visited: list, start: int):
    distances = [float('inf')] * (node_count)
    distances[start] = 0
    heap = [(0, start)]
    
    while heap:
        cur_dist, cur_node = heappop(heap)
        if cur_dist > distances[cur_node]:
            continue
        
        for neighbor, cost in graph[cur_node]:
            new_dist = cur_dist + cost
            if distances[neighbor] > new_dist and not visited[cur_node][neighbor]:
                distances[neighbor] = new_dist
                heappush(heap, (new_dist, neighbor))
                
    return distances


def bfs(end: int, dist: list, visited: list):
    queue = deque([end])
    while queue:
        node = queue.popleft()
        for prev, cost in reverse_graph[node]:
            if dist[prev] + cost == dist[node] and not visited[prev][node]:
                queue.append(prev)
                visited[prev][node] = True


while True:
    # info input
    node_count, edge_count = map(int, input().split())
    if node_count + edge_count == 0:
        break
    start, end = map(int, input().split())
    visited = [[False] * node_count for _ in range(node_count)]
    
    # graph init
    graph = [[] for _ in range(node_count)]
    reverse_graph = [[] for _ in range(node_count)]
    for _ in range(edge_count):
        u, v, cost = map(int, input().split())
        graph[u].append((v, cost))
        reverse_graph[v].append((u, cost))
    
    # find shortest path
    distances = dijkstra(graph, visited, start)
    
    # remove shortest path
    bfs(end, distances, visited)
    
    # find almost-shortest path
    distances = dijkstra(graph, visited, start)
    almost = distances[end]
    print(almost if isinstance(almost, int) else -1)

# 25.01.04
# Platinum 1: 2166 > 2167 (+1pts)
# 승급까지 -34 > -33
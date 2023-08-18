# ---------- Import  ----------
import heapq
import sys
input = sys.stdin.readline

INF = 1e9

# ---------- Function ----------
def Dijkstra(sNode):
    # Start node init
    distance[sNode] = 0
    
    # Heap init
    heap = []
    heapq.heappush(heap, (0, sNode))
    
    # Do dijkstra
    while heap:
        dist, current_node = heapq.heappop(heap)
        
        if distance[current_node] < dist:
            continue
        
        # Check nodes connected with current node
        for i in graph[current_node]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

# ---------- Main ----------
Vertex, Edge = map(int, input().split())
start = int(input())

# Init list
distance = [INF] * (Vertex+1)
graph = [[] for _ in range(Vertex+1)]

# Input weight in Edge times
for _ in range(Edge):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# Doing dijkstra
Dijkstra(start)

# Print
for i in range(1, Vertex+1):
    print("INF") if distance[i] == INF else print(distance[i])
# ---------- Import ----------
import heapq
import sys
input = sys.stdin.readline

INF = float('inf')


# ---------- Function ----------
def Dijkstra(sNode: int, eNode: int) -> int:
    Q = []
    distance[sNode] = 0
    heapq.heappush(Q, (0, sNode))
    
    while Q:
        cost, current_node = heapq.heappop(Q)
        
        if current_node == eNode:
            return distance[eNode]
        
        for next_node, weight in graph[current_node]:
            new_cost = cost + weight
            
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(Q, (new_cost, next_node))


# ---------- Main ----------
Node = int(input())
Edge = int(input())

graph = [[] for _ in range(Node+1)]
distance = [INF] * (Node+1)

for _ in range(Edge):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

START, END = map(int, input().split())
    
print(Dijkstra(START, END))
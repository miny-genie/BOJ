# ---------- Import ----------
from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

# ---------- Function ----------
def dijkstra(sNode: int, eNode: int):
    distance = [float('inf')] * (vertex+1)
    distance[sNode] = 0
    
    Q = [(0, sNode, [sNode])]
    while Q:
        cost, cur_node, path = heappop(Q)
        
        if cur_node == eNode:
            return cost, path
        
        for next_node, weight in graph[cur_node]:
            new_cost = cost + weight
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                new_path = path + [next_node]
                heappush(Q, (new_cost, next_node, new_path))
    
    return None

# ---------- Main ----------
vertex = int(input())
edge = int(input())

graph = [[] for _ in range(vertex+1)]
for _ in range(edge):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    
sNode, eNode = map(int, input().split())
answer = dijkstra(sNode, eNode)

print(answer[0], len(answer[1]), sep="\n")
print(*answer[1])
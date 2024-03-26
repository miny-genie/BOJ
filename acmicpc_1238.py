# ---------- Import ----------
from heapq import heappop, heappush
from sys import stdin
input = stdin.readline

# ---------- Function ----------
def djikstra(sNode: int, eNode: int) -> int:
    distance = [float('inf')] * (city_count+1)
    distance[sNode] = 0
    
    Q = []
    heappush(Q, (0, sNode))    # cost, node
    
    while Q:
        cost, cur_node = heappop(Q)
        
        if cur_node == eNode:
            return distance[eNode]
        
        for next_node, weight in roads[cur_node]:
            new_cost = cost + weight
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heappush(Q, (new_cost, next_node))
    
    return None

# ---------- Main ----------
city_count, road_count, cur_city = map(int, input().split())
roads = [[] for _ in range(city_count+1)]

for _ in range(road_count):
    s, e, w = map(int, input().split())
    roads[s].append((e, w))
    
answer = max(
    djikstra(i, cur_city) + djikstra(cur_city, i)
    for i in range(1, city_count+1)
)
print(answer)
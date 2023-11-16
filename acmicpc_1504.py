# -------------------- Case 1: AC(64436KB, 388ms) --------------------
# ---------- Import ----------
import heapq
import sys
input = sys.stdin.readline

INF = 1e9


# ---------- Function ----------
def Dijkstra(sNode: int, eNode: int):
    # Start node and distance Init
    distance = [INF] * (Node+1)
    distance[sNode] = 0
    
    # Init
    Q = []
    heapq.heappush(Q, (0, sNode))   # cost, node
    
    # Do dijkstra
    while Q:
        cost, current_node = heapq.heappop(Q)
        
        # End condition
        if current_node == eNode:
            return distance[eNode]
        
        # Check nodes connected with current node
        for next_node, weight in graph[current_node]:
            new_cost = cost + weight
            
            # New cost is more smallest
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(Q, (new_cost, next_node))
    
    # No way to go eNode
    return None


# ---------- Main ----------
Node, Edge = map(int, input().split())
graph = [[] for _ in range(Node+1)]

# Input graph information
for _ in range(Edge):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))

# Two node that must pass
fir, sec = map(int, input().split())
way_distance = [0, 0]

way_condition = [
    [(1, fir), (fir, sec), (sec, Node)],
    [(1, sec), (sec, fir), (fir, Node)]
]

# Find shortest way
for idx, condition in enumerate(way_condition):
    way = 0
    
    for s, e in condition:
        try:
            way += Dijkstra(s, e)
        except TypeError:
            way = None
            break
    
    way_distance[idx] = way
        
# Print answer
way1 = way_distance[0]
way2 = way_distance[1]

if (way1 is None) and (way2 is None): print(-1)
elif way1 is None: print(way2)
elif way2 is None: print(way1)
else: print(min(way1, way2))




# # -------------------- Case 2: AC(64284KB, 392ms) --------------------
# # ---------- Import ----------
# import heapq
# import sys
# input = sys.stdin.readline

# INF = 1e9


# # ---------- Function ----------
# def Dijkstra(sNode: int, eNode: int):
#     # Start node and distance Init
#     distance = [INF] * (Node+1)
#     distance[sNode] = 0
    
#     # Init
#     Q = []
#     heapq.heappush(Q, (0, sNode))   # cost, node
    
#     # Do dijkstra
#     while Q:
#         cost, current_node = heapq.heappop(Q)
        
#         # End condition
#         if current_node == eNode:
#             return distance[eNode]
        
#         # Check nodes connected with current node
#         for next_node, weight in graph[current_node]:
#             new_cost = cost + weight
            
#             # New cost is more smallest
#             if new_cost < distance[next_node]:
#                 distance[next_node] = new_cost
#                 heapq.heappush(Q, (new_cost, next_node))
    
#     # No way to go eNode
#     return INF


# # ---------- Main ----------
# Node, Edge = map(int, input().split())
# graph = [[] for _ in range(Node+1)]

# # Input graph information
# for _ in range(Edge):
#     start, end, weight = map(int, input().split())
#     graph[start].append((end, weight))
#     graph[end].append((start, weight))

# # Two node that must pass
# fir, sec = map(int, input().split())

# must_way = Dijkstra(fir, sec)
# way1 = sum([Dijkstra(1, fir), must_way, Dijkstra(sec, Node)])
# way2 = sum([Dijkstra(1, sec), must_way, Dijkstra(fir, Node)])
        
# # Print answer
# answer = min(way1, way2)
# print(answer) if answer < INF else print(-1)
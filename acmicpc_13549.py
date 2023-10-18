# ---------- Import ----------
import heapq
import sys
input = sys.stdin.readline

INF = float('inf')
MAX = 100_000 + 1

# ---------- Function ----------
def Dijkstra():
    Q = [(0, old)]   # cost, current_index
    distance[old] = 0
    
    while Q:
        cost, x = heapq.heappop(Q)
        
        # End condition
        if x == goal:
            return cost
        
        # Case of move: twice, backward, forward
        for move_check, dx in enumerate([x, -1, 1]):
            nx = x + dx
            
            # Check: out of bound
            if nx < 0 or nx >= MAX:
                continue
            
            # Teleportation no waste time
            if move_check == 0:
                new_cost = cost
            
                # Check: is shortest
                if new_cost < distance[nx]:
                    distance[nx] = new_cost
                    heapq.heappush(Q, (new_cost, nx))
                    
            # Just move waste time
            else:
                new_cost = cost + 1
                
                # Check: is shortest
                if new_cost < distance[nx]:
                    distance[nx] = new_cost
                    heapq.heappush(Q, (new_cost, nx))


# ---------- Main ----------
old, goal = map(int, input().split())

graph = [1] * MAX
graph[old] = 0
distance = [INF] * MAX

answer = Dijkstra()
print(answer)
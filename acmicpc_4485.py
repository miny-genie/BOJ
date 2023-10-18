# ---------- Import ----------
import heapq
import sys
input = sys.stdin.readline

INF = 1e9

# ---------- Function ----------
def Dijkstra(length: int, graph: list, distance: list) -> int:
    GOAL = length - 1
    Q = []
    heapq.heappush(Q, (graph[0][0], 0, 0))  # cost, x_coord, y_coord
    distance[0][0] = 0
    
    while Q:
        cost, x, y = heapq.heappop(Q)
        
        if x == GOAL and y == GOAL:
            return distance[x][y]
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < length and 0 <= ny < length:
                new_cost = cost + graph[nx][ny]
                
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(Q, (new_cost, nx, ny))
    
    return

# ---------- Main ----------
case = 0
while True:
    length = int(input())
    if length == 0: break
    
    graph = [list(map(int, input().split())) for _ in range(length)]
    distance = [[INF] * length for _ in range(length)]
    
    answer = Dijkstra(length, graph, distance)
    case += 1
    print(f'Problem {case}: {answer}')
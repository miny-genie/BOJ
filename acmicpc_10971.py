# # -------------------- Case 1: TLE --------------------
# # ---------- Import ----------
# import sys
# input = sys.stdin.readline

# # ---------- Function ----------
# def TSP(current, total):
#     global min_cost
    
#     if all(visited):
#         min_cost = min(min_cost, total)
#         return
    
#     for idx, next in enumerate(graph[current]):
#         if idx == start and sum(visited) != cities-1:
#             continue
        
#         if not visited[idx] and next:
#             visited[idx] = True
#             TSP(idx, total + next)
#             visited[idx] = False

# # ---------- Main ----------
# cities = int(input())
# graph = [list(map(int, input().split())) for _ in range(cities)]

# min_cost = 1e9
# visited = [False] * cities

# for start in range(cities):
#     TSP(start, 0)
    
# print(min_cost)

# # ---------- Comment ----------
# # https://shoark7.github.io/programming/algorithm/introduction-to-tsp-and-solve-with-exhasutive-search


# -------------------- Case 2 --------------------
# ---------- Import ----------
import sys
input = sys.stdin.readline

# ---------- Function ----------
def TSP(cost: list, length: int) -> int:
    INF = float('inf')
    VISITED_ALL = (1 << length) - 1
    answer = 1e9
    
    def find_path(start, last, visited, distance):
        nonlocal answer
        
        if visited == VISITED_ALL:
            return_to_start = cost[last][start] or INF
            answer = min(answer, distance + return_to_start)
            return
        
        for city in range(length):
            if visited & (1 << city) == 0 and cost[last][city]:
                find_path(start, city, visited | (1 << city), distance + cost[last][city])
        
    for start in range(length):
        find_path(start, start, 1 << start, 0)
        
    return answer

# ---------- Main ----------
length = int(input())
list_ = [list(map(int, input().split())) for _ in range(length)]

result = TSP(list_, length)
print(result)
from math import ceil, log2
from sys import stdin, setrecursionlimit
setrecursionlimit(100_000 + 5)
input = stdin.readline


def find_parents(node_count: int, edges: list) -> list:
    def dfs(cur: int, par: int, cost: int):
        parents[cur] = par
        costs[cur] = cost
        for neighbor, cost in graph[cur]:
            if not (neighbor == par):
                dfs(neighbor, cur, cost)
    
    graph = [[] for _ in range(node_count + 1)]
    for u, v, cost in edges:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    
    parents = [-1] * (node_count + 1)
    costs = [-1] * (node_count + 1)
    dfs(cur=1, par=1, cost=0)   # 1-based index
    
    return parents, costs


def simulation() -> list:
    max_pow = ceil(log2(room_count)) + 1
    sparse = [[(0, 0) for _ in range(max_pow)] for _ in range(room_count + 1)]
    
    for room in range(1, room_count + 1):
        sparse[room][0] = (parents[room], costs[room])
    
    for pow2 in range(1, max_pow):
        for room in range(1, room_count + 1):
            half_room, half_cost = sparse[room][pow2 - 1]
            next_room, next_cost = sparse[half_room][pow2 - 1]
            sparse[room][pow2] = (next_room, half_cost + next_cost)
    
    result = []
    for room in range(1, room_count + 1):
        current_room = room
        remain_energy = energies[room - 1]
        bit = max_pow - 1   # match index
        
        while bit >= 0:
            next_state, total_cost = sparse[current_room][bit]
            if total_cost <= remain_energy:
                current_room = next_state
                remain_energy -= total_cost
                
                # early stopping
                if next_state == 1:
                    result.append(1)
                    break
            
            bit -= 1
        
        else:
            result.append(current_room)
    
    return result


room_count = int(input())
energies = [int(input()) for _ in range(room_count)]
edges = [list(map(int, input().split())) for _ in range(room_count - 1)]

parents, costs = find_parents(room_count, edges)
result = simulation()
print(*result, sep='\n')

# 25.01.07
# Platinum 1: 2169 > 2170 (+1pts)
# 승급까지 -31 > -30
from collections import deque
from itertools import combinations
from sys import stdin
input = stdin.readline


def solve_gerrymandering(N: int, population: list, graph: dict) -> int:
    def is_connected(group: set, graph: dict) -> bool:
        start = next(iter(group))    # Random Start Point
        visited = set([start])
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor in group:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited == group
    
    def calculate_difference(group1: set, group2: set, population: list) -> int:
        pop1 = sum(population[i - 1] for i in group1)
        pop2 = sum(population[i - 1] for i in group2)
        return abs(pop1 - pop2)
    
    nodes = list(range(1, N+1))
    min_difference = float('inf')
    
    for i in range(1, N // 2 + 1):
        for group1 in combinations(nodes, i):
            group1 = set(group1)
            group2 = set(nodes) - group1
            
            if is_connected(group1, graph) and is_connected(group2, graph):
                difference = calculate_difference(group1, group2, population)
                min_difference = min(min_difference, difference)
    
    return min_difference if min_difference != float('inf') else -1


N = int(input())
population = list(map(int, input().split()))
graph = {i+1 : list(map(int, input().split()))[1:] for i in range(N)}
min_difference = solve_gerrymandering(N, population, graph)
print(min_difference)

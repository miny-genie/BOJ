from heapq import heappop, heappush
from sys import stdin
input = stdin.readline


def topology_sorting(problem_count: int, querys: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(problem_count + 1)]
    in_degree = [0 for _ in range(problem_count + 1)]
    
    # 초기화
    for start, end in querys:
        graph[start].append(end)
        in_degree[end] += 1
    
    heap = []
    for idx, degree in enumerate(in_degree):
        if not degree:
            heappush(heap, idx)
    
    result = []
    while heap:
        current = heappop(heap)
        result.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heappush(heap, neighbor)
    
    return result[1:]


problem_count, query_count = map(int, input().split())
querys = [list(map(int, input().split())) for _ in range(query_count)]

result = topology_sorting(problem_count, querys)
print(*result)
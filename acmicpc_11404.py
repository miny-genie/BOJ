from sys import stdin
input = stdin.readline

INF = float('inf')


def floyd_warshall(n: int, graph: list) -> list:
    dist = [[graph[row][col] for col in range(n)] for row in range(n)]
    
    for mid in range(n):
        for row in range(n):
            for col in range(n):
                if row == col:
                    dist[row][col] = 0
                    continue
                
                if dist[row][mid] != INF and dist[mid][col] != INF:
                    dist[row][col] = min(
                        dist[row][col],
                        dist[row][mid] + dist[mid][col]
                    )
    
    return dist


def print_list(list2d: list) -> None:
    for line in list2d:
        print(*[0 if element == INF else element for element in line])


n = int(input())
query_count = int(input())

graph = [[INF] * n for _ in range(n)]
for _ in range(query_count):
    u, v, w = map(int, input().split())
    graph[u-1][v-1] = min(graph[u-1][v-1], w)

answer = floyd_warshall(n, graph)
print_list(answer)
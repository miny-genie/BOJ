from sys import stdin
input = stdin.readline


def floyd_warshall(n: int, graph: list) -> list:
    dist = [[graph[row][col] for col in range(n)] for row in range(n)]
    
    for mid in range(n):
        for row in range(n):
            for col in range(n):
                if dist[row][mid] and dist[mid][col]:
                    dist[row][col] = 1
    
    return dist


def print_list(list2d: list) -> None:
    for line in list2d:
        print(*line)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = floyd_warshall(n, graph)
print_list(answer)
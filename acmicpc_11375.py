from sys import stdin, setrecursionlimit
setrecursionlimit(2000)
input = stdin.readline


# Bipartite Matching
def dfs(worker: int) -> bool:
    for task in graph[worker]:
        if not visited[task]:
            visited[task] = True
            if matching[task] == -1 or dfs(matching[task]):
                matching[task] = worker
                return True
    return False


# First line input
worker_count, task_count = map(int, input().split())

# Graph init
graph = [[] for _ in range(worker_count)]
for idx in range(worker_count):
    _, *works = map(lambda x: int(x) - 1, input().split())
    graph[idx] = works

# Variable declare for bipartite matching
matching = [-1] * task_count
max_match = 0

# Do bipartite matching
for worker in range(worker_count):
    visited = [False] * task_count
    if dfs(worker):
        max_match += 1

print(max_match)


# 25.01.21
# Platinum 1: 2183 > 2184 (+1pts)
# 승급까지 -17 > -16
from collections import deque
from sys import stdin
input = stdin.readline

# Input and declaration
n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
costs = [0 for _ in range(n + 1)]

# Basic info init
for cur in range(1, n + 1):
    cost, _, *befs = map(int, input().split())
    costs[cur] = cost
    
    for bef in befs:
        graph[bef].append(cur)
        indegree[cur] += 1

# Queue init
queue = deque([
    i
    for i in range(1, n + 1)
    if not indegree[i]
])

# Min time at the start
start_dp = [0 for _ in range(n + 1)]
start_dp[1] = 0

# Do dynamic programming with topology sort
while queue:
    cur = queue.popleft()
    
    for neighbor in graph[cur]:
        start_dp[neighbor] = max(start_dp[neighbor], start_dp[cur] + costs[cur])
        indegree[neighbor] -= 1
        if not indegree[neighbor]:
            queue.append(neighbor)

print(max(s + cost for s, cost in zip(start_dp, costs)))

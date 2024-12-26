from collections import defaultdict
from sys import stdin, setrecursionlimit
setrecursionlimit(1_000_000)
input = stdin.readline


def dfs(node: int):
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = 1
    
    for child in tree[node]:
        if not visited[child]:
            dfs(child)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])


node_count = int(input())
tree = defaultdict(list)
for _ in range(node_count - 1):
    u, v = list(map(int, input().split()))
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(node_count + 1)]
visited = [False] * (node_count + 1)

root = 1
dfs(root)
print(min(dp[root]))

# 24.12.26
# Platinum 1: 2151 > 2151 (+0pts)
# 승급까지 -49 > -49
# ---------- Import ----------
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100002)

# ---------- Function ----------
def DFS(adj_list, start):
    global who_is_parent
    
    for n in adj_list[start]:
        if not who_is_parent[n]:
            who_is_parent[n] = start
            DFS(adj_list, n)
    
    return

# ---------- Main ----------
node = int(input())
edge = [list(map(int, input().split())) for _ in range(node-1)]

adj_list = [[] for _ in range(node+1)]
who_is_parent = [0] * (node+1)

# Make adjacency list
for a, b in edge:
    adj_list[a].append(b)
    adj_list[b].append(a)

# Each node sort
for line in adj_list:
    line.sort()
    
# Do dfs
DFS(adj_list, 1)

# Print each node's parent
print(*who_is_parent[2:], sep='\n')
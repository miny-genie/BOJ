from collections import defaultdict
from math import ceil, log2
from sys import stdin, setrecursionlimit
setrecursionlimit(100_002)
input = stdin.readline

INIT = -1


class Tree:
    def __init__(self, node_count: int) -> None:
        self.n = node_count
        self.tree = defaultdict(list)
        self.LOG = ceil(log2(node_count))
        self.parents = [[INIT] * self.LOG for _ in range(node_count + 1)]
        self.depths = [INIT] * (node_count + 1)    # from the root
        self.distances = [INIT] * (node_count + 1)    # from the root
        self.min_edge = [[float('inf')] * self.LOG for _ in range(node_count + 1)]
        self.max_edge = [[-float('inf')] * self.LOG for _ in range(node_count + 1)]
    
    def add_edge(self, u: int, v: int, w: int) -> None:
        self.tree[u].append((v, w))
        self.tree[v].append((u, w))
    
    def dfs(self, node: int, parent: int, depth: int, dist: int) -> None:
        self.parents[node][0] = parent
        self.depths[node] = depth
        self.distances[node] = dist
        
        for next_node, next_dist in self.tree[node]:
            if next_node != parent:
                self.min_edge[next_node][0] = next_dist
                self.max_edge[next_node][0] = next_dist
                self.dfs(next_node, node, depth+1, dist+next_dist)
    
    def prepare_lca(self) -> None:
        self.dfs(node=1, parent=INIT, depth=0, dist=0)
        
        for i in range(1, self.LOG):    # 0 is direct parent node, init in dfs
            for node in range(1, self.n+1):    # 1-based index
                half_parent = self.parents[node][i-1]
                if half_parent != INIT:    # not root
                    self.parents[node][i] = self.parents[half_parent][i-1]
                    self.min_edge[node][i] = min(self.min_edge[node][i-1], self.min_edge[half_parent][i-1])
                    self.max_edge[node][i] = max(self.max_edge[node][i-1], self.max_edge[half_parent][i-1])
    
    def _lca(self, u: int, v: int) -> int:
        # Ensure 'u' is the deeper node
        if self.depths[u] < self.depths[v]:
            u, v = v, u
        
        # Calculate the depth difference
        min_length = float('inf')
        max_length = -float('inf')
        diff = self.depths[u] - self.depths[v]

        # Bring 'u' and 'v' to the same depth
        for i in range(self.LOG):
            if diff & (1 << i):
                min_length = min(min_length, self.min_edge[u][i])
                max_length = max(max_length, self.max_edge[u][i])
                u = self.parents[u][i]
        
        # Check 'u' and 'v' are now the same
        if u == v:
            return u, min_length, max_length
        
        # Find the LCA
        for i in range(self.LOG-1, -1, -1):
            if self.parents[u][i] != self.parents[v][i]:
                min_length = min(min_length, self.min_edge[u][i], self.min_edge[v][i])
                max_length = max(max_length, self.max_edge[u][i], self.max_edge[v][i])
                u = self.parents[u][i]
                v = self.parents[v][i]
        
        min_length = min(min_length, self.min_edge[u][0], self.min_edge[v][0])
        max_length = max(max_length, self.max_edge[u][0], self.max_edge[v][0])
        return self.parents[u][0], min_length, max_length
    
    def query(self, u: int, v: int) -> int:
        ancestor, min_length, max_length = self._lca(u, v)
        return min_length, max_length


node_count = int(input())
tree = Tree(node_count)

for _ in range(node_count-1):
    u, v, w = map(int, input().split())
    tree.add_edge(u, v, w)

tree.prepare_lca()

query_count = int(input())
for _ in range(query_count):
    u, v = map(int, input().split())
    lengths = tree.query(u, v)
    print(*lengths)
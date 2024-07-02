from collections import defaultdict
from math import ceil, log2
from sys import stdin, setrecursionlimit
setrecursionlimit(50_002)
input = stdin.readline


class Tree:
    def __init__(self, node_count: int) -> None:
        self.n = node_count
        self.tree = defaultdict(list)
        self.LOG = ceil(log2(node_count))
        self.parents = [[-1] * self.LOG for _ in range(node_count + 1)]
        self.depths = [-1] * (node_count + 1)
    
    def add_edge(self, u: int, v: int) -> None:
        self.tree[u].append(v)
        self.tree[v].append(u)
    
    def dfs(self, node: int, parent: int, depth: int) -> None:
        self.depths[node] = depth
        self.parents[node][0] = parent
        
        for next_node in self.tree[node]:
            if next_node != parent:
                self.dfs(next_node, node, depth+1)
    
    def prepare_lca(self) -> None:
        self.dfs(node=1, parent=-1, depth=0)
        
        for i in range(1, self.LOG):    # 0 is direct parent node, init in dfs
            for node in range(1, self.n+1):    # 1 based index
                if self.parents[node][i-1] != -1:    # not root
                    self.parents[node][i] = self.parents[self.parents[node][i-1]][i-1]
    
    def lca(self, u: int, v: int) -> int:
        # Ensure 'u' is the deeper node
        if self.depths[u] < self.depths[v]:
            u, v = v, u
        
        # Calculate the depth difference
        diff = self.depths[u] - self.depths[v]
        
        # Bring 'u' and 'v' to the same depth
        for i in range(self.LOG):
            if diff & (1 << i):
                u = self.parents[u][i]
        
        # Check 'u' and 'v' are now the same
        if u == v:
            return u
        
        # Find the LCA
        for i in range(self.LOG-1, -1, -1):
            if self.parents[u][i] != self.parents[v][i]:
                u = self.parents[u][i]
                v = self.parents[v][i]
        
        return self.parents[u][0]

# init
node_count = int(input())
tree = Tree(node_count)

# edges
for _ in range(node_count-1):
    u, v = map(int, input().split())
    tree.add_edge(u, v)

tree.prepare_lca()

# query
for _ in range(query_count := int(input())):
    u, v = map(int, input().split())
    ancestor = tree.lca(u, v)
    print(ancestor)
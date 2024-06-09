from collections import defaultdict
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

INIT = -1


class TwoSAT:
    def __init__(self, node_count) -> None:
        self.node_count = node_count
        self.graph = defaultdict(list)
        self.stack = []
        self.in_stack = [False] * (2 * node_count)
        self.index = 0
        self.indexes = [INIT] * (2 * node_count)
        self.low_link = [INIT] * (2 * node_count)
        self.scc_label = 0
        self.component = [INIT] * (2 * node_count)
    
    def transform_expression(self, a: int, b: int, c: int, d: int) -> tuple:
        # (A and B) or (C and D) using the distributive law
        # >>> (A or C) and (A or D) and (B or C) and (B or D)
        return (a, c), (a, d), (b, c), (b, d)
        
    def add_clause(self, state: str, x: int, y: int) -> None:
        def T(n): return n << 1
        def F(n): return (n << 1) | 1
        
        if state == "jewel":
            trans_exp = self.transform_expression(T(x), F(y), F(x), T(y))
        elif state == "tracker":
            trans_exp = self.transform_expression(T(x), T(y), F(x), F(y))
        
        for exp in trans_exp:
            v1, v2 = exp    # variable
            self.graph[v1 ^ 1].append(v2)
            self.graph[v2 ^ 1].append(v1)
    
    def tarjan(self) -> None:
        def dfs(v: int) -> None:
            self.indexes[v] = self.index
            self.low_link[v] = self.index
            self.index += 1
            self.stack.append(v)
            self.in_stack[v] = True
            
            for neighbor in self.graph[v]:
                if self.indexes[neighbor] == INIT:
                    dfs(neighbor)
                    self.low_link[v] = min(self.low_link[v], self.low_link[neighbor])
                elif self.in_stack[neighbor]:
                    self.low_link[v] = min(self.low_link[v], self.low_link[neighbor])
                    
            # parent node itself
            if self.low_link[v] == self.indexes[v]:
                while True:
                    pop = self.stack.pop()
                    self.in_stack[pop] = False
                    self.component[pop] = self.scc_label
                    if pop == v:
                        break
                    
                # update scc labeling, after make scc
                self.scc_label += 1
        
        # do dfs one time        
        for node in range(2 * self.node_count):
            if self.indexes[node] == INIT:
                dfs(node)
    
    def solve(self) -> bool:
        self.tarjan()
        for i in range(self.node_count):
            # True and False can not same SCC
            if self.component[2*i] == self.component[2*i+1]:
                return False
        return True


row, col = map(int, input().split())
ts = TwoSAT(row + col)

for r in range(row):
    collecion = input().rstrip()
    for c, piece in enumerate(collecion):
        # 'c + row' ensures that row and columns are distinct range
        new_c = c + row
        
        # {T(x) and F(y)} or {F(x) and T(y)}
        if piece == "*":
            ts.add_clause("jewel", r, new_c)
        
        # {T(x) and T(y)} or {F(x) and F(y)}
        elif piece == "#":
            ts.add_clause("tracker", r, new_c)

print(int(ts.solve()))
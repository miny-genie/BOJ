from collections import defaultdict
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

INIT = -1


class KosarajuTwoSAT:
    def __init__(self, node_count: int) -> None:
        self.node_count = node_count
        self.graph = defaultdict(list)
        self.rev_graph = defaultdict(list)
        self.component = [INIT] * (2 * node_count)
        self.visited = [False] * (2 * node_count)
        self.stack = []
    
    def add_clause(self, i: int, is_true_i: bool, j: int, is_true_j: bool) -> None:
        def var_to_node(var: int, is_true: bool):
            return 2*var + (0 if is_true else 1)
        
        s = var_to_node(i, not is_true_i)
        e = var_to_node(j, is_true_j)
        self.graph[s].append(e)
        self.rev_graph[e].append(s)
        
        s = var_to_node(j, not is_true_j)
        e = var_to_node(i, is_true_i)
        self.graph[s].append(e)
        self.rev_graph[e].append(s)
        
    def kosaraju(self) -> None:
        def forward_dfs(v: int) -> None:
            self.visited[v] = True
            for neighbor in self.graph[v]:
                if not self.visited[neighbor]:
                    forward_dfs(neighbor)
            self.stack.append(v)
            
        def backward_dfs(v: int, scc_label: int) -> None:
            self.component[v] = scc_label
            for neighbor in self.rev_graph[v]:
                if self.component[neighbor] == INIT:
                    backward_dfs(neighbor, scc_label)
                    
        # first dfs, stacking elements
        for node in range(2 * self.node_count):
            if not self.visited[node]:
                forward_dfs(node)
        
        # second dfs, find scc
        scc_label = 0
        while self.stack:
            pop = self.stack.pop()
            if self.component[pop] == INIT:
                backward_dfs(pop, scc_label)
                scc_label += 1
        
    def can_solve(self) -> bool:
        self.kosaraju()
        for node in range(self.node_count):
            # True and False can not same scc
            if self.component[2*node] == self.component[2*node+1]:
                return False
        return True


class TarjanTwoSAT:
    def __init__(self, node_count: int) -> None:
        self.node_count = node_count
        self.graph = defaultdict(list)
        self.scc_label = 0
        self.stack = []
        self.in_stack = [False] * (2 * node_count)
        self.index = 0
        self.indexes = [INIT] * (2 * node_count)
        self.low_link = [INIT] * (2 * node_count)
        self.component = [INIT] * (2 * node_count)
    
    def add_clause(self, i: int, is_true_i: bool, j: int, is_true_j: bool) -> None:
        def var_to_node(var: int, is_true: bool):
            return 2*var + (0 if is_true else 1)
        
        s = var_to_node(i, not is_true_i)
        e = var_to_node(j, is_true_j)
        self.graph[s].append(e)
        
        s = var_to_node(j, not is_true_j)
        e = var_to_node(i, is_true_i)
        self.graph[s].append(e)
    
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
                
                # update scc labeling, after made scc
                self.scc_label += 1
        
        # do dfs one time
        for node in range(2 * self.node_count):
            if self.indexes[node] == INIT:
                dfs(node)
    
    def can_solve(self) -> bool:
        self.tarjan()
        for node in range(self.node_count):
            # True and False can not same scc
            if self.component[2*node] == self.component[2*node+1]:
                return False
        return True


node_count, clause_count = map(int, input().split())

# choose one
ts = KosarajuTwoSAT(node_count)
ts = TarjanTwoSAT(node_count)

for _ in range(clause_count):
    x1, x2 = map(int, input().split())
    ts.add_clause(abs(x1)-1, x1 > 0, abs(x2)-1, x2 > 0)

print(int(ts.can_solve()))
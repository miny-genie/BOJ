from collections import defaultdict
from sys import stdin, setrecursionlimit
setrecursionlimit(10_000)
input = stdin.readline

INIT = -1


class TwoSAT:
    def __init__(self, num_count: int) -> None:
        self.num_vars = num_count
        self.graph = defaultdict(list)
        self.rev_graph = defaultdict(list)
        self.component = [INIT] * (2 * num_count)
        self.visited = [False] * (2 * num_count)
        self.stack = []
    
    def add_clause(self, i: int, is_true_i: bool, j: int, is_true_j: bool) -> None:
        def var_to_node(var: int, is_true: bool) -> int:
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
        for i in range(2 * self.num_vars):
            if not self.visited[i]:
                forward_dfs(i)
                
        # second dfs, find SCC
        scc_label = 0
        while self.stack:
            pop = self.stack.pop()
            if self.component[pop] == INIT:
                backward_dfs(pop, scc_label)
                scc_label += 1
        
    def solve(self) -> None:
        self.kosaraju()
        for i in range(self.num_vars):
            # True and False can not same SCC
            if self.component[2*i] == self.component[2*i+1]:
                return False
        return True


student_count, rsp_count = map(int, input().split())
clauses = [list(map(int, input().split())) for _ in range(student_count)]

ts = TwoSAT(rsp_count)
for clause in clauses:
    # scissor is True, rock is False
    x1, x2 = clause
    ts.add_clause(abs(x1)-1, x1 > 0, abs(x2)-1, x2 > 0)
    
print("^_^" if ts.solve() else "OTL")
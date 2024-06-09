##################################################
#################### Kosaraju ####################
##################################################
def k():
    from collections import defaultdict
    from sys import stdin, setrecursionlimit
    setrecursionlimit(10**6)
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
            self.answer = [False] * num_count
        
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
            def dfs_fir(v: int) -> None:
                self.visited[v] = True
                for neighbor in self.graph[v]:
                    if not self.visited[neighbor]:
                        dfs_fir(neighbor)
                self.stack.append(v)
                
            def dfs_sec(v: int, label: int) -> None:
                self.component[v] = label
                for neighbor in self.rev_graph[v]:
                    if self.component[neighbor] == INIT:
                        dfs_sec(neighbor, label)
                        
            for i in range(2 * self.num_vars):
                if not self.visited[i]:
                    dfs_fir(i)
                        
            label = 0
            while self.stack:
                v = self.stack.pop()
                if self.component[v] == INIT:
                    dfs_sec(v, label)
                    label += 1
        
        def solve(self) -> bool:
            self.kosaraju()
            for i in range(self.num_vars):
                if self.component[2 * i] == self.component[2 * i + 1]:
                    return False
                self.answer[i] = self.component[2 * i] > self.component[2 * i + 1]
            return True
        
        def get_assignment(self) -> list:
            return [int(value) for value in self.answer]


    num_count, clause_count = map(int, input().split())
    clauses = [list(map(int, input().split())) for _ in range(clause_count)]

    ts = TwoSAT(num_count)
    for clause in clauses:
        x1, x2 = clause
        ts.add_clause(abs(x1)-1, x1 > 0, abs(x2)-1, x2 > 0)
        
    if ts.solve():
        print(1)
        print(*ts.get_assignment())
    else:
        print(0)



##################################################
##################### Tarjan #####################
##################################################
from collections import defaultdict
from sys import stdin
input = stdin.readline

INIT = -1


class TwoSAT:
    def __init__(self, num_count: int) -> None:
        self.num_vars = num_count
        self.graph = defaultdict(list)
        self.index = 0
        self.stack = []
        self.in_stack = [False] * (2 * num_count)
        self.indices = [INIT] * (2 * num_count)
        self.low_link = [INIT] * (2 * num_count)
        self.sccs = []
        self.assignment = [False] * num_count
        
    def add_clause(self, i: int, is_true_i:bool, j: int, is_true_j: bool) -> None:
        def var_to_node(var: int, is_true: bool) -> int:
            return 2*var + (0 if is_true else 1)
        
        s = var_to_node(i, not is_true_i)
        e = var_to_node(j, is_true_j)
        self.graph[s].append(e)
        
        s = var_to_node(j, not is_true_j)
        e = var_to_node(i, is_true_i)
        self.graph[s].append(e)
        
    def strong_connect(self, v: int):
        self.indices[v] = self.index
        self.low_link[v] = self.index
        self.index += 1
        self.stack.append(v)
        self.in_stack[v] = True
        
        for neighbor in self.graph[v]:
            if self.indices[neighbor] == INIT:
                self.strong_connect(neighbor)
                self.low_link[v] = min(self.low_link[v], self.low_link[neighbor])
            elif self.in_stack[neighbor]:
                self.low_link[v] = min(self.low_link[v], self.low_link[neighbor])
                
        if self.low_link[v] == self.indices[v]:
            scc = []
            while True:
                pop = self.stack.pop()
                self.in_stack[pop] = False
                scc.append(pop)
                if pop == v:
                    break
            self.sccs.append(scc)
    
    def tarjan(self):
        for v in range(2 * self.num_vars):
            if self.indices[v] == INIT:
                self.strong_connect(v)
                
    def solve(self):
        self.tarjan()
        component = [INIT] * (2 * self.num_vars)
        for idx, scc in enumerate(self.sccs):
            for node in scc:
                component[node] = idx
                
        for i in range(self.num_vars):
            if component[2 * i] == component[2 * i + 1]:
                return False
            
        order = sorted(range(2 * self.num_vars), key=lambda x: -component[x])
        assigned = [False] * (2 * self.num_vars)
        for v in order:
            if not assigned[v]:
                assigned[v] = True
                assigned[v ^ 1] = False
                if v % 2 == 0:
                    self.assignment[v // 2] = True
                    
        return True
    
    def get_assignment(self):
        return [int(value) for value in self.assignment]
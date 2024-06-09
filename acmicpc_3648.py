from collections import defaultdict
from sys import stdin, setrecursionlimit
setrecursionlimit(10_000)
input = stdin.readline

INIT = -1


class TwoSAT:
    def __init__(self, num_count: int) -> None:
        self.num_vars = num_count
        self.graph = defaultdict(list)
        self.index = 0
        self.stack = []
        self.in_stack = [False] * (2 * num_count)
        self.indexes = [INIT] * (2 * num_count)
        self.low_link = [INIT] * (2 * num_count)
        self.component = [INIT] * (2 * num_count)
    
    def add_clause(self, i, is_true_i: bool, j: int, is_true_j: bool) -> None:
        def var_to_node(var: int, is_true: bool) -> int:
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
                    
            if self.low_link[v] == self.indexes[v]:
                while True:
                    pop = self.stack.pop()
                    self.in_stack[pop] = False
                    self.component[pop] = self.low_link[v]
                    if pop == v:
                        break
        
        for var in range(2 * self.num_vars):
            if self.indexes[var] == INIT:
                dfs(var)
    
    def solve(self) -> None:
        self.tarjan()
        for i in range(self.num_vars):
            # True and False can not same SCC
            if self.component[2*i] == self.component[2*i+1]:
                return False
        return True
    

while True:
    try:
        part_count, judge_count = map(int, input().split())
        judges = [list(map(int, input().split())) for _ in range(judge_count)]
        
        ts = TwoSAT(part_count)
        ts.add_clause(0, 1, 0, 1)
        
        for judge in judges:
            v1, v2 = judge  # vote
            ts.add_clause(abs(v1)-1, v1 > 0, abs(v2)-1, v2 > 0)
            
        print("yes" if ts.solve() else "no")
        
    except Exception:
        break
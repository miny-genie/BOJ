from collections import defaultdict
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline


# kosaraju algorithm in scc(strongly connected component) of directed graph
# need two times dfs
# time complexity is O(V+E)
class KosarajuSCC:
    def __init__(self, vertex_count: int, edge_count: int, edges: list) -> None:
        self.v = vertex_count
        self.e = edge_count
        self.edges = edges
        self.graph = {i+1:[] for i in range(vertex_count)}
        self.visited = [False] * (vertex_count + 1)
        self.rev_graph = {i+1:[] for i in range(vertex_count)}
        self.rev_visited = [False] * (vertex_count + 1)
        self.stack = []
        self.scc = []
        self.sccs = []
        self.post_init()
    
    def post_init(self) -> None:
        for sNode, eNode in self.edges:
            self.graph[sNode].append(eNode)
            self.rev_graph[eNode].append(sNode)
    
    def kosaraju(self):
        def dfs(node: int) -> None:
            self.visited[node] = True
            for neighbor in self.graph[node]:
                if not self.visited[neighbor]:
                    dfs(neighbor)
            self.stack.append(node)
        
        def rev_dfs(node: int) -> None:
            self.rev_visited[node] = True
            for neighbor in self.rev_graph[node]:
                if not self.rev_visited[neighbor]:
                    rev_dfs(neighbor)
            self.scc.append(node)
        
        # forward dfs
        for i in range(1, self.v):
            if not self.visited[i]:
                dfs(i)
            
        # backward dfs
        while self.stack:
            pop = self.stack.pop()
            if not self.rev_visited[pop]:
                rev_dfs(pop)
                self.sccs.append(sorted(self.scc) + [-1])
                self.scc = []
    
    def find_sccs(self) -> tuple:
        self.kosaraju()
        return len(self.sccs)


# tarjan algorithm in scc(strongly connected component) of directed graph
# need one time dfs
# time complexity is O(V+E)
class Node:
    def __init__(self):
        self.id = None
        self.low_link = None


class TarjanSCC:
    def __init__(self, vertex_count: int, edge_count: int, edges: list) -> None:
        self.v = vertex_count
        self.e = edge_count
        self.edges = edges
        
        self.graph = {i+1:[] for i in range(vertex_count)}
        self.id = 1  # 1 based index
        self.stack = []
        self.in_stack = defaultdict(bool)
        self.nodes = [None] + [Node() for _ in range(vertex_count)] # 1 based index
        self.sccs = []
        self.post_init()
    
    def post_init(self) -> None:
        for sNode, eNode in self.edges:
            self.graph[sNode].append(eNode)
    
    def tarjan(self):
        def dfs(node: int):
            self.nodes[node].id = self.id
            self.nodes[node].low_link = self.id
            self.id += 1
            self.stack.append(node)
            self.in_stack[node] = True
            
            for neighbor in self.graph[node]:
                # not yet been visited, so recurse on
                if self.nodes[neighbor].id is None:
                    dfs(neighbor)
                    self.nodes[node].low_link = min(
                        self.nodes[node].low_link, self.nodes[neighbor].low_link
                    )
                # is in stack(and already visited), so in the current scc 
                elif self.in_stack[neighbor]:
                    self.nodes[node].low_link = min(
                        self.nodes[node].low_link, self.nodes[neighbor].low_link
                    )
            
            # after visited all neighbor
            # if 'node' is root node, pop the stack and generate SCC
            if self.nodes[node].low_link == self.nodes[node].id:
                scc = []
                while True:
                    pop = self.stack.pop()
                    self.in_stack[pop] = False
                    scc.append(pop)
                    if pop == node:
                        break
                self.sccs.append(sorted(scc))
        
        for i in range(1, self.v):
            if self.nodes[i].id is None:
                dfs(i)
    
    def find_sccs(self) -> tuple:
        self.tarjan()
        return len(self.sccs)


vertex_count, edge_count = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(edge_count)]

if vertex_count == 1:
    print("Yes")
else:
    # choose one
    scc = KosarajuSCC(vertex_count, edge_count, edges)
    scc = TarjanSCC(vertex_count, edge_count, edges)
    count = scc.find_sccs()
    print("Yes" if count == 1 else "No")
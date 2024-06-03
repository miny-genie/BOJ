from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline


class KosarajuSCC:
    def __init__(self, vertex_count: int, edge_count: int, edges: list) -> None:
        self.v = vertex_count
        self.e = edge_count
        self.edges = edges
        self.stack = []
        self.graph = {i+1:[] for i in range(vertex_count)}
        self.visited = [False] * (vertex_count + 1)
        self.rev_graph = {i+1:[] for i in range(vertex_count)}
        self.rev_visited = [False] * (vertex_count + 1)
        self.scc = []
        self.sccs = []
        self.post_init()
    
    def post_init(self) -> None:
        for s, e in self.edges:
            self.graph[s].append(e)
            self.rev_graph[e].append(s)
    
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
    
    def solve(self) -> tuple:
        self.kosaraju()
        return len(self.sccs), sorted(self.sccs)


vertex_count, edge_count = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(edge_count)]

scc = KosarajuSCC(vertex_count, edge_count, edges)
count, answer = scc.solve()

print(count)
for ans in answer:
    print(*ans)
from collections import defaultdict
from sys import stdin, setrecursionlimit
setrecursionlimit(100_002)
input = stdin.readline


class Graph:
    def __init__(self, vertex_count: int, edges: list) -> None:
        self.v = vertex_count
        self.graph = defaultdict(list)
        self.time = 0
        self.visited = [False] * (vertex_count + 1)
        self.parent = [None] * (vertex_count + 1)
        self.disc = [float('inf')] * (vertex_count + 1)    # first discovery time
        self.low = [float('inf')] * (vertex_count + 1)
        self.ap = [False] * (vertex_count + 1)    # Articulation Point
        self.post_init(edges)
    
    def _add_edge(self, u: int, v: int) -> None:
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def post_init(self, edges: list) -> None:
        for edge in edges:
            self._add_edge(*edge)
    
    def _ap_util(self, cur_node: int) -> None:
        children = 0
        self.visited[cur_node] = True
        self.disc[cur_node] = self.time
        self.low[cur_node] = self.time
        self.time += 1
        
        for next_node in self.graph[cur_node]:
            if not self.visited[next_node]:
                self.parent[next_node] = cur_node
                children += 1
                self._ap_util(next_node)
                self.low[cur_node] = min(self.low[cur_node], self.low[next_node])
                
                # ap condition 1, root node and more than 1 child
                if self.parent[cur_node] is None and children > 1:
                    self.ap[cur_node] = True
                
                # ap condition 2, not root node and 'disc[at] <= low[to]'
                if self.parent[cur_node] and self.low[next_node] >= self.disc[cur_node]:
                    self.ap[cur_node] = True
            
            elif next_node != self.parent[cur_node]:
                self.low[cur_node] = min(self.low[cur_node], self.disc[next_node])
    
    def find_cut_vertices(self) -> list:
        # Using tarjan algorithm
        for i in range(1, self.v + 1):
            if not self.visited[i]:
                self._ap_util(i)
        
        return [index for index, value in enumerate(self.ap) if value]
        

vertex_count, edge_count = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(edge_count)]

graph = Graph(vertex_count, edges)
cut_vertices = graph.find_cut_vertices()

print(len(cut_vertices))
print(*sorted(cut_vertices))
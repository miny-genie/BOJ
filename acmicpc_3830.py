from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)


class DisjointSet:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n+1))
        self.weight_diff = [0] * (n+1)
    
    def union(self, x: int, y: int, diff: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX < rootY:
            self.parent[rootY] = rootX
            self.weight_diff[rootY] = (
                self.weight_diff[x] - self.weight_diff[y] + diff
            )
        else:
            self.parent[rootX] = rootY
            self.weight_diff[rootX] = (
                self.weight_diff[y] - self.weight_diff[x] - diff
            )
            
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            origin_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.weight_diff[x] += self.weight_diff[origin_parent]
        return self.parent[x]
    
    def get_weight_diff(self, x: int) -> int:
        self.find(x)
        return self.weight_diff[x]


while True:
    sample_count, query_count = map(int, input().split())
    if sample_count + query_count == 0:
        break
    
    ds = DisjointSet(sample_count)
    
    for _ in range(query_count):
        cmd, *query = list(input().rstrip().split())
        
        if cmd == "!":
            x, y, diff = map(int, query)
            ds.union(x, y, diff)
            
        else:
            x, y = map(int, query)
            if ds.find(x) == ds.find(y):
                y_weight_diff = ds.get_weight_diff(y)
                x_weight_diff = ds.get_weight_diff(x)
                print(y_weight_diff - x_weight_diff)
            else:
                print("UNKNOWN")
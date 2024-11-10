from sys import stdin
input = stdin.readline


def find(x: int, parent: list[int]) -> int:
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x: int, y: int, rank: list[int], parent: list[int]) -> None:
    rootX = find(x, parent)
    rootY = find(y, parent)
    
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


house_count, road_count = map(int, input().split())

edges = []
for _ in range(road_count):
    u, v, cost = map(int, input().split())
    edges.append((cost, u-1, v-1))
edges.sort()

parent = [i for i in range(house_count + 1)]
rank = [0] * (house_count + 1)

mst_cost = 0
max_edge = 0

for cost, u, v, in edges:
    if find(u, parent) != find(v, parent):
        union(u, v, rank, parent)
        mst_cost += cost
        max_edge = cost

print(mst_cost - max_edge)
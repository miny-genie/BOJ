from itertools import combinations
from sys import stdin
input = stdin.readline


def get_edge_costs(points: list) -> list:
    edges = []
    for p1, p2 in combinations(enumerate(points), 2):
        idx1, (p1x, p1y) = p1
        idx2, (p2x, p2y) = p2
        cost = ((p1x - p2x) ** 2 + (p1y - p2y) ** 2) ** .5
        edges.append((cost, idx1, idx2))
    return sorted(edges)


def find(x: int, parent: list) -> int:
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x: int, y: int, rank: list, parent: list):
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


point_count = int(input())
edges = get_edge_costs([
    list(map(float, input().split()))
    for _ in range(point_count)
])

parent = [i for i in range(point_count)]
rank = [0] * point_count

mst_cost = 0
for cost, u, v in edges:
    if find(u, parent) != find(v, parent):
        union(u, v, rank, parent)
        mst_cost += cost

print(mst_cost)
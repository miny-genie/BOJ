from sys import stdin, setrecursionlimit
setrecursionlimit(100_002)
input = stdin.readline


def union(node1: int, node2: int, parent: list):
    root1 = find(node1, parent)
    root2 = find(node2, parent)    
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2


def find(node: int, parent: list) -> int:
    if parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]


def spanning_tree(info: list, parent: list) -> int:
    total_cost = 0
    connect = 0    
    for cost, a, b in info:
        if find(a, parent) != find(b, parent):
            union(a, b, parent)
            total_cost += cost
            connect += 1
    return total_cost


nodes, edges = map(int, input().split())

graph_info = []
for _ in range(edges):
    u, v, cost = map(int, input().split())
    graph_info.append((cost, u-1, v-1))
graph_info.sort()

parent = [i for i in range(nodes+1)]
spanning_tree_weight = spanning_tree(graph_info, parent)    # Kruskal algorithm
print(spanning_tree_weight)

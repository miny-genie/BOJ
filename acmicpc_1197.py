# ---------- Import ----------
import sys
input = sys.stdin.readline


# ---------- Function ----------
def Union(node1: int, node2: int, parent: list):
    root1 = Find(node1, parent)
    root2 = Find(node2, parent)
    
    if root1 < root2: parent[root2] = root1
    else: parent[root1] = root2


def Find(node: int, parent: list) -> int:
    if parent[node] == node: return node
    else: return Find(parent[node], parent)


def SpanningTree(info: list, parent: list) -> int:
    total_cost = 0
    connect = 0
    
    for cost, a, b in info:
        if Find(a, parent) != Find(b, parent):
            Union(a, b, parent)
            total_cost += cost
            connect += 1
            
    return total_cost


# ---------- Main ----------
nodes, edges = map(int, input().split())

# Edges information input
info = []
for _ in range(edges):
    A, B, cost = map(int, input().split())
    info.append((cost, A-1, B-1))
info.sort()

# Init
parent = [i for i in range(nodes+1)]

# Kruskal algorithm
answer = SpanningTree(info, parent)
print(answer)
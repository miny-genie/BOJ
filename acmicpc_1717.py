# ---------- Import ----------
from sys import setrecursionlimit as srl
srl(10000000)

from sys import stdin
input = stdin.readline


# ---------- Function ----------
def Union(node1, node2, parent):
    node1_root = Find(node1, parent)
    node2_root = Find(node2, parent)
    
    if node1_root == node2_root:
        return
    elif node1_root < node2_root:
        parent[node2_root] = node1_root
    else:
        parent[node1_root] = node2_root


def Find(node, parent):
    if node == parent[node]: return node
    parent[node] = Find(parent[node], parent)
    return Find(parent[node], parent)


# ---------- Main ----------
nodes, times = map(int, input().split())
parent = [i for i in range(nodes+1)]

for _ in range(times):
    cmd, setA, setB = map(int, input().split())
    
    if cmd:
        print("YES") if Find(setA, parent) == Find(setB, parent) else print("NO")
        
    else:
        Union(setA, setB, parent)
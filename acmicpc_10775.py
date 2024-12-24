from sys import stdin
input = stdin.readline


def find(parent: list, x: int) -> int:
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent: list, x: int, y: int):
    rootX = find(parent, x)
    rootY = find(parent, y)
    parent[rootX] = rootY
 

def max_docking(gate_count: int, airplanes: list) -> int:
    parent = [i for i in range(gate_count + 1)]
    
    docked = 0
    for airplane in airplanes:
        available_gate = find(parent, airplane)
        if not available_gate:
            break
        union(parent, available_gate, available_gate - 1)
        docked += 1
        
    return docked


gate_count = int(input())
airplanes = [int(input()) for _ in range(int(input()))]

docked = max_docking(gate_count, airplanes)
print(docked)

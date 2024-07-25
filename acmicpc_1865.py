from sys import stdin
input = stdin.readline


def bellman_ford():
    INF = 1e9
    time = [INF] * (vertex_count + 1)
    time[1] = 0
    
    for i in range(vertex_count):
        for s, e, t in edges:
            if time[s] + t < time[e]:
                time[e] = time[s] + t
                if i == vertex_count - 1:
                    return True
    return False


for _ in range(test_case := int(input())):
    vertex_count, edge_count, wormhole_count = map(int, input().split())
    
    edges = []
    for _ in range(edge_count):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    
    for _ in range(wormhole_count):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    
    cycle = bellman_ford()
    print("YES" if cycle else "NO")
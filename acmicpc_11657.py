from sys import stdin
input = stdin.readline


def bellamn_ford(node_count: int, edges: list) -> tuple[bool, list]:
    distance = [float('inf')] * (node_count + 1)
    distance[1] = 0
    
    for round in range(node_count):
        for curr_node, next_node, cost in edges:
            if distance[curr_node] + cost < distance[next_node]:
                distance[next_node] = distance[curr_node] + cost
                if round == node_count - 1:
                    return True, []
    
    return False, distance[2:]


node_count, edge_count = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(edge_count)]

neg_cycle, distance = bellamn_ford(node_count, edges)
print(-1 if neg_cycle else '\n'.join(map(str, distance)).replace("inf", "-1"))
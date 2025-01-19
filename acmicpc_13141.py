from sys import stdin
input = stdin.readline

INF = float('inf')


def init_graph(n: int, edges: list) -> list:
    graph = [[] for _ in range(n + 1)]
    for s, e, length in edges:
        graph[s].append((e, length))
        graph[e].append((s, length))
    return graph


def floyd_warshall(n: int, graph: list) -> list:
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dist[i][i] = 0
    for s in range(1, n + 1):
        for e, length in graph[s]:
            dist[s][e] = min(dist[s][e], length)
    
    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])
    
    return dist


def time_to_ignition(n: int, edges: list) -> int:
    min_time = INF
    graph = init_graph(node_count, edges)
    dist = floyd_warshall(n, graph)
    
    for start_node in range(1, n + 1):
        cur_time = 0
        
        for node_a, node_b, edge_length in edges:
            start_to_a = dist[start_node][node_a]
            start_to_b = dist[start_node][node_b]
            
            time_diff = abs(start_to_a - start_to_b)
            early_arrival = min(start_to_a, start_to_b)
            
            # 한 쪽에서 다 태울동안, 다른 쪽에 도착하지 않음
            if time_diff > edge_length:
                cur_time = max(
                    cur_time,
                    early_arrival + edge_length
                )
            
            # 한 쪽에서 태울 때, 다른 쪽에 도착해서 같이 태움
            else:
                one_burn = time_diff
                other_burn = (edge_length - one_burn) / 2
                
                cur_time = max(
                    cur_time,
                    early_arrival + one_burn + other_burn
                )
        
        min_time = min(min_time, cur_time)
    
    return min_time


node_count, edge_count = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(edge_count)]

min_time = time_to_ignition(node_count, edges)
print(f"{min_time:.1f}")

# 25.01.19
# Platinum 1: 2181 > 2181 (+0pts)
# 승급까지 -19 > -19
from collections import deque
from sys import stdin
input = stdin.readline


def init() -> tuple[list, list]:
    graph = [[] for _ in range(node_count + 1)]
    indegree = [0] * (node_count + 1)
    
    for _ in range(edge_count):
        s, e, cost = map(int, input().split())
        graph[s].append((e, cost))
        indegree[e] += 1
    
    return graph, indegree


def forward() -> None:
    queue = deque([start])
    
    while queue:
        curr_node = queue.popleft()
        for next_node, move_cost in graph[curr_node]:
            if time[next_node] < time[curr_node] + move_cost:
                time[next_node] = time[curr_node] + move_cost
                road[next_node] = [curr_node]
            elif time[next_node] == time[curr_node] + move_cost:
                road[next_node].append(curr_node)
    
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)


def backward() -> int:
    queue = deque([end])
    route = set()
    
    while queue:
        curr = queue.popleft()
        for prev in road[curr]:
            if (curr, prev) not in route:
                route.add((curr, prev))
                queue.append(prev)
    
    return len(route)


node_count = int(input())
edge_count = int(input())
graph, indegree = init()
start, end = map(int, input().split())

# Find max time and that paths
time = [0] * (node_count + 1)
road = [[] for _ in range(node_count + 1)]

forward()
roads = backward()

print(time[end], roads, sep="\n")

# 25.01.17
# Platinum 1: 2181 > 2181 (+0pts)
# 승급까지 -19 > -19

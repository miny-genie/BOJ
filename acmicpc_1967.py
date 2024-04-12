from collections import deque
from sys import stdin
input = stdin.readline


def bfs(sNode: int) -> tuple[int]:
    distance = [0] * (count+1)
    visited  = [0] * (count+1)
    visited[sNode] = 1
    
    Q = deque([(sNode, 0)])
    
    while Q:
        cur_node, cur_dist = Q.popleft()
        
        for next_node, dist in graph[cur_node]:
            if not visited[next_node]:
                new_dist = cur_dist + dist
                distance[next_node] = new_dist
                visited[next_node] = 1
                Q.append((next_node, new_dist))
    
    max_dist = max(distance)
    max_node = distance.index(max_dist)

    return max_node, max_dist


count = int(input())
graph = [[] for _ in range(count+1)]

for _ in range(count-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))
    
far, _  = bfs(1)
_, dist = bfs(far)
print(dist)
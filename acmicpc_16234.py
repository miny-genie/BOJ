from collections import deque
from sys import stdin
input = stdin.readline


def bfs(graph: list[list[int]], row: int, col: int, visited: list[bool]) -> bool:
    def out_of_bound(graph: list, row: int, col: int) -> bool:
        return not (0 <= row < len(graph) and 0 <= col < len(graph))
    
    def is_association(graph: list, x: int, y: int, nx: int, ny: int) -> bool:
        return min_diff <= abs(graph[x][y] - graph[nx][ny]) <= max_diff
    
    # Initialization
    association = [(row, col)]
    total_population = graph[row][col]
    
    queue = deque([(row, col)])
    visited[row][col] = True
    
    # Find any population move and Make association
    while queue:
        x, y = queue.popleft()
        
        # Check UDLR ground
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = dx + x
            ny = dy + y
            
            # End condition
            if out_of_bound(graph, nx, ny) or visited[nx][ny]:
                continue
            
            # Neighbor difference is between min_diff(L) and max_diff(R)
            if is_association(graph, x, y, nx, ny):
                visited[nx][ny] = True
                total_population += graph[nx][ny]
                queue.append((nx, ny))
                association.append((nx, ny))
    
    # Formed association
    if len(association) >= 2:
        avg_population = total_population // len(association)
        for row, col in association:
            graph[row][col] = avg_population
        return True
    
    # Don't formed association
    else:
        return False    


n, min_diff, max_diff = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

move_count = 0
while True:
    visited = [[False] * n for _ in range(n)]
    anyone_move = False
    
    for row in range(n):
        for col in range(n):
            if not visited[row][col]:
                move_state = bfs(graph, row, col, visited)
                anyone_move |= move_state
    
    if not anyone_move:
        break
    else:
        move_count += 1
    
print(move_count)
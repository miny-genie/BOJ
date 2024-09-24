from collections import deque
from itertools import combinations
from sys import stdin
input = stdin.readline


def compute_spread_time(lab: list, activate_virus: tuple) -> int|float:
    def in_bound(x: int, y: int, size: int) -> bool:
        return 0 <= x < size and 0 <= y < size
    
    visited = [[-1] * len(lab) for _ in range(len(lab))]
    
    # Visited active virus and add queue
    queue = deque()
    for row, col in activate_virus:
        visited[row][col] = 0
        queue.append((row, col))
    
    # Initialization
    time_spread = 0
    infected_count = 0
    
    # Do bfs
    while queue:
        x, y = queue.popleft()
        
        # Search all directions
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = dx + x, dy + y
            
            # (nx, ny) is inbound and not yet visited
            if in_bound(nx, ny, len(lab)) and visited[nx][ny] == -1:
                
                # (nx, ny) state is empty space
                if lab[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    time_spread = visited[nx][ny]
                    infected_count += 1
                
                # (nx, ny) state is non-active virus
                elif lab[nx][ny] == 2:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    
    # Fill all space than return time_spread, or not return infinity
    return time_spread if infected_count == empty_space else float('inf')


lab_size, virus_count = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(lab_size)]

viruses = []
empty_space = 0

for row in range(lab_size):
    for col in range(lab_size):
        if lab[row][col] == 2:
            viruses.append((row, col))
        elif lab[row][col] == 0:
            empty_space += 1
    
min_time = min(
    compute_spread_time(lab, activate_virus)
    for activate_virus in combinations(viruses, virus_count)
)
print(-1 if isinstance(min_time, float) else min_time)
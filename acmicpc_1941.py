from collections import deque
from itertools import combinations
from sys import stdin
input = stdin.readline


def is_valid(positions: list[tuple[int]]) -> bool:
    first_value = positions[0]
    queue = deque([first_value])
    visited = {first_value}
    
    connect = 1
    s_count = 1 if room[first_value[0]][first_value[1]] == "S" else 0
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = dx + x
            ny = dy + y
            if (nx, ny) in positions and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
                connect += 1
                if room[nx][ny] == "S":
                    s_count += 1
    
    return connect == 7 and s_count >= 4


room = [input().rstrip() for _ in range(5)]

answer = sum(
    1
    for comb in combinations(range(25), 7)
    if is_valid([divmod(i, 5) for i in comb])
)
print(answer)

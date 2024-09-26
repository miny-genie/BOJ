from collections import deque
from sys import stdin
input = stdin.readline


def find_eatable_fish(bowl_info: list, baby_size: int, baby_x: int, baby_y: int) -> list:
    def out_of_bound(x: int, y: int, size: int) -> bool:
        return x < 0 or size <= x or y < 0 or size <= y
    
    # Initialization
    bowl_size = len(bowl_info)
    visited = [[False] * bowl_size for _ in range(bowl_size)]
    visited[baby_x][baby_y] = True
    
    queue = deque([(baby_x, baby_y, 0)])
    eatable_fish = []
    
    # Do bfs
    while queue:
        x, y, dist = queue.popleft()
        
        # Check all directions
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = dx + x, dy + y            
            
            # End condition
            if out_of_bound(nx, ny, bowl_size) or visited[nx][ny]:
                continue
            
            # Baby shark can move
            if (state := bowl_info[nx][ny]) <= baby_size:
                visited[nx][ny] = True
                queue.append((nx, ny, dist+1))
                
                # Noy only move but eating
                if 0 < state < baby_size:
                    eatable_fish.append((nx, ny, dist+1))
    
    # Sort key
    # 1. distance ASC / 2. row coordinate ASC / 3. col coordinate ASC  
    return sorted(eatable_fish, key=lambda x: (x[2], x[0], x[1]))


def survive_baby_shark(bowl_size: int, bowl_info: list) -> int:
    # Initialization
    baby_shark_pos = [
        (x, y)
        for x in range(bowl_size) for y in range(bowl_size)
        if bowl_info[x][y] == 9
    ][0]
    baby_shark_size = 2
    eat_stack = 0
    spend_time = 0
    
    # Survive baby shark
    while True:
        eatable_fish = find_eatable_fish(bowl_info, baby_shark_size, *baby_shark_pos)
        if not eatable_fish:
            break
        
        # One or more than eatable_fish, anyway have to eat first element
        x, y, dist = eatable_fish[0]
        
        # baby_shark move to eat fish, and spent time(distance)
        spend_time += dist
        bowl_info[baby_shark_pos[0]][baby_shark_pos[1]] = 0
        bowl_info[x][y] = 9
        baby_shark_pos = (x, y)
        
        # When baby_shark eat as many as baby_shark_size, then baby_shark bigger 
        eat_stack += 1
        if eat_stack == baby_shark_size:
            baby_shark_size += 1
            eat_stack = 0
    
    # baby_shark calls mom!
    return spend_time


bowl_size = int(input())
bowl_info = [list(map(int, input().split())) for _ in range(bowl_size)]
time = survive_baby_shark(bowl_size, bowl_info)
print(time)
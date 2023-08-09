# ---------- Import ----------
from itertools import combinations
import sys
input = sys.stdin.readline

# ---------- Main ----------
N, K = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

city_chicken_distance = 1e9
houses = [(x, y) for x in range(N) for y in range(N) if city[x][y] == 1]
chickens = [(x, y) for x in range(N) for y in range(N) if city[x][y] == 2]

# Select chicken place using combinations
for matrix in combinations(chickens, K):
    tmp = 0
    
    # Brute force every house
    for hx, hy in houses:
        chicken_distance = 1e9
        
        # Calculating chicken distance
        for cx, cy in matrix:
            distance = abs(hx-cx) + abs(hy-cy)
            chicken_distance = min(chicken_distance, distance)
            
        tmp += chicken_distance
    
    # Compare chicken distance
    city_chicken_distance = min(city_chicken_distance, tmp)
        
print(city_chicken_distance)
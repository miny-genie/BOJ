from itertools import combinations
from sys import stdin
input = stdin.readline


def calculate_min_vector(total_x: int, total_y: int, point_count: int, points: list) -> float:
    def get_vector(total_x: int, total_y: int, part_total_x: int, part_total_y: int) -> float:
        other_total_x = total_x - part_total_x
        other_total_y = total_y - part_total_y
        x_component = (other_total_x - part_total_x) ** 2
        y_component = (other_total_y - part_total_y) ** 2
        return (x_component + y_component) ** .5
    
    min_vector = float('inf')
    combs = list(combinations(points, point_count//2))
    for comb in combs:
        part_total_x = 0
        part_total_y = 0
        
        for x, y in comb:
            part_total_x += x
            part_total_y += y
        
        cur_vector = get_vector(total_x, total_y, part_total_x, part_total_y)
        min_vector = min(min_vector, cur_vector)
    
    return min_vector


for _ in range(test_case := int(input())):
    point_count = int(input())
    points, total_x, total_y = [], 0, 0
    
    for _ in range(point_count):
        x, y = map(int, input().split())
        total_x += x
        total_y += y
        points.append((x, y))
    
    min_vector = calculate_min_vector(total_x, total_y, point_count, points)
    print(min_vector)

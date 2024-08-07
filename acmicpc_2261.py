from itertools import combinations
from sys import stdin
input = stdin.readline

X, Y = 0, 1


def pythagorean_theorem(s: int, e: int) -> int:
    return (s[X] - e[X]) ** 2 + (s[Y] - e[Y]) ** 2


def compute_min_distance(start: int, end: int) -> int:
    return min(
        pythagorean_theorem(points[s], points[e])
        for s, e in combinations(range(start, end), 2)
    )


def find_min_distance(start: int, end: int) -> int:
    elements = end - start
    if elements <= 3:
        return compute_min_distance(start, end)
    
    mid = (start + end) // 2
    left_min_dist  = find_min_distance(start, mid)
    right_min_dist = find_min_distance(mid, end)
    
    min_dist = min(left_min_dist, right_min_dist)
    
    base_point_x = points[mid][X]
    combine_check_points = [
        points[i]
        for i in range(start, end)
        if (points[i][X] - base_point_x) ** 2 <= min_dist
    ]
    combine_check_points.sort(key=lambda point: point[Y])
    
    for i in range(len(combine_check_points)):
        now = combine_check_points[i]
        for j in range(i+1, len(combine_check_points)):
            comp = combine_check_points[j]
            if (now[Y] - comp[Y]) ** 2 >= min_dist:
                break
            min_dist = min(min_dist, pythagorean_theorem(now, comp))
    
    return min_dist


point_count = int(input())
points = [list(map(int, input().split())) for _ in range(point_count)]
points.sort(key=lambda point: point[X])

answer = find_min_distance(0, point_count)
print(answer)
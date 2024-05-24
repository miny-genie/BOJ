from math import atan2, ceil, sqrt
from sys import stdin
input = stdin.readline

X, Y = 0, 1


def graham_scan(points: list) -> list:
    def polar_angle(p1: list, p2: list) -> float:
        y_span = p2[Y] - p1[Y]
        x_span = p2[X] - p1[X]
        return atan2(y_span, x_span)

    def distance(p1: list, p2: list) -> int:
        return (p2[X] - p1[X])**2 + (p2[Y] - p1[Y])**2

    def ccw(p1: list, p2: list, p3: list) -> int:
        vector1 = (p2[X] - p1[X]) * (p3[Y] - p1[Y])
        vector2 = (p2[Y] - p1[Y]) * (p3[X] - p1[X])
        return vector1 - vector2
    
    points.sort(key=lambda p: (-p[Y], -p[X]))
    start = points.pop()
    points.sort(key=lambda p: (polar_angle(start, p), distance(start, p)))
    
    hull = [start]
    for point in points:
        while len(hull) > 1 and ccw(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)
    return hull + [start]


def calculate_min_width(hull: list) -> float:
    def get_line_equation(p1: list, p2: list) -> tuple:
        return p2[Y]-p1[Y], p1[X]-p2[X], p2[X]*p1[Y]-p1[X]*p2[Y]
    
    def distance_point_to_line(point: list, line: tuple) -> float:
        x, y = point
        a, b, c = line
        return abs(a*x + b*y + c) / sqrt(a**2 + b**2)
    
    def ceil_to_two_decimal_places(num):
        return ceil(num * 100) / 100
    
    min_width = float('inf')
    for i in range(len(hull)-1):
        max_width = -float('inf')
        p1, p2 = hull[i], hull[i+1]
        line = get_line_equation(p1, p2)
        
        for point in range(len(hull)):
            if point == i or point == i+1:
                continue
            distance = distance_point_to_line(hull[point], line)
            max_width = max(max_width, distance)
            
        min_width = min(min_width, max_width)
    
    return ceil_to_two_decimal_places(min_width)


case = 1
while True:
    point_count = int(input())
    if not point_count:
        break
    
    points = [list(map(int, input().split())) for _ in range(point_count)]
    hull = graham_scan(points)
    min_width = calculate_min_width(hull)
    
    print(f"Case {case}: {min_width:.2f}")
    case += 1
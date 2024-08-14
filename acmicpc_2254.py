from math import atan2
from sys import stdin
input = stdin.readline

X, Y = 0, 1


def ccw(point1: list, point2: list, point3: list) -> int:
    vector1 = (point3[X] - point2[X]) * (point1[Y] - point3[Y])
    vector2 = (point3[Y] - point2[Y]) * (point1[X] - point3[X])
    return vector1 - vector2


def get_convex_hull(points: list, used: dict) -> list:    # graham_scan
    def pythagoras_distance(point1: list, point2: list) -> int:
        return (point1[X] - point2[X]) ** 2 + (point1[Y] - point2[Y]) ** 2
    
    def polar_angle(point1: list, point2: list) -> float:
        y_span = point2[Y] - point1[Y]
        x_span = point2[X] - point1[X]
        return atan2(y_span, x_span)
    
    if not points:
        return [(0, 0)], []
    
    # biggest y, tie-breaker than smallest x
    points.sort(key=lambda point: (point[Y], -point[X]))
    start = points.pop()
    points.sort(
        key=lambda
        p: (-polar_angle(start, p), pythagoras_distance(start, p))
    )
    
    hull = [start]
    for point in points:
        while len(hull) > 1 and ccw(hull[-2], hull[-1], point) >= 0:
            hull.pop()
        hull.append(point)
    points = list(set(points) - set(hull))
    return hull, points


def is_inside(hull: list, point: list) -> bool:
    for i in range(len(hull)):
        next_i = (i + 1) % len(hull)
        if ccw(hull[i], hull[next_i], point) >= 0:
            return False
    return True


def count_layers(points: list, prison: tuple) -> int:
    layers, used = 0, dict()
    while True:
        convex_hull, points = get_convex_hull(points, used)
        if is_inside(convex_hull, prison):
            layers += 1
        else:
            return layers


point_count, prison_x, prison_y = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(point_count)]
layers = count_layers(points, (prison_x, prison_y))
print(layers)

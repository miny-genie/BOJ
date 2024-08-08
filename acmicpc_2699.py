from math import atan2
from sys import stdin
input = stdin.readline

X, Y = 0, 1


def problem_specific_input(point_count: int) -> list:
    points = []
    range_time = point_count // 5 + 1 if point_count % 5 else point_count // 5
    for _ in range(range_time):
        five_point = list(map(int, input().split()))
        for i in range(len(five_point) // 2):
            points.append((five_point[2*i], five_point[2*i+1]))
    return points


def get_pythagoras_distance(point1: list, point2: list) -> int:
    return (point1[X] - point2[X]) ** 2 + (point1[Y] - point2[Y]) ** 2


def get_polar_angle(point1: list, point2: list) -> float:
    y_span = point2[Y] - point1[Y]
    x_span = point2[X] - point1[X]
    return atan2(y_span, x_span)


def get_ccw(point1: list, point2: list, point3: list) -> int:
    vector1 = (point3[X] - point2[X]) * (point1[Y] - point3[Y])
    vector2 = (point3[Y] - point2[Y]) * (point1[X] - point3[X])
    return vector1 - vector2


def graham_scan(points: list) -> list:
    points.sort(key=lambda point: (point[Y], -point[X]))
    start = points.pop()
    points.sort(
        key=lambda
        p: (-get_polar_angle(start, p), get_pythagoras_distance(start, p))
    )
    
    hull = [start]
    for point in points:
        while len(hull) > 1 and get_ccw(hull[-2], hull[-1], point) >= 0:
            hull.pop()
        hull.append(point)
    return hull


def print_elements(elements: list) -> None:
    for element in elements:
        print(*element)


test_case = int(input())
for _ in range(test_case):
    point_count = int(input())
    points = problem_specific_input(point_count)
    hull = graham_scan(points)
    print(len(hull))
    print_elements(hull)
from math import atan2
from sys import stdin
input = stdin.readline


def specific_input() -> tuple[int, int, bool]:
    x, y, include = input().rstrip().split()
    return int(x), int(y), True if include == "Y" else False


def sort(points: list) -> list:
    def polar_angle(point1: list, point2: list) -> float:
        y_span = point2[1] - point1[1]
        x_span = point2[0] - point1[0]
        return atan2(y_span, x_span)

    def squared_distance(point1: list, point2: list) -> int:
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
    
    def ccw(point1: list, point2: list, point3: list) -> int:
        vector1 = (point3[0] - point2[0]) * (point1[1] - point3[1])
        vector2 = (point3[1] - point2[1]) * (point1[0] - point3[0])
        return vector1 - vector2
    
    points.sort(key=lambda point: (-point[0], -point[1]))
    start = points.pop()
    
    points.sort(
        key=lambda point:
        (polar_angle(start, point), -squared_distance(start, point))
    )
    end = points.pop()

    points.sort(
        key=lambda point:
        (polar_angle(start, point), squared_distance(start, point))
    )
    
    end_bound = []
    for point in reversed(points):
        if ccw(start, end, point) == 0:
            end_bound.append(points.pop())
    
    return [start] + points + end_bound + [end]


def print_unpacking_list(list2d: list) -> None:
    print(len(list2d))
    for list1d in list2d:
        print(*list1d)


point_count = int(input())
points = []

for _ in range(point_count):
    x, y, include = specific_input()
    if include:
        points.append((x, y))

print_unpacking_list(sort(points))
######################################################################
########################### 1. Graham Scan ###########################
######################################################################
from math import atan2
from sys import stdin
input = stdin.readline

X, Y = 0, 1


# https://blog.spiralmoon.dev/entry/프로그래밍-이론-두-점-사이의-절대각도를-재는-atan2
def polar_angle(p1: list, p2: list) -> float:
    y_span = p2[Y] - p1[Y]
    x_span = p2[X] - p1[X]
    return atan2(y_span, x_span)


def distance(p1: list, p2: list) -> int:
    return (p2[X] - p1[X])**2 + (p2[Y] - p1[Y])**2


# https://snowfleur.tistory.com/98
def ccw(p1: list, p2: list, p3: list) -> int:
    vector1 = (p2[X] - p1[X]) * (p3[Y] - p1[Y])
    vector2 = (p2[Y] - p1[Y]) * (p3[X] - p1[X])
    return vector1 - vector2


def graham_scan(points: list) -> list:
    points.sort(key=lambda p: (-p[Y], -p[X]))
    start = points.pop()
    points.sort(key=lambda p: (polar_angle(start, p), distance(start, p)))
    
    hull = [start]
    for point in points:
        while len(hull) > 1 and ccw(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)
    return hull


points = [list(map(int, input().split())) for _ in range(int(input()))]
hull = graham_scan(points)
print(len(hull))


######################################################################
##################### 2. Andrew's Monotone Chain #####################
######################################################################
from sys import stdin
input = stdin.readline

X, Y = 0, 1


def ccw(p1: list, p2: list, p3: list) -> int:
    vector1 = (p2[X] - p1[X]) * (p3[Y] - p1[Y])
    vector2 = (p2[Y] - p1[Y]) * (p3[X] - p1[X])
    return vector1 - vector2


def andrew_monotone_chain(points: list) -> list:
    points.sort()
    
    # build upper bull
    upper = []
    for point in reversed(points):
        while len(upper) > 1 and ccw(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
        
    # build lower hull
    lower = []
    for point in points:
        while len(lower) > 1 and ccw(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    
    return upper[:-1] + lower[:-1]


points = [list(map(int, input().split())) for _ in range(int(input()))]
hull = andrew_monotone_chain(points)
print(len(hull))
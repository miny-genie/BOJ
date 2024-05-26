from dataclasses import dataclass
from math import atan2
from sys import stdin
input = stdin.readline

POINT = 1


@dataclass
class Point:
    x: int
    y: int


def graham_scan(points: list) -> list:
    def polar_angle(p1: Point, p2: Point) -> float:
        y_span = p2.y - p1.y
        x_span = p2.x - p1.x
        return atan2(y_span, x_span)
    
    def distance(p1: Point, p2: Point) -> int:
        return (p2.x - p1.x)**2 + (p2.y - p1.y)**2
    
    def ccw(p1: Point, p2: Point, p3: Point) -> int:
        vector1 = (p2.x - p1.x) * (p3.y - p1.y)
        vector2 = (p2.y - p1.y) * (p3.x - p1.x)
        return vector1 - vector2
    
    def make_polygon(start: list, points: list) -> list:
        pop_count = 0
        end_polar_angle = polar_angle(start[POINT], points[-1][POINT])
        for _, point in points:
            if polar_angle(start[POINT], point) == end_polar_angle:
                pop_count += 1
                
        reverse = [points.pop() for _ in range(pop_count)]
        ret = [i for i, _ in [start] + points + reverse]
        return ret
    
    points.sort(key=lambda p: (-p[POINT].y, -p[POINT].x))
    start = points.pop()
    points.sort(
        key=lambda p:
        (polar_angle(start[POINT], p[POINT]), distance(start[POINT], p[POINT]))
    )
    
    hull = [start]
    for idx, point in points:
        if len(hull) > 1 and ccw(hull[-2][POINT], hull[-1][POINT], point) < 0:
            ret = make_polygon(start, points)
            return ret
        
        hull.append([idx, point])
        
    return [i for i, _ in hull]


test_case = int(input())
for _ in range(test_case):
    point_count, *info = list(map(int, input().split()))
    points = [
        [i//2, Point(info[i], info[i+1])]
        for i in range(0, len(info), 2)
    ]
    hull = graham_scan(points)
    print(*hull)
    
    
# ---------- Comment ----------
# dataclass는 Python 3.7에 도입한 기능
# 데이터 중심 클래스의 보일러플레이트 코드를 줄이는 데 유용
# __init__(), __repr__(), __eq__() 등의 메소드를 자동으로 생성
# 해당 부분에서 오버헤드가 발생하여 최적화, 메모리, 시간에서 차이가 발생
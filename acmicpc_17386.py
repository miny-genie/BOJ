from sys import stdin
input = stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    return (x3-x2) * (y1-y3) - (y3-y2) * (x1-x3)


def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)
    return ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
print(1 if is_intersect(x1, y1, x2, y2, x3, y3, x4, y4) else 0)
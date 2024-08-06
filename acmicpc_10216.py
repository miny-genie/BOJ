from math import sqrt
from sys import stdin
input = stdin.readline


class Circle:
    def __init__(self, x: int, y: int, r: int) -> None:
        self.x = x
        self.y = y
        self.r = r


class DisjointSet:
    def __init__(self, circle_count: int, circles: list) -> None:
        self.circle_count = circle_count
        self.circles = circles
        self.parent = [i for i in range(circle_count)]

    def is_connected(self, circle1: Circle, circle2: Circle) -> bool:
        x_diff = circle1.x - circle2.x
        y_diff = circle1.y - circle2.y
        distance = sqrt(x_diff * x_diff + y_diff * y_diff)
        return distance <= circle1.r + circle2.r
    
    def union(self, u: int, v: int) -> None:
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u < root_v:
            self.parent[root_v] = root_u
        else:
            self.parent[root_u] = root_v
    
    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def solve(self) -> int:
        for i in range(self.circle_count-1):
            for j in range(i+1, self.circle_count):
                if self.is_connected(self.circles[i], self.circles[j]):
                    self.union(i, j)
        return len(set(self.parent))


for _ in range(test_case := int(input())):
    circle_count = int(input())
    circles = [Circle(*map(int, input().split())) for _ in range(circle_count)]
    
    ds = DisjointSet(circle_count, circles)    
    print(ds.solve())
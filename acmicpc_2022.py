from math import sqrt
from sys import stdin
input = stdin.readline


def find_distance(x: float, y: float, c: float) -> float:
    lower, upper = 0, min(x, y)
    while upper - lower > 1e-6:
        distance = (lower + upper) / 2
        
        # Not use square operator(**), because of preventing overflow
        left_height  = sqrt(x*x - distance*distance)
        right_height = sqrt(y*y - distance*distance)
        
        # Using figure similarity
        guess_c = (left_height * right_height) / (left_height + right_height)
        
        # Need to reduce height is to say that need to spread distance
        if guess_c > c:
            lower = distance
        else:
            upper = distance
            
    return distance


x, y, c = map(float, input().split())
distance = find_distance(x, y, c)
print(f"{distance:.3f}")
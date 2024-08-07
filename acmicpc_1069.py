from math import sqrt
from sys import stdin
input = stdin.readline


def pythagorean_theorem(base: int, height: int) -> float:
    return sqrt(base ** 2 + height ** 2)


coord_x, coord_y, jump_dist, jump_time = map(int, input().split())
direct_dist = pythagorean_theorem(coord_x, coord_y)

if direct_dist >= jump_dist:
    jump_and_walk = (direct_dist // jump_dist * jump_time) + (direct_dist % jump_dist)
    jump_and_jump_twice = ((direct_dist // jump_dist - 1) * jump_time) + (jump_time * 2)
    answer = min(jump_and_walk, jump_and_jump_twice)

else:
    jump_and_back = jump_time + (jump_dist - direct_dist)
    jump_twice = jump_time * 2
    answer = min(jump_and_back, jump_twice)

print(min(answer, direct_dist))
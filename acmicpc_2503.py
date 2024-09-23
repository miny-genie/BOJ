from itertools import permutations
from sys import stdin
input = stdin.readline


def find_strikes(baseball_info: list) -> int:
    def compute_strike_n_ball(num: str, check: str) -> tuple:
        strike, ball = 0, 0
        for n, c in zip(num, check):
            if n == c:
                strike += 1
            elif c in num:
                ball += 1
        return strike, ball
    
    possible = [
        ''.join(map(str, perm))
        for perm in permutations(range(1, 10), 3)
    ]
    
    for baseball in baseball_info:
        query, strike, ball = baseball
        
        new_possible = []
        for pos in possible:
            if (strike, ball) == compute_strike_n_ball(pos, str(query)):
                new_possible.append(pos)
        possible = new_possible
        
    return len(possible)


baseball_info = [list(map(int, input().split())) for _ in range(int(input()))]
strikes = find_strikes(baseball_info)
print(strikes)
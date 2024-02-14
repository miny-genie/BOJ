from sys import stdin
input = stdin.readline


def greatest_common_divisor(a: int, b: int) -> int:
    while b > 0: a, b = b, a % b
    return a


gcd, lcm = map(int, input().split())
GOAL = lcm // gcd

div, mod = 1, GOAL
for i in range(1, int(GOAL**0.5)+1):
    if GOAL % i == 0:
        new_div = i
        new_mod = GOAL // i
        
        GCD = greatest_common_divisor(new_div, new_mod)
        if GCD == 1 and (div+mod > new_div+new_mod):
            div = new_div
            mod = new_mod
            
print(div * gcd, mod * gcd)
from functools import reduce
from sys import stdin
input = stdin.readline

MOD = 1_000_000_007


def product_of_fractions(nums: list, dens: list) -> tuple:
    def gcd(x: int, y: int) -> int:
        while y != 0:
            x, y = y, x % y
        return x

    def lcm(x: int, y: int) -> int:
        return x * y // gcd(x, y)

    def simplify_fraction(up: int, dn: int) -> tuple:
        divisor = gcd(up, dn)
        simplified_up = up // divisor
        simplified_dn = dn // divisor
        return simplified_up, simplified_dn
    
    common_den = reduce(lcm, dens)
    total_num = sum(num * (common_den // den) for num, den in zip(nums, dens))
    return simplify_fraction(total_num, common_den)


numerators = []
denominators = []

for _ in range(dice_count := int(input())):
    den, num = map(int, input().split())
    numerators.append(num)
    denominators.append(den)

num, den = product_of_fractions(numerators, denominators)
print((num * pow(den, MOD-2, MOD)) % MOD)



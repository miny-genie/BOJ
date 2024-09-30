from functools import reduce
from sys import stdin
input = stdin.readline


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def get_factors(num: int) -> list:
    factors = set()
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return sorted(factors)[1:]


nums = [int(input()) for _ in range(int(input()))]
diff = [abs(bef-aft) for bef, aft in zip(nums, nums[1:])]
total_gcd = reduce(gcd, diff)
print(*get_factors(total_gcd))
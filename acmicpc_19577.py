from collections import defaultdict
from math import gcd
from random import randrange
from sys import stdin
input = stdin.readline

# UNSIGNED_LONGLONG = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
PRIME_CHECK = set([2, 7, 61])


def miller_rabin(n: int, a: int) -> bool:
    d = (n - 1) // 2
    while d % 2 == 0:
        if pow(a, d, n) == n - 1:
            return True
        d //= 2
    tmp = pow(a, d, n)
    return tmp == n - 1 or tmp == 1


def is_prime(n: int) -> bool:
    if n in PRIME_CHECK:
        return True
    elif n % 2 == 0 or n <= 1:
        return False
    
    for check in PRIME_CHECK:
        if n % check == 0 or not miller_rabin(n, check):
            return False
    return True


def pollard_rho(n: int) -> int:
    if is_prime(n):
        return n
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return 2
    
    x = y = randrange(2, n)
    c = randrange(1, n)
    d = 1
    
    while d == 1:
        x = (pow(x, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n
        y = (pow(y, 2, n) + c) % n
        d = gcd(abs(x - y), n)
        
        if d == n:
            return pollard_rho(n)
    
    if is_prime(d):
        return d
    else:
        return pollard_rho(d)


def prime_factorization(n: int) -> dict:
    if n == 1:
        return {1:1}
    
    prime_factors = defaultdict(int)
    while n > 1:
        div = pollard_rho(n)
        prime_factors[div] += 1
        n //= div
    return dict(prime_factors)


def get_divisors(n: int) -> list[int]:
    prime_factors = prime_factorization(n)
    divisors = [1]
    for prime, exponent in prime_factors.items():
        tmp = []
        for exp in range(1, exponent + 1):
            for div in divisors:
                tmp.append(div * pow(prime, exp))
        divisors.extend(tmp)
    return sorted(divisors)


def euler_phi(n: int) -> int:
    if n == 1:
        return 1
    
    prime_factors = prime_factorization(n)
    for prime_factor in sorted(prime_factors):
        n //= prime_factor
        n *= prime_factor - 1
    return n


n = int(input())
divisors = get_divisors(n)

for prime_factor in divisors:
    if prime_factor * euler_phi(prime_factor) == n:
        print(prime_factor)
        break
else:
    print(-1)

# 24.12.03
# Platinum 1: 2115 > 2117 (+2pts)
# 승급까지 -85 > -83
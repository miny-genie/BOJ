from collections import defaultdict
from math import sqrt
from random import randrange
import sys
input = sys.stdin.readline

# unsigned long long
ULL_LIST = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])


def gcd(a: int, b: int) -> int:
    while b > 0: a, b = b, a % b
    return a


def miller_rabin(is_prime: int, check: int) -> bool:
    exp = (is_prime - 1) // 2
    while exp % 2 == 0:
        if pow(check, exp, is_prime) == is_prime - 1: return 1
        exp //= 2
    tmp = pow(check, exp, is_prime)
    return tmp == is_prime - 1 or tmp == 1


def is_prime(num: int) -> bool:
    if num % 2 == 0: return 0
    if num in ULL_LIST: return 1
    if num <= 1: return 0
    
    for check_num in ULL_LIST:
        if not miller_rabin(num, check_num): return 0    
    return 1


def pollard_rho(n: int) -> int:
    if is_prime(n): return n
    if n % 2 == 0: return 2
    
    x = y = randrange(2, n)
    c = randrange(1, n)
    d = 1
    
    while d == 1:
        x = ((x ** 2 % n) + c) % n
        y = ((y ** 2 % n) + c) % n
        y = ((y ** 2 % n) + c) % n
        d = gcd(abs(x - y), n)
        if d == n: return pollard_rho(n)
        
    if is_prime(d): return d
    else: return pollard_rho(d)

    
def lagrange_theorem(num: int) -> int:
    def four_square(n: int) -> bool:
        while n % 4 == 0:
            n //= 4
        return n % 8 == 7
    
    def three_square(n: int) -> bool:
        prime_dict = defaultdict(int)
        while n > 1:
            div = pollard_rho(n)
            prime_dict[div] += 1
            n //= div
        
        for prime, count in prime_dict.items():
            if prime % 4 == 3 and count % 2 == 1:
                return True
        return False
    
    def square(n: int) -> bool:
        sqrt_n = int(sqrt(n))
        return not (sqrt_n * sqrt_n == n)
    
    if four_square(num):
        return 4
    elif three_square(num):
        return 3
    elif square(num):
        return 2
    else:
        return 1


input_number = int(input())
answer = lagrange_theorem(input_number)
print(answer)
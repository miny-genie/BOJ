from collections import defaultdict
from math import factorial
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

    
def solution(num: int) -> int:
    if num == 4 or num == 1:
        return 1
    
    prime_dict = defaultdict(int)
    while num > 1:
        div = pollard_rho(num)
        prime_dict[div] += 1
        num //= div
        
    for count in prime_dict.values():
        if count > 1:
            return -1
        
    return factorial(len(prime_dict))


for _ in range(caseT := int(input())):
    n = int(input())
    answer = solution(n)
    print(answer)
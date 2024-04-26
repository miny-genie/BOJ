from collections import defaultdict
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
    # if n == 1: return 1
    
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
    
    
def euler_phi(num: int, prime_set: set) -> int:
    for prime in prime_set:
        num //= prime
        num *= prime-1
    return num
    

input_number = int(input())

prime_dict, current_value = defaultdict(int), input_number
while current_value > 1:
    div = pollard_rho(current_value)
    prime_dict[div] += 1
    current_value //= div
    
answer = 1
for count in prime_dict.values():
    answer *= count + 1
    
print(answer)
from bisect import bisect_left
from collections import defaultdict
from math import ceil, sqrt
from random import randrange
import sys
input = sys.stdin.readline

# unsigned long long
ULL_LIST = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])


def gcd(a: int, b: int) -> int:
    while b > 0: a, b = b, a % b
    return a


def is_prime(num: int) -> bool:
    def miller_rabin(is_prime: int, check: int) -> bool:
        exp = (is_prime - 1) // 2
        while exp % 2 == 0:
            if pow(check, exp, is_prime) == is_prime - 1: return 1
            exp //= 2
        tmp = pow(check, exp, is_prime)
        return tmp == is_prime - 1 or tmp == 1
    
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
    def find_all_divisor(idx: int, x: int, factors: list, divisors: list) -> None:
        if idx == len(factors):
            divisors.append(x)
            return
        
        t = 1
        base, max_exp = factors[idx]
        for _ in range(max_exp+1):
            find_all_divisor(idx+1, x*t, factors, divisors)
            t *= base
            
    def find_min_triple(num: int, divisors: list) -> int:
        ans = float('inf')
        
        for divisor in divisors:
            d = num // divisor
            # formula: (w+h)/2 ≥ sqrt(wh)
            opt = ceil(2 * sqrt(divisor))
            if opt + d > ans:
                break
            
            # minimum of formula is w = h = sqrt(k)
            idx = bisect_left(divisors, sqrt(divisor))
            diff = 0
            
            while idx - diff >= 0 or idx + diff < len(divisors):
                FLAG = False
                
                # check lower bound
                frt = idx - diff
                if frt >= 0 and divisor % divisors[frt] == 0:
                    w = divisors[frt]
                    h = divisor // w
                    ans = min(ans, w+h+d)
                    FLAG = True
                
                # check upper bound
                bck = idx + diff
                if bck < len(divisors) and divisor % divisors[bck] == 0:
                    w = divisors[bck]
                    h = divisor // w
                    ans = min(ans, w+h+d)
                    FLAG = True
                    
                if FLAG: break
                diff += 1
            
        return ans
    
    # fatorize number by dictionary
    prime_dict = defaultdict(int)
    compose_number = num

    while compose_number > 1:
        div = pollard_rho(compose_number)
        prime_dict[div] += 1
        compose_number //= div
        
    # create all case of possible divisor
    factors, divisors = list(prime_dict.items()), []
    find_all_divisor(0, 1, factors, divisors)
    divisors.sort()
        
    return find_min_triple(num, divisors)


while True:
    if (num := int(input())) == 0:
        break
    
    answer = solution(num)
    print(answer)
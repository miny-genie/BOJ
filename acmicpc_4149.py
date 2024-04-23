# -------------------- Import --------------------
from random import randrange
import sys
input = sys.stdin.readline

# unsigned long long
ull_list = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])


# -------------------- Function --------------------
def gcd(a, b):
    while b > 0: a, b = b, a % b
    return a


def miller_rabin(is_prime, check):
    exp = (is_prime - 1) // 2
    while exp % 2 == 0:
        if pow(check, exp, is_prime) == is_prime - 1: return 1
        exp //= 2
    tmp = pow(check, exp, is_prime)
    return tmp == is_prime - 1 or tmp == 1


def is_prime(num):
    if num % 2 == 0: return 0
    if num in ull_list: return 1
    if num <= 1: return 0
    
    for check_num in ull_list:
        if not miller_rabin(num, check_num): return 0    
    return 1


def pollard_rho(n):
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


# -------------------- Main --------------------
num = int(input())

answer = []
while num > 1:
    div = pollard_rho(num)
    answer.append(div)
    num //= div
    
answer.sort()
print(*answer, sep="\n")

# 
# https://yabitemporary.tistory.com/entry/5-밀러-라빈-소수판정법과-폴라드-로-소인수분해
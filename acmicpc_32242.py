from collections import defaultdict
from math import gcd
from random import randrange
from sys import stdin
input = stdin.readline


class Formula:
    def __init__(self):
        # Unsigned Long Long
        self.prime_check = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
        
    def miller_rabin(self, n: int, a: int) -> bool:
        d = (n - 1) // 2
        while d % 2 == 0:
            if pow(a, d, n) == n - 1:
                return 1
            d //= 2
        tmp = pow(a, d, n)
        return tmp == n - 1 or tmp == 1

    def is_prime(self, num: int) -> bool:
        if num in self.prime_check:
            return True
        elif num % 2 == 0 or num < 1:
            return False
        
        for check_num in self.prime_check:
            if num % check_num == 0:
                return False
            elif not self.miller_rabin(num, check_num):
                return False
        return True

    def pollard_rho(self, n: int) -> int:
        if self.is_prime(n):
            return n
        elif n == 1:
            return 1
        elif n % 2 == 0:
            return 2
        
        x = y = randrange(2, n)
        c = randrange(1, n)
        d = 1
        
        while d == 1:
            x = ((x ** 2 % n) + c) % n
            y = ((y ** 2 % n) + c) % n
            y = ((y ** 2 % n) + c) % n
            d = gcd(abs(x - y), n)
            if d == n:
                return self.pollard_rho(n)
        
        if self.is_prime(d):
            return d
        else:
            return self.pollard_rho(d)
    
    def get_prime_factor_pairs(self, n: int) -> list:
        origin_num = n
        n = abs(n)
        
        primes = defaultdict(int)
        while n > 1:
            prime = self.pollard_rho(n)
            primes[prime] += 1
            n //= prime
        
        factors = [1]
        for prime, exponent in primes.items():
            tmp = []
            for exp in range(1, exponent + 1):
                for factor in factors:
                    tmp.append(factor * prime ** exp)
            factors.extend(tmp)
        
        pairs = []
        for factor in factors:
            pairs.append((-factor, -origin_num // factor))
            pairs.append((factor, origin_num // factor))
        
        return sorted(pairs)


def solve_equation(a: int, b: int, c: int, d: int) -> None:
    formula = Formula()
    
    if a == 0:
        # Bézout's Identity
        if b and c:
            x = gcd(b, c)
            if d % x == 0:
                print("INFINITY")
            else:
                print(0)
        
        # Cy + D == 0
        elif b == 0 and c:
            if d % c == 0:
                print("INFINITY")
            else:
                print(0)
        
        # By + D == 0
        elif b and c == 0:
            if d % b == 0:
                print("INFINITY")
            else:
                print(0)
        
        # D == 0
        else:
            if d == 0:
                print("INFINITY")
            else:
                print(0)
    
    else:
        # Axy + D == 0
        if b == 0 and c == 0:
            if d == 0:
                print("INFINITY")
            else:
                if d % a == 0:
                    pairs = formula.get_prime_factor_pairs(-d // a)
                    print(len(pairs))
                    for pair in pairs:
                        print(*pair)
                else:
                    print(0)
        
        # Axy + Bx + Cy + D == 0
        else:
            x = b * c - a * d
            if x == 0:
                if c % a == 0 or b % a == 0:
                    print("INFINITY")
                else:
                    print(0)
            else:
                pairs = formula.get_prime_factor_pairs(x)
                
                pairs = sorted(
                    ((div1 - c) // a, (div2 - b) // a)
                    for div1, div2 in pairs
                    if (div1 - c) % a == 0 and (div2 - b) % a == 0
                )
                
                print(len(pairs))
                for pair in pairs:
                    print(*pair)                        
    
    return None


a, b, c, d = map(int, input().split())
solve_equation(a, b, c, d)

# 24.11.29
# Platinum 2: 2092 > Platinum 1: 2100 (+8pts)
# 승급까지 -8 > -100

# 21%에서 틀린 이유: gcd의 잘못된 구현
# 음수를 신경쓰지 않았음 b > 0이 아닌 b != 0이어야 했음, 이후 23%에서 틀림

# 23%에서 틀린 이유: get_prime_factor_pairs의 잘못된 입력
# 내부 로직은 부호를 고려하여 작성했으나, 입력을 부호를 뺸 절댓값으로 넘겨주었음
# 서브태스크 1~3 중 1, 3은 WA / 2는 AC를 받음, 이후 56%에서 틀림

# 56%에서 14점 받은 이유: 조건 구문 처리 실수
# L112에서 d == 0 and d % a로 조건문을 작성했었음
# d % a는 INFINITY가 아니라 0으로 빠지는 구문이라 따로 작성했어야 함
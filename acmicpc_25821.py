from sys import stdin
input = stdin.readline


def is_prime(number: int) -> bool:
    def bottom_up_miller_rabin(
        prime_candidate: int, base: int, exp: int, remain: int
    ) -> bool:
        """This calculation is miller rabin primality test function.\n
        Processed in advance, it is fast in determining many prime numbers.
        """
        result = pow(base, remain, prime_candidate)
        if result == 1 or result == prime_candidate - 1:
            return True
        
        for _ in range(exp - 1):
            result = pow(result, 2, prime_candidate)
            if result == prime_candidate - 1:
                return True
        return False
        
    def top_down_miller_rabin(prime_candidate: int, base: int) -> bool:
        """This calculation is miller rabin primality test function.\n
        Because of simple structure, it is useful just one calculation.
        """
        exp = (prime_candidate - 1) // 2
        while exp % 2 == 0:
            if pow(base, exp, prime_candidate) == prime_candidate - 1:
                return True
            exp //= 2
        tmp = pow(base, exp, prime_candidate)
        return tmp == prime_candidate - 1 or tmp == 1

    test_bases = set([2, 7, 61])
    
    if number in test_bases:
        return True
    if number <= 1 or number % 2 == 0:
        return False
    
    # # Top Down
    # for base in test_bases:
    #     if not top_down_miller_rabin(number, base):
    #         return False
    # return True
    
    # Bottom Up
    exponent = 0
    remainder = number - 1
    while remainder % 2 == 0:
        exponent += 1
        remainder //= 2
    
    for base in test_bases:
        if not bottom_up_miller_rabin(number, base, exponent, remainder):
            return False
    return True


def generate_palindromes(limit: int) -> list:
    def compute(num: int, odd: int) -> int:
        palin = num
        if odd:
            num //= 10
            
        while num > 0:
            palin = (palin * 10) + (num % 10)
            num //= 10
        
        return palin
    
    palindromes = []
    for odd_or_even in range(2):
        i = 1
        while (palin := compute(i, odd_or_even)) <= limit:
            palindromes.append(palin)
            i += 1
            
    return palindromes


start, end = map(int, input().split())
palindromes = generate_palindromes(end)

count = sum(
    True
    for palindrome in palindromes
    if start <= palindrome and is_prime(palindrome)
)
print(count)
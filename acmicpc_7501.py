from sys import stdin
input = stdin.readline

ULL_SET = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])


def is_prime(num: int) -> bool:
    def is_even(n: int):
        return n % 2 == 0

    def miller_rabin(num: int, check: int) -> bool:
        exp = (num - 1) // 2
        while is_even(exp):
            if pow(check, exp, num) == num - 1:
                return 1
            exp //= 2
        
        tmp = pow(check, exp, num)
        return tmp == num-1 or tmp == 1
    
    if num == 9: return True
    if is_even(num): return False
    if num in ULL_SET: return True
    
    for check_num in ULL_SET:
        if not miller_rabin(num, check_num):
            return False
    return True
    

start, end = map(int, input().split())
prime_list = [n for n in range(start, end+1) if is_prime(n)]
print(*prime_list)
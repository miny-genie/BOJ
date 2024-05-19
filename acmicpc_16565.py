from sys import stdin
input = stdin.readline

MOD = 10_007
TOTAL_CARDS = 52


def generate_factorial_list() -> list:
    dp = [1]
    for i in range(1, 52+1):
        dp.append(dp[-1] * i % MOD) 
    return dp


def power(base: int, exp: int) -> int:
    if exp == 0:
        return 1
    
    tmp = power(base, exp//2)
    
    if exp % 2:
        return tmp * tmp * base % MOD
    else: 
        return tmp * tmp % MOD
    
    
def combination(factorial: list, n: int, r: int) -> int:
    up = factorial[n]
    dn = factorial[n-r] * factorial[r] % MOD
    return up * power(dn, MOD-2) % MOD


def solution(player_card: int) -> int:
    all_case = 0
    factorial = generate_factorial_list()
    
    for i in range(1, player_card//4+1):
        parity_weight = (-1) ** (i-1)
        four_card = combination(factorial, 13, i)
        
        n = TOTAL_CARDS - i*4
        r = player_card - i*4
        remaing_cards = combination(factorial, n, r)
        
        all_case += (remaing_cards * four_card * parity_weight) % MOD
    
    return all_case % MOD


player_card = int(input())
answer = solution(player_card)
print(answer)
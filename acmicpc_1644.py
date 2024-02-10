# ---------- Import ----------
from sys import stdin
input = stdin.readline

# ---------- Function ----------
def sieve_of_eratosthenes(end: int) -> list:
    isprime_list = [1 for _ in range(end+1)]
    isprime_list[0] = isprime_list[1] = 0

    for check in range(2, int(end**0.5)+1):
        for rm in range(check+check, end+1, check):
            isprime_list[rm] = 0

    prime_list = []
    for i, boolean in enumerate(isprime_list):
        if boolean:
            prime_list.append(i)

    return prime_list


def solution(prime_list: list) -> bool:
    count, total = 0, 0
    
    end = 0
    for start in range(len(prime_list)):
        while end < len(prime_list) and total < GOAL:
            total += prime_list[end]
            end += 1
            
        if total == GOAL:
            count += 1
            
        elif start > GOAL:
            return count
            
        total -= prime_list[start]
        
    return count

# ---------- Main ----------
LIMIT = 4_000_000
GOAL= int(input())

prime_list = sieve_of_eratosthenes(LIMIT)
answer = solution(prime_list)
print(answer)
from sys import stdin
input = stdin.readline


def generate_prime_numbers(num) -> list:
    numbers = [True] * (num + 1)
    numbers[0] = numbers[1] = False
    for idx in range(2, int(num**.5)+1):
        for not_prime in range(idx+idx, num+1, idx):
            numbers[not_prime] = False
    return numbers


def is_squared_prime(num: int, prime_numbers: list) -> list:
    if num % 2:
        num -= 5
        squared_prime = [2, 3]
    else:
        num -= 4
        squared_prime = [2, 2]
        
    for i in range(2, num+1):
        if prime_numbers[i] and prime_numbers[num-i]:
            squared_prime.append(i)
            squared_prime.append(num-i)
            return squared_prime
    return [-1]


num = int(input())
if num < 8:
    print(-1)
    
else:
    squared_prime = is_squared_prime(num, generate_prime_numbers(num))
    print(*squared_prime)
    
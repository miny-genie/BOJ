from sys import stdin
input = stdin.readline


def count_multiples(prime_count: int, n: int, primes: list) -> int:
    answer = 0
    for subset_mask in range(1, 1 << prime_count):
        common_multiple = 1
        bit_count = 0

        for bit in range(prime_count):
            if subset_mask & (1 << bit):
                common_multiple *= primes[bit]
                bit_count += 1

        if bit_count % 2:
            answer += n // common_multiple
        else:
            answer -= n // common_multiple

    return answer 


prime_count, n = map(int, input().split())
primes = list(map(int, input().split()))
multiples = count_multiples(prime_count, n, primes)
print(multiples)

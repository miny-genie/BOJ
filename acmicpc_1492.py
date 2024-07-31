from sys import stdin
input = stdin.readline

MOD = 1_000_000_007


def faulhaber_formula(N: int, K: int) -> int:
    def generate_factorial_list(n: int) -> list:
        ret = [1, 1]    # 0, 1 index
        for i in range(2, n+1):
            ret.append(ret[-1] * i % MOD)
        return ret
    
    def binomial_coef(n: int, k: int, fact: list) -> int:
        up = fact[n]
        dn = pow(fact[n-k] * fact[k], MOD - 2, MOD)
        return up * dn % MOD
    
    factorial = generate_factorial_list(K+1)
        
    # 1^k + 2^k + ... + n^k
    # k = 0) 1 + 1 + ... + 1 = 1 * n
    sum_of_powers = [N]
    
    # Faulhaber formula
    for k in range(1, K+1):
        inverse = pow(binomial_coef(k+1, k, factorial), -1, MOD)
        const = pow(N+1, k+1, MOD) - 1
        for i in range(0, k):
            binomial = binomial_coef(k+1, i, factorial)
            sum_of_power = sum_of_powers[i]
            const = (const - (binomial * sum_of_power)) % MOD
        const = const * inverse % MOD
        sum_of_powers.append(const)
    
    return sum_of_powers[-1]


n, k = map(int, input().split())
answer = faulhaber_formula(n, k)
print(answer)


from sys import stdin
input = stdin.readline

MOD = 1_000_000_007


def gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b
    return a


def multiply_matrix(A: list, B: list) -> list:
    length = len(A)
    result = [[0] * length for _ in range(length)]
    
    for m in range(length):
        for n in range(length):
            for k in range(length):
                result[m][n] += A[m][k] * B[k][n]
            result[m][n] %= MOD
            
    return result


def power_matirx(base: list, exp: int) -> list:
    if exp == 1:
        return base
    
    tmp = power_matirx(base, exp//2)
    ret = multiply_matrix(tmp, tmp)
    
    if exp % 2:
        return multiply_matrix(ret, base)
    else:
        return ret
    

def fibonacci(n):
    if n == 0: return 0
    
    first_term = [[1, 1], [1, 0]]    
    result = power_matirx(first_term, n)
    return result[1][0]


fir, sec = map(int, input().split())
print(fibonacci(gcd(fir, sec)))

# ---------- Comment ----------
# 1000000000000 100000000000000000
# 730695249
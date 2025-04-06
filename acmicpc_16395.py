from sys import stdin
input = stdin.readline


def power(a: int, n: int) -> int:
    if n == 0:
        return 1
    tmp = power(a, n//2)
    if n % 2:
        return tmp * tmp * a
    else:
        return tmp * tmp


factorial = [1] * (30 + 1)
for i in range(2, 30 + 1):
    factorial[i] = factorial[i-1] * i
    
n, k = map(lambda x: int(x)-1, input().split())

up = factorial[n]
dn = factorial[n-k] * factorial[k]

print(up // dn)
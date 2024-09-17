from sys import stdin
input = stdin.readline

factorial = [1] * (100+1)
for i in range(2, 100+1):
    factorial[i] = factorial[i-1] * i

n = int(input())
up = factorial[n]
dn = factorial[5] * factorial[n-5]
print(up // dn)
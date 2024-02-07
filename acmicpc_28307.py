from sys import stdin
input = stdin.readline

_ = int(input())
upper = list(map(int, input().split()))
lower = list(map(int, input().split()))

total = 0
for i, up in enumerate(upper):
    if i == 0 and up:
        total += 3
        
    elif up:
        total += 3
        if upper[i-1]: total -= 2

for i, dn in enumerate(lower):
    if i == 0 and dn:
        total += 3
        if upper[0]: total -= 2
        
    elif dn:
        total += 3
        if lower[i-1]: total -= 2
        if i % 2 == 0 and upper[i]: total -= 2
        
print(total)
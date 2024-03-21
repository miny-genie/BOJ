from sys import stdin
input = stdin.readline

w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

w_var = (x + t) // w
h_var = (y + t) // h

if w_var % 2: x = w - (x + t) % w
else: x = (x + t) % w

if h_var % 2: y = h - (y + t) % h
else: y = (y + t) % h

print(x, y)